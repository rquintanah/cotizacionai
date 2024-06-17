from app.utils.file_utils import extract_text_from_pdf
from app.services.chromadb_client import ChromaDBClient

def process_pdf(file_path):
    text_content = extract_text_from_pdf(file_path)
    print(f"Extracted text: {text_content}")

    documents = [text_content]
    chromadb_client = ChromaDBClient()
    chromadb_client.insert_documents(documents)
    print("Inserted documents into ChromaDB")
