from functools import wraps
from flask import make_response, jsonify, Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import (
    JWTManager, create_access_token, 
    jwt_required, get_jwt_identity, unset_jwt_cookies,
    get_jwt
)
from models.UsersModel import UsersModel
from config.Config import Configuration
from db.db import app

auth_bp = Blueprint('auth', __name__)


# Configura la clave secreta para JWT
app.config['JWT_SECRET_KEY'] = Configuration.SECRET_KEY  # Cambia esto por una clave secreta segura
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Tiempo de expiración del token (1 hora)
BLOCKLIST = set()

# Inicializa el JWTManager
jwt = JWTManager(app)

# Función para autenticar al usuario
def autenticar_usuario(username, password):
    usuario = UsersModel.query.filter_by(username=username, password=password).all()
    print(usuario, type(username))

    if usuario:
        return usuario[0]

    return None

# Función decoradora personalizada para verificar si un token está en la lista negra
def token_in_blacklist(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        jti = get_jwt()['jti']
        if jti in BLOCKLIST:
            return jsonify({'mensaje': 'Token inválido'}), 401
        return fn(*args, **kwargs)
    return wrapped

# Ruta de inicio de sesión
@cross_origin
@auth_bp.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    username: str = datos.get('username')
    password: str = datos.get('password')
    
    usuario = autenticar_usuario(username, password)
    data_token = {
        'user_id': usuario.user_id,
        'rol': usuario.rol_id,
        'name': usuario.name
    }
    if usuario:
        # Crea un token de acceso JWT si la autenticación es exitosa
        token_acceso = create_access_token(identity=usuario.user_id, additional_claims=data_token)
        return make_response(jsonify({'token_acceso': token_acceso}), 200)
    
    return make_response(jsonify({'mensaje': 'Credenciales incorrectas'}), 401)

# Ruta para cerrar sesión
@cross_origin
@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
@token_in_blacklist
def logout():
    jti = get_jwt()["jti"]
    BLOCKLIST.add(jti)
    # unset_jwt_cookies()
    return jsonify({'mensaje': 'Cierre de sesión exitoso'}), 200

# Ruta protegida que requiere autenticación
@auth_bp.route('/ruta_protegida', methods=['GET'])
@jwt_required()
@token_in_blacklist
def ruta_protegida():
    usuario_actual_id = get_jwt_identity()
    return jsonify({'mensaje': 'Esta es una ruta protegida', 'usuario_id': usuario_actual_id})
