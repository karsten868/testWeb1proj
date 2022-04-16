from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_login import LoginManager, current_user, login_user, login_required
from App.models import LogIn, User


# ''' Begin Flask Login Functions '''
# login_manager = LoginManager()
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# ''' End Flask Login Functions '''


logIn_views = Blueprint('logIn_views', __name__, template_folder='../templates')


# @logIn_views.route('/', methods=['GET'])
# def index():
#   form= LogIn()
#   return render_template('logIn.html', form=form)

@logIn_views.route('/login', methods=['GET'])
def logIn_page():
  form = LogIn()
  return render_template('logIn.html', form=form)

@logIn_views.route('/login', methods=['POST'])
def logIn_submission():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']): # check credentials
        flash('Logged in successfully.') # send message to next page
        login_user(user) # login the user
        return redirect(url_for('homePage')) # redirect to main page if login successful
  flash('Invalid credentials')
  return redirect(url_for('logIn'))