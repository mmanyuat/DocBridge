from flask import current_app as app
from flask import render_template, request, redirect, url_for, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == "POST":
    pass
  return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == "POST":
    pass
  return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():
  return render_template('dashboard.html')


@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('index'))
