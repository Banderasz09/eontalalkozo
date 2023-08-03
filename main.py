from flask import Flask

app = Flask(__name__)
file = open('index.html', 'r')

html = file.read()

@app.route("/")
def index():
    return html

app.run(debug=True)
