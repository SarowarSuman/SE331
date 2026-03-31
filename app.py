from flask import Flask, request, render_template, redirect
from helper import apology

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("greet.html")

@app.route("/greet")
def greet():
    name = request.args.get("username", "World")
    return render_template("greet.html", name=name)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email:
            return apology(top="No email", bottom="Please provide an email")

        if not password:
            return apology(top="No password", bottom="Please enter a password")

        if len(password) < 8:
            return apology(top="Password length", bottom="Must be at least 8 characters")

        user_email = "test@example.com"
        user_password = "securepassword"

        if email != user_email or password != user_password:
            return apology(top="Invalid credentials", bottom="Please try again")

        return redirect("/home")

    return render_template("login.html")


@app.route("/home")
def homepage():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
