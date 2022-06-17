from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("base.html")

@app.route("/charts", methods=['GET', 'POST'])
def charts():
    return render_template("charts.html")

@app.route("/info", methods=['GET', 'POST'])
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True)


#               _
#  quack      >(.)__
#              (___/