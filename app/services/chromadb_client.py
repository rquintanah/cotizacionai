from chromadb import Client
import uuid

class ChromaDBClient:
    def __init__(self):
        self.client = Client()
        self.collection = self.client.get_or_create_collection("example_collection")  # Utiliza get_or_create_collection

    def insert_documents(self, documents):
        ids = [str(uuid.uuid4()) for _ in documents]
        self.collection.add(ids=ids, documents=documents, metadatas=[{"meta": "data"} for _ in documents])
        print(f"Inserted documents into ChromaDB: {documents}")

    def search_documents(self, query):
        results = self.collection.query(query_texts=[query], n_results=5)
        return results['documents']
