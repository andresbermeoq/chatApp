from wtforms import Form, HiddenField
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField


from .models import User

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError("Solo los Humanos pueden registrarse")


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

  accept = BooleanField('', [
    validators.DataRequired()
  ])

  honeypot = HiddenField("", [length_honeypot])

  def validate_username(self, username):
    if User.get_by_username(username.data):
      raise validators.ValidationError("El Username ya se encuentra Registrado")

  def validate_email(self, email):
    if User.get_by_email(email.data):
      raise validators.ValidationError('El Correo ya se encuentra Registrado')

  def validate(self):
    if not Form.validate(self):
      return False

    if len(self.password.data) < 3:
      self.password.errors.append('El Password no es valido')
      return False
      
    return True


