# upload.py

from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
import os
from app.services.pdf_processor import process_pdf

class UploadFile(Resource):
    def post(self):
        # Verificar si 'file' está en la solicitud
        if 'file' not in request.files:
            return {'error': 'No file part'}, 400
        file = request.files['file']
        # Verificar si el nombre del archivo no está vacío
        if file.filename == '':
            return {'error': 'No selected file'}, 400
        # Guardar el archivo si está presente
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            file.save(file_path)
            print(f"File saved to {file_path}")  # Log para verificar que el archivo se guardó
            process_pdf(file_path)  # Llamar a process_pdf correctamente
            return {'message': 'File successfully uploaded'}, 200
