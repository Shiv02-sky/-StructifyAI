import json
import os
import ollama

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b")

SYSTEM_PROMPT = """
You are an intelligent document analysis assistant.

Extract information from the document.

Return ONLY valid JSON.

Do NOT use markdown.

Use exactly this schema.

{
    "document_type":"",
    "title":"",
    "summary":"",
    "people":[],
    "organizations":[],
    "dates":[],
    "emails":[],
    "phone_numbers":[],
    "addresses":[],
    "keywords":[]
}
"""


def process_document(document_text):
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": document_text
            }
        ]
    )

    output = response["message"]["content"]

    output = output.replace("```json", "")
    output = output.replace("```", "")
    output = output.strip()

    try:
        structured_json = json.loads(output)
    except Exception:
        structured_json = {
            "raw_output": output
        }

    summary = structured_json.get("summary", "")

    return {
        "json": structured_json,
        "summary": summary
    }