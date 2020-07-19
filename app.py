from flask import Flask, render_template, request, redirect, url_for
import trello_items as api
from forms import AddToDoForm, EditToDoForm

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', items=api.get_items())

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddToDoForm()
    if form.validate_on_submit():
        print('Adding To-Do Item: ' + form.description.data)
        api.add_item(form.description.data)
        return redirect('/')
    return render_template('add.html', title='Add Item', form=form)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    item = api.get_item(id)
    print(item.status)
    form = EditToDoForm(item)
    if form.validate_on_submit():
        print('Mark Item Done: ' + item.title)
        api.mark_done(id)
        return redirect('/')
    return render_template('edit.html', title='Edit Item', form=form)

if __name__ == '__main__':
    app.run()
