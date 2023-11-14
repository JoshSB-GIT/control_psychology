from db.db import db


class ProgramsModel(db.Model):
    __tablename__ = 'programs'
    program_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)
    status = db.Column(db.Integer, default=1)
    update_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())
    create_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, name, description, duration):
        self.name = name
        self.description = description
        self.duration = duration
