from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/test/<int:pk>/")
def secret_page(pk):
    return f"Well {pk} is a dumb number."


if __name__ == "__main__":
    app.run(debug=True)
