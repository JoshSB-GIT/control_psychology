from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin
from db.db import db
from models.HistoryModel import HistoryModel

history_dp = Blueprint('history_dp', __name__)


@cross_origin
@history_dp.route('/get_history', methods=['POST'])
def get_history() -> dict:
    data = request.json
    response: tuple = 'No se encontraron historiales', 401
    histories = HistoryModel.query.filter(HistoryModel.status == 1).all()

    if histories:
        list_history: list[dict] = []
        for history in histories:
            response = {
                'history_id': history.history_id,
                'patient_id': history.patient_id,
                'psychologist_id': history.psychologist_id,
                'status': history.status,
                'update_at': history.update_at,
                'create_at': history.create_at,
            }
            list_history.append(response)

        response = list_history, 200

        if data:
            key = list(data.keys())[0]

            if key:
                value = data.get(key, None)
                for h in list_history:
                    if h[key] == value:
                        response = h, 200
            else:
                response = 'No se encontró el campo', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@history_dp.route('/add_history', methods=['POST'])
def add_history() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al insertar el historial', 401
    if data:
        patient_id = data.get('patient_id', None)
        psychologist_id = data.get('psychologist_id', None)
        history = HistoryModel(
            patient_id=patient_id, psychologist_id=psychologist_id
        )
        db.session.add(history)
        db.session.commit()
        response = history, 200
    else:
        response = 'No se han introducido datos', 401

    res, code = response

    return make_response(
        jsonify({
            'patient_id': res.patient_id,
            'psychologist_id': res.psychologist_id,
            'status': res.status,
            'update_at': res.update_at,
            'create_at': res.create_at
        }), code)
