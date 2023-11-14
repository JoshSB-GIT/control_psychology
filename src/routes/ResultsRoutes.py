from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin
from db.db import db
from models.ResultsModel import ResultsModel

results_dp = Blueprint('results_dp', __name__)


@cross_origin
@results_dp.route('/get_results', methods=['POST'])
def get_results() -> dict:
    data = request.json
    response: tuple = 'No se encontraron resultados', 401
    results = ResultsModel.query.filter(ResultsModel.status == 1).all()

    if results:
        list_results: list[dict] = []
        for result in results:
            response = {
                'result_id': result.result_id,
                'appointment_id': result.appointment_id,
                'rating': result.rating,
                'feedback': result.feedback,
                'status': result.status,
                'create_at': result.create_at,
                'update_at': result.update_at,
            }
            list_results.append(response)

        response = list_results, 200

        if data:
            key = list(data.keys())[0]

            if key:
                value = data.get(key, None)
                for res in list_results:
                    if res[key] == value:
                        response = res, 200
            else:
                response = 'No se encontró el campo', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@results_dp.route('/add_result', methods=['POST'])
def add_result() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al insertar el resultado', 401
    if data:
        appointment_id = data.get('appointment_id', None)
        rating = data.get('rating', None)
        feedback = data.get('feedback', None)

        result = ResultsModel(
            appointment_id=appointment_id,
            rating=rating,
            feedback=feedback
        )

        db.session.add(result)
        db.session.commit()
        response = result, 200
    else:
        response = 'No se han introducido datos', 401

    res, code = response

    return make_response(
        jsonify({
            'appointment_id': res.appointment_id,
            'rating': res.rating,
            'feedback': res.feedback,
            'status': res.status,
            'create_at': res.create_at,
            'update_at': res.update_at
        }), code)
