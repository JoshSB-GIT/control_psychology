from db.db import db

class DocumentTypeModel(db.Model):
    __tablename__ = 'document_types'
    document_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    def __init__(self, name, description):
        self.name = name
        self.description = description