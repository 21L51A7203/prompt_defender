# logger.py
import logging
import os

# Ensure log directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging format
logging.basicConfig(
    filename='logs/analysis.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def log_prompt_analysis(prompt_type, prompt_text, score, detected_patterns):
    logging.info(
        f"TYPE: {prompt_type} | SCORE: {score} | PATTERNS: {detected_patterns} | PROMPT: {prompt_text}"
    )
