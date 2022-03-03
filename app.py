import json

import requests
from flask import Flask, render_template, request
from forms import DeleteForm, AddForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
Bootstrap(app)


@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm(request.form)
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        # TODO Continue form parse and add also on API
        return 'Member Added'
    return render_template('add_member.html', form=form)


@app.route('/update', methods=['GET', 'POST'])
def update():
    pass


@app.route('/patch', methods=['GET', 'POST'])
def patch():
    pass


@app.route('/upload_csv', methods=['GET', 'POST'])
def upload_csv():
    pass


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteForm(request.form)
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        payload = {"first_name": first_name, "last_name": last_name}
        headers = {'content-type': 'application/json'}
        url = "http://127.0.0.1:5000/member"
        requests.delete(url, headers=headers, data=json.dumps(payload))
        return 'Member Deleted'

    return render_template('delete_member.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
