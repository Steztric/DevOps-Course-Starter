from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from item import ToDoItem, Status

class AddToDoForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Item')
    
class StartDoingForm(FlaskForm):
    def __init__(self, item: ToDoItem, **kw):
        super(StartDoingForm, self).__init__(**kw)
        self.item = item

    id = StringField('Id')
    submit = SubmitField('Start Doing')
    
class MarkDoneForm(FlaskForm):
    def __init__(self, item: ToDoItem, **kw):
        super(MarkDoneForm, self).__init__(**kw)
        self.item = item

    id = StringField('Id')
    submit = SubmitField('Mark Done')