from functools import wraps
from flask import make_response, jsonify, Blueprint, request
from flask_cors import cross_origin
from models.CitationsModel import CitationsModel
from db.db import db

citations_dp = Blueprint('citations', __name__)


@cross_origin
@citations_dp.route('/get_citations', methods=['POST'])
def get_citations() -> dict:
    data = request.json
    response: tuple = 'No se encontraron citas', 401
    citations = CitationsModel.query.all()

    if citations:
        list_citations: list[dict] = []
        for citation in citations:
            response = {
                'citation_id': citation.citation_id,
                'citation_date': citation.citation_date,
                'description': citation.description,
                'status': citation.status,
                'psychologist_id': citation.psychologist_id,
                'patient_id': citation.patient_id,
                'created_at': citation.created_at,
                'updated_at': citation.updated_at
            }
            list_citations.append(response)

        response = list_citations, 200

    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@citations_dp.route('/add_citation', methods=['POST'])
def add_citation() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al insertar', 401
    if data:
        citation_date = data.get('citation_date', None)
        description = data.get('description', None)
        psychologist_id = data.get('psychologist_id', None)
        patient_id = data.get('patient_id', None)
        citation = CitationsModel(
            citation_date=citation_date,
            description=description,
            psychologist_id=psychologist_id,
            patient_id=patient_id
        )
        db.session.add(citation)
        db.session.commit()
        response = citation, 200
    else:
        response = 'No se han introducido datos', 401

    res, code = response

    return make_response(
        jsonify({
            'citation_id': res.citation_id,
            'citation_date': res.citation_date,
            'description': res.description,
            'psychologist_id': res.psychologist_id,
            'patient_id': res.patient_id,
            'created_at': res.created_at,
            'updated_at': res.updated_at
        }), code)


@cross_origin
@citations_dp.route('/delete_citation', methods=['PUT'])
def delete_citation() -> dict:
    data = request.json
    response = ('Ocurrió un error al eliminar', 401)

    citation_id = data.get('citation_id', None)

    if citation_id:
        citation = CitationsModel.query.get(citation_id)

        if citation:
            db.session.delete(citation)
            db.session.commit()
            response = 'Cita eliminada correctamente!', 200
        else:
            response = 'No se encontró la cita', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@citations_dp.route('/update_citation', methods=['PUT'])
def update_citation() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar', 401)

    citation_id = data.get('citation_id', None)
    citation_date = data.get('citation_date', None)
    description = data.get('description', None)
    psychologist_id = data.get('psychologist_id', None)
    patient_id = data.get('patient_id', None)

    if citation_id:
        citation = CitationsModel.query.get(citation_id)

        if citation:

            citation.citation_date = citation_date
            citation.description = description
            citation.psychologist_id = psychologist_id
            citation.patient_id = patient_id

            try:

                db.session.commit()
                response = 'Cita actualizada correctamente!', 200
            except Exception as e:
                response = (f'Ocurrió un error al actualizar: {str(e)}', 500)
        else:
            response = 'No se encontró la cita', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)
