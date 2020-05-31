from flask import Flask, render_template, request, redirect, url_for
import session_items as session
from forms import AddToDoForm

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', items=session.get_items())

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddToDoForm()
    if form.validate_on_submit():
        print('Adding To-Do Item: ' + form.description.data)
        session.add_item(form.description.data)
        return redirect('/')
    return render_template('add.html', title='Add Item', form=form)

if __name__ == '__main__':
    app.run()
