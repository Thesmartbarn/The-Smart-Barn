from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "hello"


if __name__ == "__main__":
    print("")
    app.run()