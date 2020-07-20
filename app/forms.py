from wtforms import Form, HiddenField
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField


from .models import User

def codigo_validator(form, field):
  if field.data == 'Codi'


class LoginForm(Form):
  username = StringField('Username', [
    validators.length(min=4, max=50, message = 'El Username se encuentra fuera de Rango')
  ])

  password = PasswordField('Password', [
    validators.Required(message = 'El Password es Requerido')
  ])

class RegisterForm(Form):
  username = StringField('Username', [
    validators.length(min=4, max=50)
  ])

  email = EmailField('Email', [
    validators.length(min = 6, max = 100),
    validators.Required(message = 'El Email es requerido.'),
    validators.Email(message = 'Ingrese un Email Valido')
  ])

  password = PasswordField('Password', [
    validators.Required(message = 'El Password es Requerido'),
    validators.EqualTo('confirm_password', message = 'El Password no coincide')
  ])

  confirm_password = PasswordField('Confirm Password')

  
