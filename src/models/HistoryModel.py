from db.db import db
from models.UsersModel import UsersModel


class HistoryModel(db.Model):
    __tablename__ = 'history'
    history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey(
        UsersModel.user_id))
    psychologist_id = db.Column(db.Integer, db.ForeignKey(
        UsersModel.user_id))
    status = db.Column(db.Integer, default=1)
    update_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())
    create_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, patient_id, psychologist_id):
        self.patient_id = patient_id
        self.psychologist_id = psychologist_id
