from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-sonnet-4-0"

def first_request_with_file():
    file = client.beta.files.upload(
        file=("streaming.csv", open("streaming.csv", "rb"), "text/csv")
    )

    response = client.messages.create(
        model=model,
        max_tokens=2000,
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze churn and prepare data"},
                    {"type": "container_upload", "file_id": file.id},
                ],
            }
        ],
    )

    return response

def followup_request():
    response = client.messages.create(
        model=model,
        max_tokens=2000,
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
        messages=[
            {
                "role": "user",
                "content": "Now create a visualization from the same dataset"
            }
        ],
    )

    return response

res1 = first_request_with_file()
print(res1)

res2 = followup_request()
print(res2)


"""
FILES API + CODE EXECUTION (SHORT NOTE)

1. Files API:
- Upload file once → get file_id
- Use file_id instead of sending file again

2. Code Execution:
- Claude runs Python code in a container
- No internet access
- Can generate plots, files, outputs

3. Workflow:
- Upload file
- Send file using "container_upload"
- Claude analyzes using code
- Returns results + downloadable files

4. Important:
- Send file ONLY in first request
- Next messages → no need to send file again
- File stays available in same session

5. Output:
- Text (analysis)
- Code (executed)
- Files (plots, reports)

Simple idea:
Upload once → reuse in same session
"""