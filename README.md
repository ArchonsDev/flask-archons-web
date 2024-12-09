<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App Starter Guide</title>
</head>
<body>
    <h1>Flask App Starter Guide</h1>
    <p>This is a Flask application designed to help you get started quickly with a minimal setup.</p>

    <hr>

    <h2>Getting Started</h2>
    <p>Follow the steps below to set up and run the application:</p>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.7 or higher</li>
        <li><code>pip</code> (Python package manager)</li>
    </ul>

    <hr>

    <h2>Setup Instructions</h2>

    <h3>1. Create a Virtual Environment</h3>
    <p>It is recommended to use a virtual environment to manage your project dependencies. Run the following commands:</p>
    <pre>
        <code>
# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
        </code>
    </pre>

    <h3>2. Install Dependencies</h3>
    <p>Once the virtual environment is activated, install the required dependencies:</p>
    <pre>
        <code>pip install -r requirements.txt</code>
    </pre>

    <h3>3. Run the Application</h3>
    <p>With the dependencies installed, you can start the Flask development server:</p>
    <pre>
        <code>flask run</code>
    </pre>
    <p>This will start the application, and it will be accessible at:</p>
    <pre>
        <code>http://127.0.0.1:5000</code>
    </pre>

    <hr>

    <h2>Project Structure</h2>
    <pre>
        <code>
project/
│
├── app/                # Your Flask application code
│   ├── __init__.py     # Flask application factory
│   ├── routes.py       # Application routes
│   └── templates/      # HTML templates
│
├── requirements.txt    # List of project dependencies
├── README.html         # This file
└── run.py              # Entry point to run the app
        </code>
    </pre>

    <hr>

    <h2>Additional Notes</h2>
    <ul>
        <li>To deactivate the virtual environment, simply run:</li>
    </ul>
    <pre>
        <code>deactivate</code>
    </pre>
    <p>Use <code>.venv</code> as the directory for your virtual environment to ensure consistency.</p>

    <hr>

    <h3>Contributions</h3>
    <p>Feel free to fork the repository, open issues, or submit pull requests to improve the project.</p>

    <p>Happy coding! 🎉</p>
</body>
</html>
