from flask import Flask
import random

app = Flask(__name__)

win_number = random.randint(1, 9)


@app.route("/")
def home():
    return """<h1 style='color:blue'>Hello there. Guess a number between 1 and 9</h1>
                <p>Input it in the url after ' / '</p>
                <img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif'>
            """


@app.route("/<int:pk>")
def guess(pk):
    if pk == win_number:
        return """
            <h1 style='color:green'>You got it, you rock</h1>
            <img src='https://media.giphy.com/media/nXxOjZrbnbRxS/giphy.gif'>
        """
    if pk < win_number:
        return """
            <h1 style='color:red'>You are too low, try again</h1>
            <img src='https://media.giphy.com/media/jqI7vrTgA1An4pi4k8/giphy.gif'>
        """
    else:
        return """
            <h1 style='color:purple'>You are too high, try again</h1>
            <img src='https://media.giphy.com/media/F89PG9XV8sofbaXV4D/giphy.gif'>
        """


if __name__ == "__main__":
    app.run(debug=True)
