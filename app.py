from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    print(f"New contact form: {name} | {email} | {message}")
    return f"Thanks {name}, we received your message!"

from flask import Flask, render_template, request

app = Flask(__name__)

users = {}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return f"Welcome, {username}!"
        else:
            return "Invalid username or password."
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "Username already exists."
        
        users[username] = password
        return f"Signup successful. <a href='/login'>Login here</a>"
    return render_template("signup.html")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)