# save this as app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return "Hello, World!\n"


if __name__ == "__main__":
    app.run()
