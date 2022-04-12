from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required
from flask import Flask, request, render_template, redirect, flash, url_for
from App.models import User
from App.database import db
from App.models import signupForm
from App.models import loginForm


''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

''' End Flask Login Functions '''


signUp_views = Blueprint('signUp_views', __name__, template_folder='../templates')


@signUp_views.route('/signup', methods=['GET'])
def signUp_page():
    form = signUp_page() # create form object
    return render_template('signUp.html', form=form) # pass form object to template

@signUp_views.route('/signUp', methods=['POST'])
def signup_submission():
  form = signUp_page() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newuser = User(username=data['username'], email=data['email']) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return redirect(url_for('index'))# redirect to login page
  flash('Error invalid input!')
  return redirect(url_for('signUp'))
