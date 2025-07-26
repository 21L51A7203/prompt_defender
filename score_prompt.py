def score_prompt(prompt):
    prompt_lower = prompt.lower()

    injected_keywords = [
        "ignore previous", 
        "act like", 
        "you are no longer", 
        "pretend to", 
        "bypass", 
        "forget instructions",
        "jailbreak",
        "override",
        "i am the system",
        "hacker"
    ]

    injected_score = sum(keyword in prompt_lower for keyword in injected_keywords)
    clean_score = 1 if injected_score == 0 else 0
    verdict = "Clean" if injected_score == 0 else "Injected"

    return {
        "clean_score": clean_score,
        "injected_score": injected_score,
        "verdict": verdict
    }
