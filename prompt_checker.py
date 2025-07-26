import os
from main import compare_prompts
from utils.logger import log_event

def analyze_prompts(clean_path, injected_path, output_path):
    try:
        with open(clean_path, 'r', encoding='utf-8') as f:
            clean_prompt = f.read()
        with open(injected_path, 'r', encoding='utf-8') as f:
            injected_prompt = f.read()

        log_event(f"Analyzing prompts from {clean_path} and {injected_path}")
        result = compare_prompts(clean_prompt, injected_prompt)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)

        log_event("Analysis completed. Results saved.")
        return result
    except Exception as e:
        log_event(f"Error: {str(e)}")
        return "❌ Failed to analyze prompts. Check the logs for more details."
