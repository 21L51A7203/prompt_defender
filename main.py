from utils.logger import log_event

def score_prompt(prompt):
    score = 0
    red_flags = ["ignore previous", "disregard above", "you are now", "pretend", "bypass", "as an ai", "simulate", "disobey"]
    for flag in red_flags:
        if flag in prompt.lower():
            score += 10
    return score

def compare_prompts(clean_prompt, injected_prompt):
    log_event("Scoring clean and injected prompts...")
    clean_score = score_prompt(clean_prompt)
    injected_score = score_prompt(injected_prompt)

    result = f"""🔍 Prompt Analysis Report

Clean Prompt Score: {clean_score}
Injected Prompt Score: {injected_score}

Result: {"⚠️ Potential Prompt Injection Detected!" if injected_score > clean_score else "✅ No significant prompt injection detected."}
"""
    return result
