from flask_app import db
from models.user import User, Role, UserRoles


if __name__ == "__main__":
    db.create_all()
