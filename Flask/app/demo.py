from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello duniya'

@app.route('/home')
def home():
    return 'ghar mei aa gaye'

@app.route('/error')
def error():
    print 'bad password'
    abort(401)

# do a redirect
@app.route('/login')
def login():
    return redirect(url_for('user', username = 'ansari'))

@app.route('/user/<username>')
def user(username):
    return 'home for ' + str(username)

if __name__ == '__main__':
    app.run(debug = True)
