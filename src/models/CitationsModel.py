from db.db import db
from models.UsersModel import UsersModel


class CitationsModel(db.Model):
    __tablename__ = 'citations'
    citation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    citation_date = db.Column(db.Date)
    description = db.Column(db.Text)
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())
    psychologist_id = db.Column(db.Integer, db.ForeignKey(
        UsersModel.user_id, ondelete='CASCADE', onupdate='CASCADE'))
    patient_id = db.Column(db.Integer, db.ForeignKey(
        UsersModel.user_id, ondelete='NO ACTION', onupdate='NO ACTION'))

    def __init__(self, citation_date, description, psychologist_id, patient_id):
        self.citation_date = citation_date
        self.description = description
        self.psychologist_id = psychologist_id
        self.patient_id = patient_id
