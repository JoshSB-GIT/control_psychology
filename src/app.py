from flask import Flask, make_response, jsonify
from flask_cors import CORS, cross_origin
from config.Config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy


configuration = DevelopmentConfig()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{configuration.MYSQL_USER}@{configuration.MYSQL_HOST}/flaskmysql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db = SQLAlchemy(app)


@cross_origin
@app.route('/')
def home() -> dict:
    response: dict = {}
    from controllers.Roles import RolesController
    rol = RolesController()
    roles, code = rol.get_roles()

    if code != 404:
        response = roles
    
    return make_response(jsonify({'data': response}), code)


if __name__ == '__main__':
    app.run(debug=True)
