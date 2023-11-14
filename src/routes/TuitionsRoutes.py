from flask import make_response, jsonify, Blueprint, request
from flask_cors import cross_origin
from db.db import db
from models.TuitionsModel import TuitionsModel

tuitions_dp = Blueprint('tuitions', __name__)


@cross_origin
@tuitions_dp.route('/get_tuitions', methods=['POST'])
def get_tuitions() -> dict:
    data = request.json
    response: tuple = 'No se encontraron matrículas', 401
    tuitions = TuitionsModel.query.filter(TuitionsModel.status == 1).all()

    if tuitions:
        list_tuition: list[dict] = []
        for tuition in tuitions:
            response = {
                'tuition_id': tuition.tuition_id,
                'program_id': tuition.program_id,
                'user_id': tuition.user_id,
                # Formatear la fecha si es necesario
                'tuition_date': tuition.tuition_date.strftime('%Y-%m-%d'),
                'status': tuition.status,
            }
            list_tuition.append(response)

        response = list_tuition, 200

        if data:
            key = list(data.keys())[0]

            if key:
                value = data.get(key, None)
                for t in list_tuition:
                    if t[key] == value:
                        response = t, 200
            else:
                response = 'No se encontró el campo', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@tuitions_dp.route('/add_tuition', methods=['POST'])
def add_tuition() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al insertar la matrícula', 401
    if data:
        program_id = data.get('program_id', None)
        user_id = data.get('user_id', None)
        tuition_date = data.get('tuition_date', None)

        if program_id and user_id and tuition_date:
            tuition = TuitionsModel(
                program_id=program_id, user_id=user_id, tuition_date=tuition_date
            )
            db.session.add(tuition)
            db.session.commit()
            response = tuition, 200
        else:
            response = 'Faltan datos obligatorios', 401
    else:
        response = 'No se han introducido datos', 401

    res, code = response

    return make_response(
        jsonify({
            'tuition_id': res.tuition_id,
            'program_id': res.program_id,
            'user_id': res.user_id,
            # Formatear la fecha si es necesario
            'tuition_date': res.tuition_date.strftime('%Y-%m-%d'),
            'status': res.status,
            'update_at': res.update_at,
            'create_at': res.create_at
        }), code)


@cross_origin
@tuitions_dp.route('/delete_tuition', methods=['PUT'])
def delete_tuition() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar', 401)

    tuition_id = data.get('tuition_id', None)

    if tuition_id:
        tuition = TuitionsModel.query.get(tuition_id)

        if tuition:
            tuition.status = 0
            db.session.commit()
            response = 'Matrícula eliminada correctamente!', 200
        else:
            response = 'No se encontró la matrícula', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@tuitions_dp.route('/update_tuition', methods=['PUT'])
def update_tuition() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar la matrícula', 401)

    tuition_id = data.get('tuition_id', None)
    program_id = data.get('program_id', None)
    user_id = data.get('user_id', None)
    tuition_date = data.get('tuition_date', None)

    if tuition_id:
        tuition = TuitionsModel.query.get(tuition_id)

        if tuition:
            tuition.program_id = program_id
            tuition.user_id = user_id
            tuition.tuition_date = tuition_date

            try:
                db.session.commit()
                response = 'Matrícula actualizada correctamente!', 200
            except Exception as e:
                response = (f'Ocurrió un error al actualizar: {str(e)}', 500)
        else:
            response = 'No se encontró la matrícula', 401

    res, code = response

    return make_response(
        jsonify({
            'tuition_id': res.tuition_id,
            'program_id': res.program_id,
            'user_id': res.user_id,
            'tuition_date': res.tuition_date,
            'status': res.status
        }), code)
