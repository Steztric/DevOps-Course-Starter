from flask import Flask, render_template, request, redirect, url_for
import trello_items as api
from forms import AddToDoForm, StartDoingForm, MarkDoneForm
from view_model import ViewModel
from item import Status
from datetime import datetime, date

def create_app():
    app = Flask(__name__)

    def set_show_done(view_model: ViewModel):
        show_done = request.args.get('show_done')
        if (show_done != None):
            if show_done == 'True':
                view_model.show_all_done_items = True
            elif show_done == 'False':
                view_model.show_all_done_items = False

    def get_today():
        now = datetime.now()
        return date(now.year, now.month, now.day)

    @app.route('/')
    def index():
        item_view_model = ViewModel(api.get_items())
        set_show_done(item_view_model)
        today = get_today()
        done_items = item_view_model.older_done_items if item_view_model.show_all_done_items else item_view_model.recent_done_items(today)
        return render_template('index.html', view_model=item_view_model, done_items=done_items)

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
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
