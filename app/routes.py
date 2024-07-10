from flask import render_template,flash,redirect,url_for
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={'username' : 'ibrahim' }
    posts=[
        {
            'author':{'username': 'hamid'},
            'post' :'nhar zwin frabat o chmicha'
            },
        {
            'author':{'username': 'hamid'},
            'post' :'casa fiha chta mablanch'
            }
    ]
        
    return render_template('index.html' ,title='Home',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'login request for {form.username.data} remeber me = {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)