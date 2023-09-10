from db.db import db

class UsersModel(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    middlename = db.Column(db.String(255))
    first_lastname = db.Column(db.String(255))
    second_lastname = db.Column(db.String(255))
    identification = db.Column(db.Integer)
    age = db.Column(db.Integer)
    telephone = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_type.document_type_id', ondelete='CASCADE', onupdate='CASCADE'))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.rol_id', ondelete='CASCADE', onupdate='CASCADE'))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DATETIME, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    def __init__(self, kwargs):
        self.name = kwargs['name']
        self.middlename = kwargs.get('middlename')
        self.first_lastname = kwargs.get('first_lastname')
        self.second_lastname = kwargs.get('second_lastname')
        self.identification = kwargs.get('identification')
        self.age = kwargs.get('age')
        self.telephone = kwargs.get('telephone')
        self.phone = kwargs.get('phone')
        self.document_type_id = kwargs.get('document_type_id')
        self.rol_id = kwargs.get('rol_id')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
