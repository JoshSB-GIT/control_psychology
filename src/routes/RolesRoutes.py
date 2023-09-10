from flask import make_response, jsonify, Blueprint
from flask_cors import cross_origin
from models.RolesModel import RolesModel

roles_bp = Blueprint('roles', __name__)


@cross_origin
@roles_bp.route('/get_roles', methods=['GET'])
def get_roles() -> dict:
    response: tuple = 'Rol no encontrado', 404
    roles = RolesModel.query.all()

    if roles:
        list_roles: list = []
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
        
    res, code = response

    return make_response(jsonify({'data': res}), code)
