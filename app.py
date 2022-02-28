from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Buttons.html')


@app.route('/add')
def add():
    return "Add"


if __name__ == '__main__':
    app.run(debug=True)
