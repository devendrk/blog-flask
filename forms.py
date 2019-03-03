from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from models import Jobs



class SearchForm(FlaskForm):
    search = StringField('The word you want', validators=[DataRequired()])
    exclude = SubmitField('What to exclude', validators=[DataRequired()])
    submit = SubmitField('Seach Jobs')

    # fetches data from our model / database on submit
    def FetchData(Jobs):
        if submit:
            Jobs.query.filter_by(Jobs.data)
            return redirect('/results')
        return render_template(results.html)
