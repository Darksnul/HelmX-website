from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # You can add login logic here
        return redirect(url_for("home"))
    return render_template("login.html")

# Signup Page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # You can add signup logic here
        return redirect(url_for("home"))
    return render_template("signup.html")

# Contact Form (POST Request)
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    # Here you can add code to save the message or send an email
    return "Thank you for contacting HelmX!"

# Run the app with Render-compatible settings
if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 10000)))