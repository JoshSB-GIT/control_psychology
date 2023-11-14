from functools import wraps
from flask import make_response, jsonify, Blueprint, request
from flask_cors import cross_origin
from models.VisitsModel import VisitsModel
from db.db import db

visits_dp = Blueprint('visits', __name__)

@cross_origin
@visits_dp.route('/get_visits', methods=['POST'])
def get_visits() -> dict:
    data = request.json
    response: tuple = 'No se encontraron visitas', 401
    visits = VisitsModel.query.filter(VisitsModel.status == 1).all()

    if visits:
        list_visit: list[dict] = []
        for visit in visits:
            response = {
                'visit_id':visit.visit_id,
                'notes':visit.notes,
                'status':visit.status,
                'created_at':visit.created_at,
                'updated_at':visit.updated_at,
                'visit_date':visit.visit_date,
                'psychologist_id':visit.psychologist_id,
                'patient_id':visit.patient_id
            }
            list_visit.append(response)
        
        response = list_visit, 200
        
        if data:
            key = list(data.keys())[0]
            
            if key:
                value = data.get(key, None)
                for rol in list_visit:
                    if rol[key] == value:
                        response = rol, 200
            else:
                response = 'No se encontró el campo', 401
        
    res, code = response

    return make_response(jsonify({'data': res}), code)

@cross_origin
@visits_dp.route('/add_visit', methods=['POST'])
def add_visit() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al insertar', 401
    if data:
        visit_id = data.get('visit_id', None)
        notes = data.get('notes', None)
        status = data.get('status', None)
        created_at = data.get('created_at', None)
        updated_at = data.get('updated_at', None)
        visit_date = data.get('visit_date', None)
        psychologist_id = data.get('psychologist_id', None)
        patient_id = data.get('patient_id', None)
        
        user = VisitsModel(
                visit_id=visit_id, notes=notes, status=status, created_at=created_at, updated_at=updated_at, visit_date=visit_date, psychologist_id=psychologist_id, patient_id=patient_id
            )
        db.session.add(user)
        db.session.commit()
        response = user, 200
    else:
        response = 'No se han introducido datos', 401
        
    res, code = response

    return make_response(
        jsonify({
            'visit_id':res.visit_id,
            'notes':res.notes,
            'status':res.status,
            'created_at':res.created_at,
            'updated_at':res.updated_at,
            'visit_date':res.visit_date,
            'psychologist_id':res.psychologist_id,
            'patient_id':res.patient_id
        }), code)

@cross_origin
@visits_dp.route('/delete_visit', methods=['PUT'])
def delete_visit() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar', 401)

    visit_id = data.get('visit_id', None)

    if visit_id:
        visit = VisitsModel.query.get(visit_id)

        if visit:
            visit.status = 0
            db.session.commit()
            response = 'Visita eliminado correctamente!', 200
        else:
            response = 'No se encontró el Visita', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)

@cross_origin
@visits_dp.route('/update_visit', methods=['PUT'])
def update_visit() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar', 401)

    visit_id = data.get('visit_id', None)
    notes = data.get('notes', None)
    created_at = data.get('created_at', None)
    updated_at = data.get('updated_at', None)
    visit_date = data.get('visit_date', None)
    psychologist_id = data.get('psychologist_id', None)
    patient_id = data.get('patient_id', None)

    if visit_id:
        visit = VisitsModel.query.get(visit_id)

        if visit:
            visit.notes = notes
            visit.created_at = created_at
            visit.updated_at = updated_at
            visit.visit_date = visit_date
            visit.psychologist_id = psychologist_id
            visit.patient_id = patient_id

            try:
                db.session.commit()
                response = 'Visita actualizado correctamente!', 200
            except Exception as e:
                response = (f'Ocurrió un error al actualizar: {str(e)}', 500)
        else:
            response = 'No se encontró el Visita', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)