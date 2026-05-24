from flask import Flask, render_template, request, redirect, url_for, session
from database.db import *
app = Flask(__name__)
app.secret_key = "clave secreta"

create_tables()

@app.route("/")
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    products = get_all_products()
    return render_template("index.html", products=products)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_user_by_username(username)
        if user and user[2] == password:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/add", methods=["GET", "POST"])
def add():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        quantity = request.form["quantity"]
        category_id = request.form["category_id"]
        add_product(name, price, quantity, category_id)
        return redirect(url_for("index"))
    else: 
        categories = get_all_categories()
        return render_template("add.html", categories=categories)

@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session:
        return redirect(url_for("login"))
    delete_product(id)
    return redirect(url_for("index"))

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        quantity = request.form["quantity"]
        category_id = request.form["category_id"]
        update_product(id, name, price, quantity, category_id)
        return redirect(url_for("index"))
    else: 
        categories = get_all_categories()
        product = get_product_by_id(id)
        return render_template("update.html", product=product, categories=categories)
    
@app.route("/search")
def search():
    term = request.args.get("term")
    products = search_products(term)
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)