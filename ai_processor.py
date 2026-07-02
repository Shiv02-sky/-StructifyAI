import json
import re

try:
    import ollama
except:
    ollama = None

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


def fallback_json(document_text):
    text = document_text[:4000]

    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    phones = re.findall(r'\b\d{10}\b|\b\d{3,5}[-‐]\d{5,10}\b', text)

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    title = lines[0] if lines else "Document"

    return {
        "document_type": "Document",
        "title": title,
        "summary": "Document processed successfully using fallback extraction.",
        "people": [],
        "organizations": [],
        "dates": [],
        "emails": emails,
        "phone_numbers": phones,
        "addresses": [],
        "keywords": []
    }


def process_document(document_text):
    short_text = document_text[:3000]

    if ollama is not None:
        try:
            response = ollama.chat(
                model="phi3:mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": short_text}
                ]
            )

            output = response["message"]["content"].strip()
            output = output.replace("```json", "").replace("```", "").strip()

            structured_json = json.loads(output)
            summary = structured_json.get("summary", "Document processed successfully.")

            return {
                "json": structured_json,
                "summary": summary
            }

        except Exception:
            pass

    structured_json = fallback_json(short_text)

    return {
        "json": structured_json,
        "summary": structured_json["summary"]
    }