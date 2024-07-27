from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,FloatField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
print("forms.py loaded successfully") 
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # Add this line
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')
    
    
from wtforms.validators import InputRequired
from wtforms import IntegerField, SelectField
class HeartDiseasePredictionForm(FlaskForm):
    age = IntegerField('Age', validators=[InputRequired()])
    sex = SelectField('Sex', choices=[('0', 'Female'), ('1', 'Male')], validators=[InputRequired()])
    cp = SelectField('Chest Pain Type', choices=[('0', 'Typical Angina'), ('1', 'Atypical Angina'), ('2', 'Non-anginal Pain'), ('3', 'Asymptomatic')], validators=[InputRequired()])
    trestbps = IntegerField('Resting Blood Pressure', validators=[InputRequired()])
    chol = IntegerField('Serum Cholesterol', validators=[InputRequired()])
    fbs = SelectField('Fasting Blood Sugar > 120 mg/dl', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    restecg = SelectField('Resting Electrocardiographic Results', choices=[('0', 'Normal'), ('1', 'ST-T Wave Abnormality'), ('2', 'Left Ventricular Hypertrophy')], validators=[InputRequired()])
    thalach = IntegerField('Max Heart Rate Achieved', validators=[InputRequired()])
    exang = SelectField('Exercise Induced Angina', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    oldpeak = FloatField('ST Depression Induced by Exercise', validators=[InputRequired()])
    slope = SelectField('Slope of the Peak Exercise ST Segment', choices=[('0', 'Upsloping'), ('1', 'Flat'), ('2', 'Downsloping')], validators=[InputRequired()])
    ca = SelectField('Number of Major Vessels Colored by Fluoroscopy', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], validators=[InputRequired()])
    thal = SelectField('Thalassemia', choices=[('0', 'Normal'), ('1', 'Fixed Defect'), ('2', 'Reversible Defect')], validators=[InputRequired()])
    submit = SubmitField('Predict')