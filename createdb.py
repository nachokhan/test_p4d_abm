from flask_app import db
from models.user import User, Role, UserRoles
from models.drone import Drone, DroneCameras
from models.drone_brand import DroneBrand
from models.camera import Camera
from models.camera_brand import CameraBrand


if __name__ == "__main__":
    db.create_all()
