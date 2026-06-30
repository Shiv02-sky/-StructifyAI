import json
import ollama

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
        model="phi3:mini",
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

    # Remove markdown if present
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