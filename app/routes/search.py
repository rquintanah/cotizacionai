from flask import request
from flask_restful import Resource
from app.services.chromadb_client import ChromaDBClient

class SearchDocuments(Resource):
    def post(self):
        query = request.json.get('query')
        if not query:
            return {'error': 'Query is required'}, 400

        chromadb_client = ChromaDBClient()
        results = chromadb_client.search_documents(query)
        return {'results': results}, 200
