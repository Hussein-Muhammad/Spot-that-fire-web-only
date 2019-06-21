from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route('/new')
def new():
    return render_template('new.html')
@app.route('/settings')
def settings():
    return render_template('settings.html')
@app.route('/burning_tips')
def burning_tips():
    return render_template('burning_tips.html')
@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)