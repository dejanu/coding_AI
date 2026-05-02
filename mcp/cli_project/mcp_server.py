from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")


financial_instruments = {
    "stock.md": "This document provides an overview of the stock market and its key players.",
    "bond.pdf": "This document explains the basics of bonds and how they work.",
    "options.docx": "This document describes the different types of options and their uses in trading.",
}


@mcp.tool(name="read_doc", description="Read the contents of a document given its ID.")
def read_doc(doc_id: str = Field(description="The ID of the document to read")) -> str:
    if doc_id not in financial_instruments:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return financial_instruments.get(doc_id, "Document not found.")

@mcp.tool(name="edit_doc",description="Edit the contents of a document ")
def edit_doc(
    doc_id: str = Field(description="The ID of the document to edit"), 
    old_content: str = Field(description="The current content of the document"),
    new_content: str = Field(description="The new content for the document")) -> None:
    if doc_id not in financial_instruments:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    # find and replace the old content with the new content in the document
    financial_instruments[doc_id] = financial_instruments.get(doc_id, "").replace(old_content, new_content)  



@mcp.resource(
    "docs://documents",
    mime_type="application/json",
)
def list_docs() -> list[str]:
    # resource to return all doc id's
    return list(financial_instruments.keys())

@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain",
)
def get_doc(doc_id: str) -> str:
    # resource to return the contents of a particular doc
    if financial_instruments.get(doc_id) is None:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return financial_instruments.get(doc_id, "Document not found.")


# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
