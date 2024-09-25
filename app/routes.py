from flask import current_app as app
from flask import render_template, request, redirect, url_for, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Appointment


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
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Add more validation as needed
        
        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please log in instead.', 'error')
            return redirect(url_for('login'))

        # Create a new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)  # Assuming you have a method to hash passwords
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!')

        # Redirect to the booked appointments page after registration
        return redirect(url_for('show_appointments'))  # Adjust the route name if needed

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
@app.route('/appointments')
def show_appointments():
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

# Example of route to create a new appointment
@app.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        patient_id = request.form.get('patient_id')
        doctor_id = request.form.get('doctor_id')
        appointment_date = request.form.get('appointment_date')

        new_appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, appointment_date=appointment_date)
        db.session.add(new_appointment)
        db.session.commit()

        flash('Appointment booked successfully!')
        return redirect(url_for('show_appointments'))

    return render_template('book_appointment.html')