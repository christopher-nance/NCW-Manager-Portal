"""
Routes and views for the flask application.
"""

from datetime import datetime
import flask
from flask import render_template, session, request, redirect, url_for
from NCW_Manager_Portal import app
import msal

app = flask(__name__)
app.secret_key = "my_secret_key"

# Configure MSAL settings
CLIENT_ID = "e732516b-f803-473a-bb61-bcd394488ee1"
CLIENT_SECRET = "_Xv8Q~bsNq0hGydp3QUJJMSLuK~GTukZ3HGHJc-j"
AUTHORITY = "https://login.microsoftonline.com/16abb6e6-23e2-421c-8afd-0e7a19ce0fe0"
REDIRECT_URI = "https://manager-portal-rg.azurewebsites.net/callback"
SCOPE = ["User.Read"]

# Create a new MSAL client
msal_client = msal.ConfidentialClientApplication(CLIENT_ID, client_credential=CLIENT_SECRET, authority=AUTHORITY)

# Define the login route
@app.route("/login")
def login():
    # Redirect the user to the Azure AD login page
    auth_url = msal_client.get_authorization_request_url(SCOPE, redirect_uri=REDIRECT_URI)
    return redirect(auth_url)

# Define the callback route
@app.route("/callback")
def callback():
    # Handle the authentication response from Azure AD
    if "code" in request.args:
        result = msal_client.acquire_token_by_authorization_code(request.args["code"], SCOPE, redirect_uri=REDIRECT_URI)
        if "access_token" in result:
            session["access_token"] = result["access_token"]
            return redirect(url_for("home"))
    return "Authentication failed."


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    if "access_token" not in session:
        return redirect(url_for("login"))
    # Use the access token to verify the user's identity and authorize access to protected resources
    headers = {"Authorization": "Bearer " + session["access_token"]}
    response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
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
        message='Please complete the form below and press Submit Request to submit paperwork to HR for approval.'
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

@app.route('/DamageClaims')
def DamageClaims():
    """Renders the about page."""
    return render_template(
        'DamageClaims.html',
        title='Damage Claims',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/DowntimeLogger')
def DowntimeLogger():
    """Renders the about page."""
    return render_template(
        'DowntimeLogger.html',
        title='Downtime Logger',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/TicketSubmitter')
def TicketSubmitter():
    """Renders the about page."""
    return render_template(
        'TicketSubmitter.html',
        title='Ticket Submitter',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    """Catches any errors and returns error page."""
    return render_template(
        'missingPage.html',
        errorCode=404,
        message='The page you requested does not exists. Please make sure you are trying to access an existing resource or contact your IT administrator for more information.'
    )
