from flask_app import db


class DroneBrand(db.Model):
    """ Respresents a Drone's Brand
    """

    __tablename__ = 'drone_brands'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    @staticmethod
    def get_by_id(id):
        return DroneBrand.query.get(id)

    @staticmethod
    def get_all():
        return DroneBrand.query.all()
