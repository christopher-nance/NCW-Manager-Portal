"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from NCW_Manager_Portal import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/NewHirePaperwork')
def NewHirePaperwork():
    """Renders the about page."""
    return render_template(
        'NewHirePaperwork.html',
        title='New Hire Paperwork',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/IncidentReport')
def IncidentReport():
    """Renders the about page."""
    return render_template(
        'IncidentReport.html',
        title='Incident Report',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/EmployeeTermination')
def EmployeeTermination():
    """Renders the about page."""
    return render_template(
        'EmployeeTermination.html',
        title='Employee Termination',
        year=datetime.now().year,
        message='Your application description page.'
    )
