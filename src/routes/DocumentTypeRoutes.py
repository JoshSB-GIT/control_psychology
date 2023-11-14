from functools import wraps
from flask import make_response, jsonify, Blueprint, request
from flask_cors import cross_origin
from models.DocumentTypeModel import DocumentTypeModel
from db.db import db

document_types_dp = Blueprint('document_types', __name__)

@cross_origin
@document_types_dp.route('/get_document_types', methods=['POST'])
def get_document_types() -> dict:
    data = request.json
    response: tuple = 'No se encontraron documentos', 401
    document_types = DocumentTypeModel.query.all()

    if document_types:
        list_document_types: list[dict] = []
        for document_types in document_types:
            response = {
                'document_type_id': document_types.document_type_id,
                'name': document_types.name,
                'description': document_types.description,
                'status': document_types.status,
                'created_at': document_types.created_at,
                'updated_at': document_types.updated_at
            }
            list_document_types.append(response)

        response = list_document_types, 200

    res, code = response

    return make_response(jsonify({'data': res}), code)