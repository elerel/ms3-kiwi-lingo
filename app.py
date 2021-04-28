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

# Renders home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# Renders Glossary Page
@app.route("/get_words")
def get_words():
    words = list(mongo.db.words.find().sort("word", 1))
    return render_template("glossary.html", words=words)


# Render Search Function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    words = list(mongo.db.words.find({"$text": {"$search": query}}))
    return render_template("glossary.html", words=words)


# Render Sign Up/Register Page
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

        flash("Yeah, nah mate. Passwords do not match.")

    return render_template("register.html")

# Renders Login Page
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
                flash("Kia Ora, {}!".format(
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


# Renders Profile Page
@app.route("/profile/<username>", methods=["GET", "POST"])  
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
        # finds words added by user:
    words = list(mongo.db.words.find())
    # if existing user display profile
    if session["user"]:
        return render_template("profile.html",
                               username=username, words=words)

    return redirect(url_for("login"))


# Render delete profile
@app.route("/delete_profile")
def delete_profile():
    if 'user' not in session:
        return redirect(url_for("login"))
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    mongo.db.users.delete_one({"username": username})
    flash("Your Profile Has Been Deleted. Haere Ra!")
    session.pop("user")
    return render_template("login.html", username=username)


# Renders Logout Page
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out. Haere Ra!")
    session.pop("user")
    return redirect(url_for("login"))


# Renders Add Word Page
@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if request.method == "POST":
        # checks db to find word already added
        existing_word = mongo.db.words.find_one(
            {"word": request.form.get("word")})

        if existing_word:
            # Display flash message if word already exists
            flash("Aw stink owl! That word is already listed.")
            return redirect(url_for("add_word"))

        word = {
            "category_name": request.form.get("category_name"),
            "word": request.form.get("word").capitalize(),
            "definition": request.form.get("definition"),
            "phrase_example": request.form.get("phrase_example"),
            "created_by": session["user"],
            "thumbs_up": 0,
            "thumbs_down": 0
        }
        mongo.db.words.insert_one(word)
        flash("Shot for adding your word, mate!")
        return redirect(url_for("get_words"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_word.html", categories=categories)


# Edit word functionality
@app.route("/edit_word/<word_id>", methods=["GET", "POST"])
def edit_word(word_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "word": request.form.get("word").capitalize(),
            "definition": request.form.get("definition"),
            "phrase_example": request.form.get("phrase_example"),
            "created_by": session["user"],
            "thumbs_up": 0,
            "thumbs_down": 0
        }
        mongo.db.words.update({"_id": ObjectId(word_id)}, submit)
        flash("Your Word Has Been Updated!")
        return redirect(url_for("get_words"))

    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_word.html", word=word, categories=categories)


# Delete Word Function
@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    mongo.db.words.delete_one({"_id": ObjectId(word_id)})
    flash("Word Successfully Deleted")
    return redirect(url_for("get_words"))


# Renders Manage Category Page- for elerel profile
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Add Category functionality- for elerel
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Edit Category Functionality - elerel
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Succesfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete Category Functionality - elerel
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# Render Contact Us Page
@app.route("/contact")
def contact():
    return render_template("contact.html")    


# Likes and Dislikes functionality:
@app.route("/thumbs_up/<word_id>", methods=["GET", "POST"])
def thumbs_up(word_id):
    word = mongo.db.words.find_one_and_update(
        # code credit to W3 Resources: https://www.w3resource.com/mongodb/mongodb-field-update-operator-$inc.php
        {"_id": ObjectId(word_id)}, {"$inc": {"thumbs_up": 1}})
    return redirect(url_for("get_words", word=word))


# Dislike:
@app.route("/thumbs_down/<word_id>", methods=["GET", "POST"])
def thumbs_down(word_id):
    word = mongo.db.words.find_one_and_update(
        # code credit to W3 Resources: https://www.w3resource.com/mongodb/mongodb-field-update-operator-$inc.php
        {"_id": ObjectId(word_id)}, {"$inc": {"thumbs_down": 1}})
    return redirect(url_for("get_words", word=word))


@app.errorhandler(404)
def not_found(error):
    # renders any 404 error'''
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    # render any 500 error'''
    return render_template('errors/500.html'), 500
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
