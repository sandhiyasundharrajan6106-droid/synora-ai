import json
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from app.computer_vision.eye_analysis import analyze_eye_tracking
from app.database.db import fetch_assessment_by_id, fetch_assessment_history, get_connection, save_assessment
from app.schemas.assessment import ScreeningAnalyzeRequest
from app.schemas.profile import ProfilePayload
from app.schemas.symptoms import SymptomsPayload
from app.services.feature_extraction import extract_feature_vector
from app.services.report_service import build_report
from app.services.screening_service import analyze as screening_analyze

router = APIRouter()


def decode_record(row):
    record = dict(row)
    for key in ("profile", "symptoms", "eye_analysis", "reaction", "memory", "attention", "feature_vector"):
        if isinstance(record.get(key), str):
            try:
                record[key] = json.loads(record[key])
            except json.JSONDecodeError:
                record[key] = {}
    return record


@router.get("/health")
def api_health():
    return {"status": "ok"}


@router.post("/profile")
def submit_profile(payload: ProfilePayload):
    return {"status": "success", "profile": payload.model_dump()}


@router.post("/symptoms")
def submit_symptoms(payload: SymptomsPayload):
    return {"status": "success", "symptoms": {"selected_symptoms": payload.symptoms, "notes": payload.notes}}


@router.post("/eye-analysis")
def submit_eye_analysis(payload: dict):
    return {"status": "success", "eye_analysis": analyze_eye_tracking(payload)}


@router.post("/cognitive/reaction")
def submit_reaction(payload: dict):
    return {"status": "success", "reaction": payload}


@router.post("/cognitive/memory")
def submit_memory(payload: dict):
    return {"status": "success", "memory": payload}


@router.post("/cognitive/attention")
def submit_attention(payload: dict):
    return {"status": "success", "attention": payload}


@router.post("/screening/analyze")
def analyze_screening_route(payload: ScreeningAnalyzeRequest):
    feature_vector = extract_feature_vector(
        payload.eye_analysis,
        payload.reaction,
        payload.memory,
        payload.attention,
        payload.symptoms,
    )
    screening = screening_analyze(feature_vector)
    assessment = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "profile": payload.profile,
        "symptoms": payload.symptoms,
        "eye_analysis": payload.eye_analysis,
        "reaction": payload.reaction,
        "memory": payload.memory,
        "attention": payload.attention,
        "feature_vector": feature_vector,
        "screening_score": screening["screening_score"],
        "screening_indication": screening["screening_indication"],
    }
    assessment_id = save_assessment(assessment)
    assessment["id"] = assessment_id
    report = build_report(assessment)
    with get_connection() as conn:
        conn.execute("UPDATE assessments SET report_text = ? WHERE id = ?", (report, assessment_id))
        conn.commit()
    return {
        "status": "success",
        "assessment_id": assessment_id,
        "feature_vector": feature_vector,
        "screening_score": screening["screening_score"],
        "screening_indication": screening["screening_indication"],
        "report": report,
        "disclaimer": "This tool is for preliminary screening and educational purposes only. It does not replace professional medical evaluation.",
    }


@router.get("/assessment/history")
def get_assessment_history():
    return {"status": "success", "assessments": [decode_record(row) for row in fetch_assessment_history()]}


@router.get("/assessment/{assessment_id}")
def get_assessment(assessment_id: int):
    row = fetch_assessment_by_id(assessment_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Assessment not found.")
    return {"status": "success", "assessment": decode_record(row)}


@router.get("/report/{assessment_id}")
def get_report(assessment_id: int):
    row = fetch_assessment_by_id(assessment_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Assessment not found.")
    assessment = decode_record(row)
    return {
        "status": "success",
        "assessment_id": assessment_id,
        "filename": f"synora-report-{assessment_id}.txt",
        "content": assessment.get("report_text") or build_report(assessment),
    }
