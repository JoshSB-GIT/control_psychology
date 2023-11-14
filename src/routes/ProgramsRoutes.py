from models.HistoryModel import HistoryModel
from models.UsersModel import UsersModel
from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin
from db.db import db
from models.ProgramsModel import ProgramsModel

programs_dp = Blueprint('programs_dp', __name__)


@cross_origin
@programs_dp.route('/get_programs', methods=['POST'])
def get_programs() -> dict:
    data = request.json
    response: tuple = 'No se encontraron programas', 401
    programs = ProgramsModel.query.filter(ProgramsModel.status == 1).all()

    if programs:
        list_programs: list[dict] = []
        for program in programs:
            response = {
                'program_id': program.program_id,
                'name': program.name,
                'description': program.description,
                'duration': program.duration,
                'status': program.status,
                'update_at': program.update_at,
                'create_at': program.create_at,
            }
            list_programs.append(response)

        response = list_programs, 200

        if data:
            key = list(data.keys())[0]

            if key:
                value = data.get(key, None)
                for prog in list_programs:
                    if prog[key] == value:
                        response = prog, 200
            else:
                response = 'No se encontró el campo', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@programs_dp.route('/add_program', methods=['POST'])
def add_program() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al insertar el programa', 401
    if data:
        name = data.get('name', None)
        description = data.get('description', None)
        duration = data.get('duration', None)

        program = ProgramsModel(
            name=name, description=description, duration=duration
        )
        db.session.add(program)
        db.session.commit()
        response = program, 200
    else:
        response = 'No se han introducido datos', 401

    res, code = response

    return make_response(
        jsonify({
            'name': res.name,
            'description': res.description,
            'duration': res.duration,
            'status': res.status,
            'update_at': res.update_at,
            'create_at': res.create_at
        }), code)


@cross_origin
@programs_dp.route('/delete_program', methods=['PUT'])
def delete_program() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar el programa', 401)

    program_id = data.get('program_id', None)

    if program_id:
        program = ProgramsModel.query.get(program_id)

        if program:
            program.status = 0
            db.session.commit()
            response = 'Programa eliminado correctamente!', 200
        else:
            response = 'No se encontró el programa', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)


programs_dp = Blueprint('programs_dp', __name__)


@cross_origin
@programs_dp.route('/update_program', methods=['PUT'])
def update_program() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar el programa', 401)

    program_id = data.get('program_id', None)
    name = data.get('name', None)
    description = data.get('description', None)
    duration = data.get('duration', None)

    if program_id:
        program = ProgramsModel.query.get(program_id)

        if program:
            program.name = name
            program.description = description
            program.duration = duration

            try:
                db.session.commit()
                response = 'Programa actualizado correctamente!', 200
            except Exception as e:
                response = (f'Ocurrió un error al actualizar: {str(e)}', 500)
        else:
            response = 'No se encontró el programa', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)
