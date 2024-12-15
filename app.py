"""1.Основний роут для направлення на тури
   2.Зробити роут для фільтрації за направлення
   3.Написати шаблони
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tours")
def tours():
    return render_template("tours.html")


@app.route("/tours-from-Kiev")
def tours_from_Kiev():
    return render_template("tours_from_Kiev.html")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
