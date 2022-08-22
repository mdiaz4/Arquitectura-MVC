from flask import render_template, redirect
from past.builtins import raw_input
from app import app
from model import Person
import view
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
        """Return Template index"""
        return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
        """"Return Template Person"""
        return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
        """Return data of person and template person.
           The data is: id_person, name and last_name
        """
        id_person = request.form['id_person']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        p = Person(id_person=id_person, name=first_name, last_name=last_name)
        model.append(p)
        return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
        """Return data of person and template people.
           The data is: id_person, name and last_name
           
        """
        data = [(i.id_person, i.name, i.last_name) for i in model]
        print(data)
        return render_template('people.html', value=data)


@app.route("/person_update/<id>")
def update_person(id):
        """"Return template person_update"""
        return render_template("person_update.html", value=id)


@app.route("/person_detail_update", methods=["POST"])
def persona_detail_update():
        """Return template person_detail
           and data of the person updated.
        """
        id_person = request.form['static_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        for i in model:
            if i.id_person == id_person:
                model.remove(i)
                p = Person(id_person=id_person, name=first_name, last_name=last_name)
                model.append(p)
        """Delete de name and last_name old
           and add the new data of the person
           selected.
           Depending on id.
        """
                    
        return render_template ('person_detail.html', value=("Update Person: "+ "(" + p.id_person +" - "+ p.name + " - "+ p.last_name + ")"))


@app.route("/person_delete/<id>")
def delete_person(id):
        """Return the id_person , name and last_name
           of a person deleted.
        """
        for i in model:
            if i.id_person == id:
                temp = i
                model.remove(i)
        """Delete data of a person selected.
           Depending on id.
        """
        return render_template ('person_detail.html', value=("Persona Eliminada: "+ "(" + temp.id_person +" - "+temp.name + " - "+ temp.last_name + ")"))
        

if __name__ == '__main__':
    app.run()