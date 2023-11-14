from functools import wraps
from flask import make_response, jsonify, Blueprint, request
from flask_cors import cross_origin
from models.UsersModel import UsersModel
from db.db import db

users_dp = Blueprint('users', __name__)

@cross_origin
@users_dp.route('/get_users', methods=['POST'])
def get_users() -> dict:
    data = request.json
    response: tuple = 'No se encontraron usuarios', 401
    users = UsersModel.query.filter(UsersModel.status == 1).all()

    if users:
        list_user: list[dict] = []
        for user in users:
            response = {
                'user_id': user.user_id,
                'name': user.name,
                'middlename': user.middlename,
                'first_lastname': user.first_lastname,
                'second_lastname': user.second_lastname,
                'identification': user.identification,
                'age': user.age,
                'telephone': user.telephone,
                'phone': user.phone,
                'document_type_id': user.document_type_id,
                'rol_id': user.rol_id,
                'username': user.username,
                'password': user.password,
            }
            list_user.append(response)
        
        response = list_user, 200
        
        if data:
            key = list(data.keys())[0]
            aux_list = []
            if key:
                value = data.get(key, None)
                for rol in list_user:
                    if rol[key] == value:
                        aux_list.append(rol)
                response = aux_list, 200
            else:
                response = 'No se encontró el campo', 401
        
    res, code = response

    return make_response(jsonify({'data': res}), code)

@cross_origin
@users_dp.route('/add_user', methods=['POST'])
def add_user() -> dict:
    data = request.json
    response: tuple = 'Ocurrió un error al insertar', 401
    if data:
        name = data.get('name', None)
        middlename = data.get('middlename', None)
        first_lastname = data.get('first_lastname', None)
        second_lastname = data.get('second_lastname', None)
        identification = data.get('identification', None)
        age = data.get('age', None)
        telephone = data.get('telephone', None)
        phone = data.get('phone', None)
        document_type_id = data.get('document_type_id', None)
        rol_id = data.get('rol_id', None)
        username = data.get('username', None)
        password = data.get('password', None)
        user = UsersModel(
                name=name, middlename=middlename, first_lastname=first_lastname,
                second_lastname=second_lastname, identification=identification,
                age=age, telephone=telephone, phone=phone,
                document_type_id=document_type_id, rol_id=rol_id,
                username=username, password=password
            )
        db.session.add(user)
        db.session.commit()
        response = user, 200
    else:
        response = 'No se han introducido datos', 401
        
    res, code = response

    return make_response(
        jsonify({
            'name': res.name,
            'middlename': res.middlename,
            'first_lastname': res.first_lastname,
            'second_lastname': res.second_lastname,
            'identification': res.identification,
            'age': res.age,
            'telephone': res.telephone,
            'phone': res.phone,
            'document_type_id': res.document_type_id,
            'rol_id': res.rol_id,
            'username': res.username,
            'password': res.password
        }), code)

@cross_origin
@users_dp.route('/delete_user', methods=['PUT'])
def delete_user() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar', 401)

    user_id = data.get('user_id', None)

    if user_id:
        user = UsersModel.query.get(user_id)

        if user:
            user.status = 0
            db.session.commit()
            response = 'Usuario eliminado correctamente!', 200
        else:
            response = 'No se encontró el usuario', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)


@cross_origin
@users_dp.route('/update_user', methods=['PUT'])
def update_user() -> dict:
    data = request.json
    response = ('Ocurrió un error al actualizar', 401)

    user_id = data.get('user_id', None)
    name = data.get('name', None)
    middlename = data.get('middlename', None)
    first_lastname = data.get('first_lastname', None)
    second_lastname = data.get('second_lastname', None)
    identification = data.get('identification', None)
    age = data.get('age', None)
    telephone = data.get('telephone', None)
    phone = data.get('phone', None)
    document_type_id = data.get('document_type_id', None)
    rol_id = data.get('rol_id', None)
    username = data.get('username', None)
    password = data.get('password', None)

    if user_id:
        user = UsersModel.query.get(user_id)

        if user:
            user.name = name
            user.middlename = middlename
            user.first_lastname = first_lastname
            user.second_lastname = second_lastname
            user.identification = identification
            user.age = age
            user.telephone = telephone
            user.phone = phone
            user.document_type_id = document_type_id
            user.rol_id = rol_id
            user.username = username
            user.password = password

            try:
                db.session.commit()
                response = 'Usuario actualizado correctamente!', 200
            except Exception as e:
                response = (f'Ocurrió un error al actualizar: {str(e)}', 500)
        else:
            response = 'No se encontró el usuario', 401

    res, code = response

    return make_response(jsonify({'data': res}), code)