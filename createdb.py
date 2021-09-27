from flask_app import db
from app.models.user import User, Role, UserRoles
from app.models.drone import Drone, DroneCameras
from app.models.drone_brand import DroneBrand
from app.models.camera import Camera
from app.models.camera_brand import CameraBrand


if __name__ == "__main__":
    db.create_all()
