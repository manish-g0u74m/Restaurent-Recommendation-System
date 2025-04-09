from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

class SuggestionForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    locality = StringField('Locality', validators=[DataRequired()])
    cuisine = SelectField('Cuisine', choices=[
        ('Indian', 'Indian'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Mexican', 'Mexican')
    ], validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    comment = TextAreaField('Comments')
    submit = SubmitField('Submit Suggestion')