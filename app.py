from flask import Flask, render_template
from flask_restful import Api
from routes.register_routes import RegisterRoutes
from routes.logprocess_routes import LogProcessRoutes

app = Flask(__name__)
api = Api(app)

RegisterRoutes.configure_routes(app)
LogProcessRoutes.configure_routes(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/swimmwear")
def swimmwear():
    return render_template("swimmwear.html")


@app.route("/swimmwear2")
def swimmwear2():
    return render_template("swimmwear2.html")


@app.route("/otros")
def otros():
    return render_template("otros.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/dashboard1")
def dashboardadmin():
    return render_template("dashboard1.html")


@app.route("/dashboard2")
def dashboardclient():
    return render_template("dashboard2.html")


if __name__ == "__main__":
    app.run(debug=True)
