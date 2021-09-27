from flask import Blueprint
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_user import UserManager, login_required
from flask import redirect, render_template, url_for, request
from werkzeug.urls import url_parse


# LOCAL IMPORTS
from flask_app import db, app
from views.forms.users import LoginForm, SignupForm
from models.user import User, Role


login_manager = LoginManager(app)
login_manager.login_view = "users.login"
user_manager = UserManager(app, db, User)


users = Blueprint(
    "users",
    __name__,
    template_folder="../templates/users",
    static_folder="static",
    static_url_path="/login",
)


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@users.route("/nthome", methods=["GET", "POST"])
def not_implemented_home():
    return "<h1>Nacho, don't fforget to set a HOME page.</h1>"


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        user = User.get_by_email(current_user.email)
        user.last_login = db.func.now()
        user.save()
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page) == "":
            next_page = url_for("users.not_implemented_home")
        return redirect(next_page)

    form = LoginForm()
    error = None

    if form.validate_on_submit():
        email = form.email.data
        passw = form.password.data
        remember_login = form.rememberme.data

        user = User.get_by_email(email)

        if (
            user is not None
            and user.deleted == 0
            and user.check_password(passw)
        ):
            login_user(user, remember_login)

            next_page = request.args.get("next")

            if not next_page or url_parse(next_page) == "":
                next_page = url_for("users.not_implemented_home")

            return redirect(next_page)
        else:
            print("Error loging in:")

        error = "Either user or password are incorrect"
    return render_template("login.html", form=form, error=error)


@users.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    error = None

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        pass1 = form.password1.data
        pass2 = form.password2.data
        role = Role.get_by_id(form.role.data)

        user = User.get_by_email(email)

        if user is not None:
            error = f"El email {email} ya está siendo utilizado por \
                otro usuario."
        else:
            if pass1 is not None and pass1 != pass2:
                error = "Las contraseñas no coinciden. Por favor, escríbalas \
                        nuevamente."
            else:
                # create & save the user
                user = User(username=name, email=email)
                user.set_password(pass1)
                user.roles.append(role)
                user.save()
                # Now leave the user logged in
                login_user(user, remember=True)

                next_page = request.args.get("next", None)
                if not next_page or url_parse(next_page).netloc != "":
                    next_page = url_for("users.not_implemented_home")
                return redirect(next_page)

    return render_template("signup.html", form=form, error=error)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("users.login"))
