def safe_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return float(default)


def normalize_score(value, minimum=0.0, maximum=100.0):
    value = safe_float(value, default=0.0)
    return max(minimum, min(maximum, value))


def calculate_symptom_score(symptoms):
    if not symptoms:
        return 0.0
    selected = symptoms.get("selected_symptoms", [])
    if not isinstance(selected, list):
        return 0.0
    return round((len(selected) / 10.0) * 100.0, 2)


def extract_feature_vector(eye_analysis, reaction, memory, attention, symptoms):
    symptom_score = calculate_symptom_score(symptoms)
    eye_tracking_score = normalize_score(eye_analysis.get("tracking_score", 0))
    eye_consistency = normalize_score(eye_analysis.get("consistency", 0))
    eye_response_delay = safe_float(eye_analysis.get("response_delay", 0), default=0.0)
    reaction_time = safe_float(reaction.get("average_reaction_ms", 0), default=0.0)
    reaction_consistency = normalize_score(reaction.get("consistency", 0))
    memory_score = normalize_score(memory.get("memory_score", 0))
    attention_score = normalize_score(attention.get("attention_score", 0))

    return {
        "eye_tracking_score": round(eye_tracking_score, 2),
        "eye_consistency": round(eye_consistency, 2),
        "eye_response_delay": round(eye_response_delay, 2),
        "reaction_time": round(reaction_time, 2),
        "reaction_consistency": round(reaction_consistency, 2),
        "memory_score": round(memory_score, 2),
        "attention_score": round(attention_score, 2),
        "symptom_score": round(symptom_score, 2),
    }
