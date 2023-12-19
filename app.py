from icecream import ic
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def load_credentials():
    try:
        with open("credentials.json", "r") as file:
            credentials = json.load(file)
    except FileNotFoundError:
        credentials = {}
    return credentials

def save_credentials(credentials):
    with open("credentials.json", "w") as file:
        json.dump(credentials, file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    credentials = load_credentials()

    if username in credentials:
        return "Username already exists. Please choose a different username."
    else:
        credentials[username] = password
        save_credentials(credentials)
        return "Account successfully registered."

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    credentials = load_credentials()

    if username in credentials and credentials[username] == password:
        return "Login successful. Welcome, {}!".format(username)
    else:
        return "Invalid username or password. Please try again."

if __name__ == "__main__":
    app.run(debug=True)
