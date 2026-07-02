from dotenv import load_dotenv
load_dotenv()

import base64
from anthropic import Anthropic

client = Anthropic()

def chat_with_pdf(pdf_path, prompt):
    with open(pdf_path, "rb") as f:
        file_bytes = base64.b64encode(f.read()).decode("utf-8")

    response = client.messages.create(
        model="claude-sonnet-4-0",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": file_bytes
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    return response

response = chat_with_pdf(
    "earth.pdf",
    "Summarize this document in one sentence"
)

print(response)