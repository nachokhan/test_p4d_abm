from flask_app import db


class CameraBrand(db.Model):
    """ Respresents a Camera's Brand
    """

    __tablename__ = 'camera_brands'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    @staticmethod
    def get_by_id(id):
        return CameraBrand.query.get(id)

    @staticmethod
    def get_all():
        return CameraBrand.query.all()
