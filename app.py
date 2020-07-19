from flask import Flask, render_template, request, redirect, url_for, Markup
import session_items as session
from forms import AddToDoForm

app = Flask(__name__)
app.config.from_object('flask_config.Config')

def makeTaskLink(id, action, label):
    return f'<a href="/actions/{action}/{id}">{label}</a>'

def startTaskLink(id):
    return Markup(f'<a href="/actions/start/{id}">Start</a>')

def removeTaskLink(id):
    return Markup(f'<a href="/actions/remove/{id}">Remove</a>')

def getActions(id):
    item = session.get_item(id)
    print(item)
    return Markup(makeTaskLink(id, 'start', 'Start'))

@app.route('/')
def index():
    return render_template('index.html', items=session.get_items(), actions=getActions)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddToDoForm()
    if form.validate_on_submit():
        print('Adding To-Do Item: ' + form.description.data)
        session.add_item(form.description.data)
        return redirect('/')
    return render_template('add.html', title='Add Item', form=form)

@app.route('/actions/<action>/<id>', methods=['GET', 'POST'])
def actions(action, id):
    print(f'Start To-Do: {id}')
    return redirect('/')

if __name__ == '__main__':
    app.run()
