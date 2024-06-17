from flask_restful import Api
from app.routes.upload import UploadFile
from app.routes.search import SearchDocuments

def initialize_routes(api: Api):
    api.add_resource(UploadFile, '/upload')
    api.add_resource(SearchDocuments, '/search')
