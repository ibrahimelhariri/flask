from flask import render_template
from app import app

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

