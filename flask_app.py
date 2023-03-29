
# A very simple Flask Hello World app for you to get started with...
import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

# Database
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Session

Base = declarative_base()
class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    password = Column(String)
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"

if os.path.exists('cnotes.db'):
    engine = create_engine("sqlite:///cnotes.db", echo=True, future=True)
else:
    engine = create_engine("sqlite:///cnotes.db", echo=True, future=True)
    Base.metadata.create_all(engine)

# Web form
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = MyForm()
    if request.method == 'POST':
        #print(form.name.data, form.password.data)
        with Session(engine) as session:
            user = User(name=form.name.data, password=form.password.data)
            session.add(user)
            session.commit()

    return render_template('form.html', form=form)

#from sqlalchemy import select
#stmt = select(User)
#for user in session.scalars(stmt):
#    print(user)