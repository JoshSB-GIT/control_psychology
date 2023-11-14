from db.db import db
from models.ProgramsModel import ProgramsModel
from models.UsersModel import UsersModel


class TuitionsModel(db.Model):
    __tablename__ = 'tuitions'
    tuition_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    program_id = db.Column(db.Integer, db.ForeignKey(
        ProgramsModel.program_id))
    user_id = db.Column(db.Integer, db.ForeignKey(
        UsersModel.user_id))
    tuition_date = db.Column(db.Date)
    status = db.Column(db.Integer, default=1)

    def __init__(self, program_id, user_id, tuition_date):
        self.program_id = program_id
        self.user_id = user_id
        self.tuition_date = tuition_date
