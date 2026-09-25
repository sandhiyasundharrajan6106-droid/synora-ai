def build_report(assessment):
    profile = assessment.get("profile", {})
    symptoms = assessment.get("symptoms", {})
    eye = assessment.get("eye_analysis", {})
    reaction = assessment.get("reaction", {})
    memory = assessment.get("memory", {})
    attention = assessment.get("attention", {})
    screening_score = assessment.get("screening_score", 0.0)
    indication = assessment.get("screening_indication", "UNKNOWN")

    symptom_names = symptoms.get("selected_symptoms", [])
    symptom_summary = ", ".join(symptom_names) if symptom_names else "No major symptoms recorded"

    report_lines = [
        "SYNORA AI REPORT",
        "====================",
        f"Assessment ID: {assessment.get('id', 'N/A')}",
        f"Name: {profile.get('name', 'N/A')}",
        f"Age: {profile.get('age', 'N/A')}",
        f"Athlete status: {profile.get('athlete_status', 'N/A')}",
        f"Sport/activity: {profile.get('sport_activity', 'N/A')}",
        f"Assessment date: {profile.get('assessment_date', 'N/A')}",
        "",
        "Eye movement results:",
        f"- Tracking score: {eye.get('tracking_score', 'N/A')}",
        f"- Consistency: {eye.get('consistency', 'N/A')}",
        f"- Response delay: {eye.get('response_delay', 'N/A')} ms",
        "",
        "Reaction time:",
        f"- Average reaction: {reaction.get('average_reaction_ms', 'N/A')} ms",
        f"- Fastest reaction: {reaction.get('fastest_reaction_ms', 'N/A')} ms",
        f"- Slowest reaction: {reaction.get('slowest_reaction_ms', 'N/A')} ms",
        "",
        "Memory result:",
        f"- Correct: {memory.get('correct', 'N/A')}",
        f"- Incorrect: {memory.get('incorrect', 'N/A')}",
        f"- Memory score: {memory.get('memory_score', 'N/A')}",
        "",
        "Attention result:",
        f"- Correct: {attention.get('correct', 'N/A')}",
        f"- Incorrect: {attention.get('incorrect', 'N/A')}",
        f"- Missed: {attention.get('missed', 'N/A')}",
        f"- Attention score: {attention.get('attention_score', 'N/A')}",
        "",
        "Symptoms:",
        f"- {symptom_summary}",
        "",
        f"Prototype Screening Score: {screening_score}",
        f"Preliminary Screening Indication: {indication}",
        "",
        "Disclaimer:",
        "This tool is for preliminary screening and educational purposes only. It does not replace professional medical evaluation.",
        "NOT A MEDICAL DIAGNOSIS.",
    ]
    return "\n".join(report_lines)
