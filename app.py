
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#DB configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.app_context().push()

#DB Schema
class Notes(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"{self.Sno} - {self.title}"


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        added_note = Notes(title=title, desc=desc)
        db.session.add(added_note)
        db.session.commit()
    allnotes = Notes.query.all()
    return render_template("index.html", mynotes=allnotes)

@app.route("/delete/<int:SerialNo>")
def delete(SerialNo):
    note = Notes.query.filter_by(Sno = SerialNo).first()
    db.session.delete(note)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:SerialNo>", methods=["POST", "GET"])
def update(SerialNo):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        note = Notes.query.filter_by(Sno = SerialNo).first()
        note.title = title
        note.desc = desc
        db.session.add(note)
        db.session.commit()
        return redirect("/")
    note = Notes.query.filter_by(Sno = SerialNo).first()
    return render_template("update.html", mynote=note)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
