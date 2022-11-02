
# A very simple Flask Hello World app for you to get started with...
import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = MyForm()
    if request.method == 'POST':
        print(form.name.data, form.password.data)
    return render_template('form.html', form=form)

