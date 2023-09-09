from app import db

class RolesModel(db.Model):
    __tablename__ = 'roles'
    rol_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DATETIME, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    def __init__(self, kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
