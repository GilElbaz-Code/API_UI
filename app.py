import json
import requests
from flask import Flask, render_template, request
from forms import DeleteForm, AddForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
Bootstrap(app)
headers = {'content-type': 'application/json'}
URL = "http://127.0.0.1:5000/member"


@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm(request.form)
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        facebook = form.facebook.data
        twitter = form.twitter.data
        party = form.twitter.data
        gov_role = form.gov_role.data
        knesset_role = form.knesset_role.data
        additional_role = form.additional_role.data
        personal_phone = form.personal_phone.data
        office_phone = form.office_phone.data
        email = form.email.data
        speaker_name = form.speaker_name.data
        speaker_phone = form.speaker_phone.data
        head_office_name = form.head_office_name.data
        head_office_phone = form.head_office_phone.data
        political_consultant_name = form.political_consultant_name.data
        political_consultant_phone = form.political_consultant_phone.data
        picture = form.picture.data
        position = form.position.data
        payload = {'first_name': first_name, 'last_name': last_name,
                   'facebook': facebook, 'twitter': twitter, 'party': party, 'gov_role': gov_role,
                   'knesset_role': knesset_role, 'additional_role': additional_role,
                   'personal_phone': personal_phone, 'office_phone': office_phone,
                   'email': email, 'speaker_name': speaker_name, 'speaker_phone': speaker_phone,
                   'head_office_name': head_office_name, 'head_office_phone': head_office_phone,
                   'political_consultant_name': political_consultant_name,
                   'political_consultant_phone': political_consultant_phone, 'picture': picture,
                   'position': position}
        requests.post(URL, headers=headers, data=json.dumps(payload))
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
        requests.delete(URL, headers=headers, data=json.dumps(payload))
        return 'Member Deleted'

    return render_template('delete_member.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
