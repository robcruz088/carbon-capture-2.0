from flask import Flask, render_template, make_response
from time import time

app = Flask(__name__)

@app.route()
def main():
    return

@app.route('/data', methods=["GET","POST"])
def data():
    return


if __name__ == "__main__":
    app.run(debug=True)



