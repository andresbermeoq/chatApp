from flask import Blueprint
from flask import render_template, request, redirect, url_for, abort, flash

from flask_login import login_user, logout_user, login_required, current_user

from .forms import LoginForm
from .models import User

from . import login_manager

page = Blueprint('page', __name__)


@page.route('/')
def index():
  return render_template('index.html', title = 'ChatApp')

@page.route('/login', methods = ['GET','POST'])
def login_user():

  form = LoginForm(request.form)

  if request.method == 'POST' and form.validate():
    user = User.get_by_username(form.username.data)
    if user and user.verify_password(form.password.data):
      login_user(user)
      flash('Usuario Registrado Correctamente')
    else:
      flash('Usuario o Password Invalidos', 'error')

  return render_template('auth/login.html', title = 'Registro', form = form, active = 'login_user')

@page.route('/register', methods = ['GET','POST'])
def register_user():
  
