from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.ext.hybrid import hybrid_property
from services import db, bcrypt

##Barrett -> Table Models 

class Set(db.Model, SerializerMixin):
    __tablename__ = "Sets"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    user = db.relationship('User', backpopulates='Sets')

class Workout(db.Model, SerializerMixin):
    __tablename__ = "Workouts"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    attributes = db.Column(db.String, nullable=False)

class Set_Workout(db.Model, SerializerMixin):
    __tablename__ = "Set_Workouts"
    id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer, db.ForeignKey('Sets.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('Workouts.id'))

    set = db.relationship('Set', backpopulates='Set_Workouts')
    workout = db.relationship('Workout', backpopulates='Set_Workouts')


class User(db.Model, SerializerMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)

    @hybrid_property
    def password(self):
        return self._password_hash
    
        # Now we create a setter function!
    @password.setter
    def password(self, password):
        #NOTE WE NEED THE ENCODE AND DECODE IN PYTHON 3 DUE TO SPECIAL CHARACTERS ∫
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    # Now lets create an authentification route using
    # bcrypt.check_password_hash(_password_hash, password.encode('utf-8'))
    def authenticate(self,password):
        return bcrypt.check_password_hash(self._password_hash,password.encode('utf-8'))