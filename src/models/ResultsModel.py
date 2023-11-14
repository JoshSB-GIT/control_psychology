from db.db import db
from models.CitationsModel import CitationsModel


class ResultsModel(db.Model):
    __tablename__ = 'results'
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey(
        CitationsModel.citation_id))
    rating = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    status = db.Column(db.Integer, default=1)
    create_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())
    update_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    def __init__(self, appointment_id, rating, feedback):
        self.appointment_id = appointment_id
        self.rating = rating
        self.feedback = feedback
