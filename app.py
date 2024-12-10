import os

from flask import Flask, render_template, render_template_string, request
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

# Configuration
app = Flask(__name__)

# Configure Flask-Mail using environment variables
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))  # Default to 587 if not set
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'  # Convert string to boolean
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# Initialize Flask-Mail
mail = Mail(app)

@app.route("/", methods=["GET"])
def index():
    # Home page route
    return render_template("home.html", title="Home")

@app.route("/about", methods=["GET"])
def about():
    # About Us page route.
    return render_template("about.html", title="About")

@app.route("/contact", methods=["GET"])
def contact():
    # Contact Us page route.
    return render_template("contact.html", title="Contact")

@app.route('/send-email', methods=['POST'])
def send_email():
    # Sample data for the user who signed up
    user_name = request.form['name']  # Get user's name from the form
    user_email = request.form['email']  # Get user's email from the form
    
    # Read the email template from the file
    with open('templates/app_creation_response_email.txt', 'r') as f:
        email_template = f.read()

    # Render the template with dynamic values (name and email)
    email_content = render_template_string(email_template, name=user_name, email=user_email)

    # Create the message
    msg = Message(
        'Thank You for Your Interest in Creating an App with Us',
        recipients=[user_email]
    )
    msg.body = email_content  # Set the email body to the rendered template content

    try:
        # Send the email
        mail.send(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error sending email: {e}'

if __name__ == "__main__":
    # Run app
    app.run()
