from flask_app import db


class Camera(db.Model):
    """ Respresents a Camera
    """

    __tablename__ = 'cameras'
    id = db.Column(db.Integer(), primary_key=True)
    model = db.Column(db.String(50), nullable=False, unique=False)
    megapixel = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('camera_brands.id'))

    brand = db.relationship('CameraBrand')

    def __repr__(self):
        return f'{self.brand.name} {self.model} ({self.megapixel}MP)'

    @staticmethod
    def get_by_id(id):
        return Camera.query.get(id)

    @staticmethod
    def get_all():
        return Camera.query.all()
