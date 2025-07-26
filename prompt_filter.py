import re

def heal_prompt(prompt):
    # Rule-based static filtering
    suspicious_phrases = [
        "ignore previous", "bypass", "jailbreak", "as an AI", "confidential", "delete all"
    ]
    pattern = re.compile("|".join(suspicious_phrases), re.IGNORECASE)
    healed = pattern.sub("[REMOVED]", prompt)
    return healed
