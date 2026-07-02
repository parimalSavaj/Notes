import os
from anthropic import Anthropic

# Initialize the client (ensure ANTHROPIC_API_KEY is in your environment variables)
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# 1. Send the request with citations enabled
message = client.messages.create(
    model="claude-3-5-sonnet-latest", # Citations are supported on Sonnet and Haiku models
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "text",
                        "media_type": "text/plain",
                        "data": "Anthropic was founded in 2021 by former OpenAI researchers. The Claude 3 model family was officially introduced in early 2024, bringing advanced reasoning capabilities."
                    },
                    "title": "Anthropic History",
                    "citations": {"enabled": True} # Critical: Enable citations for this document
                },
                {
                    "type": "text",
                    "text": "When was Anthropic founded and when was Claude 3 released?"
                }
            ]
        }
    ]
)

# 2. Parse the response and extract the citations
answer = ""
citations = []

for block in message.content:
    if block.type == "text":
        answer += block.text
        
    # Check if the text block contains citations
    if hasattr(block, 'citations') and block.citations:
        citations.extend(block.citations)

# 3. Print the results
print("Answer:")
print(answer)
print("\n" + "-"*40 + "\n")
print("Citations extracted from the text:")

for idx, citation in enumerate(citations, 1):
    source_text = citation.cited_text.strip()
    
    # For plain text documents, Claude returns character indices
    start_idx = getattr(citation, 'start_char_index', 'N/A')
    end_idx = getattr(citation, 'end_char_index', 'N/A')
    
    print(f"{idx}. \"{source_text}\"")
    print(f"   Location: Chars {start_idx}-{end_idx} in '{citation.document_title}'\n")



"""
Answer:
Based on the provided text, Anthropic was founded in 2021, and the Claude 3 model family was released in early 2024.

----------------------------------------

Citations extracted from the text:
1. "Anthropic was founded in 2021 by former OpenAI researchers."
   Location: Chars 0-60 in 'Anthropic History'

2. "The Claude 3 model family was officially introduced in early 2024"
   Location: Chars 62-127 in 'Anthropic History'
"""