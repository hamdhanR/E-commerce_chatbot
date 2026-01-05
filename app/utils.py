# app/utils.py
import re
import json
from bson import json_util

def extract_mongo_pipeline(llm_output: str):
    """
    Extract a MongoDB aggregation pipeline from LLM output string.
    """
    # Remove markdown fences if present
    cleaned = re.sub(r"```(?:json)?|```", "", llm_output).strip()

    # Regex to extract MongoDB pipeline
    pattern = r'(\[\s*\{[\s\S]*?\}\s*\])'
    match = re.search(pattern, cleaned)

    if not match:
        raise ValueError("No valid MongoDB pipeline found in LLM output")

    pipeline_str = match.group(1)

    # Convert string → Python object
    return json.loads(pipeline_str)


def safe_json_dumps(data):
    """
    Convert MongoDB data to JSON string safely.
    """
    return json_util.dumps(data, indent=2)
