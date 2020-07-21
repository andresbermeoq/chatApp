from flask import Blueprint
from flask import render_template, request, redirect, url_for, abort, flash

from flask_login import login_user,logout_user,login_required, current_user

from .forms import LoginForm, RegisterForm
from .models import User

from . import login_manager

page = Blueprint('page', __name__)

@login_manager.user_loader
def load_user(id):
  return User.get_by_id(id)

@page.route('/')
def index():
  return render_template('index.html', title = 'ChatApp')

@page.route('/logout')
def logout():
    logout_user()
    flash('Sesion Cerrada')
    return redirect(url_for('.login'))

@page.route('/login', methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('.chat_app'))
        
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.get_by_username(form.username.data)
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash('Usuario Registrado Correctamente')
        else:
            flash('Usuario o Password Invalidos', 'error')

    return render_template('auth/login.html', title='Login', form=form, active='login')

@page.route('/register', methods = ['GET','POST'])
def register_user():
  form = RegisterForm(request.form)

  if request.method == 'POST' and form.validate():
      user = User.createElement(form.username.data, form.password.data, form.email.data)
      flash('Usuario Registrado Existosamente')
      login_user(user)
      return redirect(url_for('.chat_app'))

  return render_template('auth/register.html', title = 'Registro', form = form, active = 'register_user')

@page.route('/chat')
@login_required
def chat_app():
  return render_template('chat/chat.html', title = 'Chat', active = 'Chat')
