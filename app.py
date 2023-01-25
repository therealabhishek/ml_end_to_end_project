from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    logging.info("We are testing logging module.")
    return "ML End to End project!!"


if __name__ == "__main__":
    app.run(debug=True)
