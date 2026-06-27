from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


# BASIC ROUTES

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"


@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"


@app.route("/number/<int:number>")
def show_number(number):
    return f"<h2>Your contact number is {number}</h2>"


@app.route("/home")
def home():
    images = get_images()
    return render_template("home.html", images=images)


@app.route("/bye")
def bye():
    return "<p>Bye, Flask!</p>"

# UPLOAD SETUP
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "upload")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_images():
    return os.listdir(app.config["UPLOAD_FOLDER"])


# UPLOAD ROUTES (GALLERY)

@app.route("/upload", methods=["POST"])
def upload_file():
    files = request.files.getlist("file")

    for file in files:
        if file and file.filename != "" and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    return redirect(url_for("home"))


@app.route("/upload/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# RUN APP

if __name__ == "__main__":
    app.run(debug=True)