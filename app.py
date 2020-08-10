from flask import Flask, render_template, request, redirect, url_for
import trello_items as api
from forms import AddToDoForm, StartDoingForm, MarkDoneForm
from view_model import ViewModel
from item import Status

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    item_view_model = ViewModel(api.get_items())
    return render_template('index.html', view_model=item_view_model)

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
    is_to_do = item.status == Status.to_do
    form = StartDoingForm(item) if is_to_do else MarkDoneForm(item)
    if form.validate_on_submit():
        if is_to_do:
            print('Marked Item Doing: ' + item.title)
            api.mark_doing(id)
        else:
            print('Marked Item Done: ' + item.title)
            api.mark_done(id)
        return redirect('/')
    return render_template('edit.html', title='Edit Item', form=form)

if __name__ == '__main__':
    app.run()
