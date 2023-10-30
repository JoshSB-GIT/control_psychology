from db.db import db
from models.UsersModel import UsersModel

class VisitsModel(db.Model):
    __tablename__ = 'visits'
    visit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    notes = db.Column(db.Text)
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DATETIME, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    visit_date = db.Column(db.Date)
    psychologist_id = db.Column(db.Integer, db.ForeignKey(UsersModel.user_id, ondelete='CASCADE', onupdate='CASCADE' ))
    patient_id  = db.Column(db.Integer, db.ForeignKey(UsersModel.user_id, ondelete='CASCADE', onupdate='CASCADE'))
    
    def __init__(self, visit_id, notes, status, created_at, updated_at, visit_date, psychologist_id, patient_id):
       self.visit_id = visit_id
       self.notes = notes
       self.status = status
       self.created_at = created_at
       self.updated_at = updated_at
       self.visit_date = visit_date
       self.psychologist_id = psychologist_id
       self.patient_id = patient_id
