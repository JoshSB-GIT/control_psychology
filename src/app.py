from flask import make_response, jsonify
from flask_cors import CORS, cross_origin
from routes.RolesRoutes import roles_bp
from routes.AuthRoutes import auth_bp
from routes.UsersRoutes import users_dp
from routes.CitationsRoutes import citations_dp
from routes.VisitsRoutes import visits_dp
from db.db import app, db

app.register_blueprint(roles_bp, url_prefix='/roles')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(users_dp, url_prefix='/users')
app.register_blueprint(citations_dp, url_prefix='/citations')
app.register_blueprint(visits_dp, url_prefix='/visits')

CORS(app)

@cross_origin
@app.route('/')
def home() -> dict:
    return make_response(jsonify({'home': 'Hello word!'}), 200)

if __name__ == '__main__':
    app.run(debug=True)
