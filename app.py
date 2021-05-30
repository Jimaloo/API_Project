from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.run()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userDb.db'

db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50))
    l_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.String(100))


def __init__(self, f_name, l_name, email, message):
    self.f_name = f_name
    self.l_name = l_name
    self.email = email
    self.message = message


db.create_all()


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == "POST":
        user = users(
            f_name = request.form["f_name"],
            l_name = request.form["l_name"],
            email = request.form["email"],
            message = request.form["message"]
        )

        db.session.add(user)
        db.session.commit()
    return render_template('contact.html')
