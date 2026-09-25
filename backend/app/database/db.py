import json
import os
import sqlite3
from pathlib import Path

default_db_path = Path(__file__).resolve().parents[1] / "neuroguard.db"
DB_PATH = Path(os.getenv("NEUROGUARD_DB_PATH", "/tmp/neuroguard.db" if os.getenv("VERCEL") else default_db_path))


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                profile TEXT NOT NULL,
                symptoms TEXT,
                eye_analysis TEXT,
                reaction TEXT,
                memory TEXT,
                attention TEXT,
                feature_vector TEXT,
                screening_score REAL,
                screening_indication TEXT,
                report_text TEXT
            )
            """
        )
        conn.commit()


def save_assessment(assessment):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO assessments (
                created_at,
                profile,
                symptoms,
                eye_analysis,
                reaction,
                memory,
                attention,
                feature_vector,
                screening_score,
                screening_indication,
                report_text
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                assessment["created_at"],
                json.dumps(assessment["profile"]),
                json.dumps(assessment.get("symptoms", {})),
                json.dumps(assessment.get("eye_analysis", {})),
                json.dumps(assessment.get("reaction", {})),
                json.dumps(assessment.get("memory", {})),
                json.dumps(assessment.get("attention", {})),
                json.dumps(assessment.get("feature_vector", {})),
                assessment.get("screening_score"),
                assessment.get("screening_indication"),
                assessment.get("report_text"),
            ),
        )
        conn.commit()
        return cursor.lastrowid


def fetch_assessment_by_id(assessment_id):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM assessments WHERE id = ?", (assessment_id,)).fetchone()
        if row is None:
            return None
        return dict(row)


def fetch_assessment_history():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM assessments ORDER BY created_at DESC"
        ).fetchall()
        return [dict(row) for row in rows]
