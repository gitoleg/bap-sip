from subprocess import check_output
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, FieldList, TextField
from wtforms.validators import Required
import bap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class UploadForm(FlaskForm):
    fname = StringField('Path to file', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        session['myfile'] = form.fname.data
        return redirect(url_for('bir', sub='None'))
    return render_template('index.html', form=form)

@app.route('/bir/<sub>')
def bir(sub):
    subs=['sub1','sub2','sub3']
    if sub == 'None':
        return render_template('subs_test.html', subs=subs)
    else:
        print("choosen sub is {}".format(sub))
        return render_template('subs_test.html', subs=subs, sub=sub)

# @app.route('/bir/<sub>')
# def bir(sub):
#     myfile=session['myfile']
#     proj = bap.run(myfile)
#     if sub == 'None':
#         return render_template('subs.html', project=proj)
#     else:
#         return render_template('subs.html', project=proj, sub=sub)

if __name__ == '__main__':
    app.run(debug=True)
