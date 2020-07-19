from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddToDoForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Item')
    
class EditToDoForm(FlaskForm):
    def __init__(self, item, **kw):
        super(EditToDoForm, self).__init__(**kw)
        self.item = item

    id = StringField('Id')
    submit = SubmitField('Mark Done')