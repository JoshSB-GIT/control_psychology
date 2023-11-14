from flask import make_response, jsonify, Blueprint, request
from flask_cors import cross_origin
from models.RolesModel import RolesModel
from db.db import db

roles_bp = Blueprint('roles', __name__)


@cross_origin
@roles_bp.route('/get_roles', methods=['POST'])
def get_roles() -> dict:
    data = request.json
    response: tuple = 'No se encontraron roles', 401
    roles = RolesModel.query.filter(RolesModel.status == 1).all()
    print(data)

    if roles:
        list_roles: list[dict] = []
        for rol in roles:
            response = {
                'rol_id': rol.rol_id,
                'name': rol.name,
                'description': rol.description,
                'status': rol.status,
                'created_at': rol.created_at,
                'updated_at': rol.updated_at
            }
            list_roles.append(response)
        
        response = list_roles, 200
        
        if data:
            key = list(data.keys())[0]
            
            if key:
                value = data.get(key, None)
                for rol in list_roles:
                    if rol[key] == value:
                        response = rol, 200
            else:
                response = 'No se encontró el campo', 401
        
    res, code = response

    return make_response(jsonify({'data': res}), code)

@cross_origin
@roles_bp.route('/add_roles', methods=['POST'])
def add_roles() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al insertar', 401
    if data:
        name = data.get('name', None)
        description = data.get('description', None)
        if name:
            print(name, description)
            rol = RolesModel(name, description)
            db.session.add(rol)
            db.session.commit()
            response = rol, 200
        else:
            response = 'No se han introducido datos', 401
        
    res, code = response

    return make_response(
        jsonify({'name': str(res.name),
                 'description': str(res.description)
                }), code)

@cross_origin
@roles_bp.route('/delete_rol', methods=['PUT'])
def delete_rol() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al actualizar', 401
    rol_id = data.get('rol_id', None)
    if rol_id:
        rol = RolesModel.query.filter(RolesModel.rol_id == rol_id).first()
        if rol:
            rol.status = 0
            db.session.commit()
            response = 'Rol eliminado correctamente!', 200
        else:
            response = 'No se encontró el rol', 401
        
    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@roles_bp.route('/update_rol', methods=['PUT'])
def update_rol() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al actualizar', 400
    rol_id = data.get('rol_id', None)
    name = data.get('name', None)
    description = data.get('description', None)
    print(data)
    if name and description:
        rol = RolesModel.query.filter(RolesModel.rol_id == rol_id).first()
        if rol:
            rol.name = name
            rol.description = description
            db.session.commit()
            response = 'Rol actualizado correctamente!', 200
        else:
            response = 'No se encontró el rol', 400
        
    res, code = response
    print(f'{res}')

    return make_response(jsonify({'data': res}), code)