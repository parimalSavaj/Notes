from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# TODO: Write a tool to read a doc
@mcp.tool(
    name="read_doc",
    description="Reads a document and returns its as a string.",
)
def read_doc(doc_id: str = Field(..., description="The ID of the document to read.")) -> str:
    return docs.get(doc_id, "Document not found.")

# TODO: Write a tool to edit a doc
@mcp.tool(
    name="edit_doc",
    description="Edits a document and returns its as a string.",
)
def edit_doc(doc_id: str = Field(..., description="The ID of the document to edit."), content: str = Field(..., description="The new content of the document.")) -> str:
    if doc_id not in docs:
        return "Document not found."
    docs[doc_id] = content
    return "Document edited successfully."

# TODO: Write a resource to return all doc id's
@mcp.resource(
    "docs://documents",
    mime_type="application/json",
)
def get_all_docs() -> list[str]:
    return list(docs.keys())

# TODO: Write a resource to return the contents of a particular doc
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain",
)
def get_doc(doc_id: str) -> str:
    return docs.get(doc_id, "Document not found.")

# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
