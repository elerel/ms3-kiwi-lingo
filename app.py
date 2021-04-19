import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_words")
def get_words():
    words = list(mongo.db.words.find())
    return render_template("glossary.html", words=words)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if existing_user:
            flash("Yeah, nah mate. Username already in use.")
            return redirect(url_for("register"))

        if password == confirm_password:

            register = {
                "first_name": request.form.get("first_name"),
                "username": request.form.get("username"),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username")
            flash("Ripper! You've created your profile page!")
            return redirect(url_for("profile", username=session["user"]))
            return render_template("register.html")

        flash("Yeah, nah mate. Passwords do not match.")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if the username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username")
                    flash("Kia Ora, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))    

            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesnt exist
            flash("Username does not exist")
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if request.method == "POST":
        thumbs_up = "on" if request.form.get("thumbs_up") else "off"
        thumbs_down = "on" if request.form.get("thumbs_down") else "off"
        word = {
            "category_name": request.form.get("category_name"),
            "word": request.form.get("word"),
            "definition": request.form.get("definition"),
            "phrase_example": request.form.get("phrase_example"),
            "created_by": session["user"],
            "thumbs_up": thumbs_up,
            "thumbs_down": thumbs_down
        }
        mongo.db.words.insert_one(word)
        flash("Shot for adding your word, mate!")
        return redirect(url_for("get_words"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_word.html", categories=categories)


@app.route("/edit_word/<word_id>", methods=["GET", "POST"])
def edit_word(word_id):
    
    if request.method == "POST":
        thumbs_up = "on" if request.form.get("thumbs_up") else "off"
        thumbs_down = "on" if request.form.get("thumbs_down") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "word": request.form.get("word"),
            "definition": request.form.get("definition"),
            "phrase_example": request.form.get("phrase_example"),
            "created_by": session["user"],
            "thumbs_up": thumbs_up,
            "thumbs_down": thumbs_down
        }
        mongo.db.words.update({"_id": ObjectId(word_id)}, submit)
        flash("Your Word Has Been Updated!")
        return redirect(url_for("get_words"))

    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_word.html", word=word, categories=categories)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)