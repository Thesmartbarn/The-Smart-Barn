from flask import Flask, jsonify
from flask_cors import CORS 

class API:
    def __init__(self, __name__) -> None:
        self.API = Flask(__name__)
        self.__name__ = __name__
        CORS(self.API, resources={r"/*": {"origins": "*"}})
        
    def main(self, func):
        @self.API.route("/", methods=["GET"])
        def index():
            return func()
        if self.__name__ == "__main__":
            self.API.run(host="0.0.0.0")