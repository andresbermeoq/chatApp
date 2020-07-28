from time import localtime, strftime
from flask import Blueprint
from flask import render_template, request, redirect, url_for, abort, flash, session
from flask_socketio import SocketIO, send, join_room, leave_room
from flask_login import login_user,logout_user,login_required, current_user

from .forms import LoginForm, RegisterForm
from .models import User

from . import login_manager, socketio

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
    return redirect(url_for('.index'))

@page.route('/login', methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('.chat_app'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.get_by_username(form.username.data)
        if user and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('.chat_app'))
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
  users = User.query.all()
  ROOMS = ["Publico", "Programacion"]
  return render_template('chat/chat.html', title = 'Chat', users = users,
                                           active = 'Chat', rooms = ROOMS)

clients = []

@socketio.on('message')
def message(data):

  print('Received Message: ' + str(data))
  send({'msg': data['msg'], 'username': data['username'],
        'time_stamp': strftime('%b-%d %I:%M%p', localtime())},
        room = data['room'])

@socketio.on('connect', namespace='/chat')
def connect():
    clients.append(request.namespace)

@socketio.on('disconnect', namespace='/chat')
def user_disconnect():
    print(strftime("%Y-%m-%d %H:%M:%S") + ' - Client disconnected.')
    clients.remove(request.namespace)

@socketio.on('join')
def join(data):
  room = data['room']
  join_room(room)
  send({'msg': data['username'] + " Ha Entrado a " + data['room']},
      room = data['room'])

@socketio.on('leave')
def leave(data):
  room = data['room']
  leave_room(room)
  send({'msg': data['username'] + "Estas Saliendo de " + data['room']},
      room = data['room'])
  clients.remove(data['username'])


