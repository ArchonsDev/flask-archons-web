from flask import Flask, render_template

# Configuration
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Home page route
    return render_template("index.html", title="Home")

@app.route("/about", methods=["GET"])
def about():
    # About Us page route.
    return render_template("about.html", title="About")

@app.route("/contact", methods=["GET"])
def contact():
    # Contact Us page route.
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    # Run app
    app.rune()
