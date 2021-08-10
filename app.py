from flask import Flask, render_template
from routes.register_routes import RegisterRoutes
from routes.logprocess_routes import LogProcessRoutes

app = Flask(__name__)
RegisterRoutes.configure_routes(app)
LogProcessRoutes.configure_routes(app)


@app.route("/")
def index():
    return render_template("index-prueba.html")


@app.route("/product")
def swimmwear():
    return render_template("product.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout-hsv.html")


@app.route("/dashboardadmin")
def dashboardadmin():
    return render_template("dashboardadmin-hsv.html")


@app.route("/dashboardclient")
def dashboardclient():
    return render_template("dashboardclient-hsv.html")


if __name__ == "__main__":
    app.run(debug=True)
