from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {username}"