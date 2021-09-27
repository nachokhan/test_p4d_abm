from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length, Email

from app.models.user import Role


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired("Mandatory field"), Email()]
    )
    password = PasswordField(
        "Password", validators=[DataRequired("Mandatory field")]
    )
    rememberme = BooleanField("Remember Me")
    submit = SubmitField("Login")


class SignupForm(FlaskForm):

    Roles = [
        (0, "ADMINISTRADOR"),
        (1, "COMERCIAL"),
        (2, "CLIENTE"),
    ]

    choices = [(e.id, e.name) for e in Role.get_all()]

    name = StringField(
        "Username",
        validators=[DataRequired("Mandatory field"), Length(max=64)],
    )
    password1 = PasswordField(
        "Password",
        validators=[DataRequired("Mandatory field")],
    )
    password2 = PasswordField(
        "Repeat Password",
        validators=[DataRequired("Mandatory field")],
    )
    email = StringField(
        "Email", validators=[DataRequired("Mandatory field"), Email()]
    )
    role = SelectField(
        "Role",
        choices=choices,
        validators=[DataRequired("Mandatory field")],
    )
    submit = SubmitField("Signup")
