from flask_app import db


class Drone(db.Model):
    """ Represents a Drone
    """

    __tablename__ = 'drones'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    serial_number = db.Column(db.String(20), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('drone_brands.id'))

    brand = db.relationship('DroneBrand')
    cameras = db.relationship('Camera', secondary='drone_cameras')

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Drone.query.get(id)

    @staticmethod
    def get_all():
        return Drone.query.all(id)


class DroneCameras(db.Model):
    """ Represents a camera supported by a drone
        (Many2Many relationship)
    """

    __tablename__ = 'drone_cameras'
    id = db.Column(db.Integer(), primary_key=True)
    drone_id = db.Column(db.Integer(), db.ForeignKey('drones.id', ondelete='CASCADE'))
    camera_id = db.Column(db.Integer(), db.ForeignKey('cameras.id', ondelete='CASCADE'))
