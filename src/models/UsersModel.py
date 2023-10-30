from db.db import db
from models.DocumentTypeModel import DocumentTypeModel

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
    document_type_id = db.Column(db.Integer, db.ForeignKey(DocumentTypeModel.document_type_id, ondelete='CASCADE', onupdate='CASCADE' ))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.rol_id', ondelete='CASCADE', onupdate='CASCADE'))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DATETIME, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    def __init__(self, name, middlename, first_lastname, second_lastname,
             identification, age, telephone, phone,
             document_type_id, rol_id, username, password):
        self.name = name
        self.middlename = middlename
        self.first_lastname = first_lastname
        self.second_lastname = second_lastname
        self.identification = identification
        self.age = age
        self.telephone = telephone
        self.phone = phone
        self.document_type_id = document_type_id
        self.rol_id = rol_id
        self.username = username
        self.password = password
