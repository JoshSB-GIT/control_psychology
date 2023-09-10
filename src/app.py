from flask import make_response, jsonify
from flask_cors import CORS, cross_origin
from routes.RolesRoutes import roles_bp
from routes.AuthRoutes import auth_bp
from db.db import app, db

app.register_blueprint(roles_bp, url_prefix='/roles')
app.register_blueprint(auth_bp, url_prefix='/auth')
CORS(app)

@cross_origin
@app.route('/')
def home() -> dict:
    return make_response(jsonify({'home': 'Hello word!'}), 200)

if __name__ == '__main__':
    app.run(debug=True)
