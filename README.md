# Archons.dev Webapp

This is a Flask application for the official Archons.dev website.

## Getting Started
Follow the steps below to set up and run the application:

## Prerequisites:
- Python 3.7 or higher
- pip (Python package manager)

## Setup Instructions:
1. Create a Virtual Environment:
   It is recommended to use a virtual environment to manage your project dependencies. Run the following commands:

   ### Create a virtual environment named .venv
   ```
   python -m venv .venv
   ```
   
   ### Activate the virtual environment
   ```
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install Dependencies:
   Once the virtual environment is activated, install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Application:
   With the dependencies installed, you can start the Flask development server:
   ```
   flask run
   ```

   This will start the application, and it will be accessible at:

   http://127.0.0.1:5000

## Project Structure:
```
project/
│
├── app/                # Your Flask application code
│   ├── __init__.py     # Flask application factory
│   ├── routes.py       # Application routes
│   └── templates/      # HTML templates
│
├── requirements.txt    # List of project dependencies
├── README.txt          # This file
└── run.py              # Entry point to run the app
```
## Additional Notes:
- To deactivate the virtual environment, simply run:
  ```
  deactivate
  ```

- Use `.venv` as the directory for your virtual environment to ensure consistency.

## Contributions:
Feel free to fork the repository, open issues, or submit pull requests to improve the project.

Happy coding! 🎉
