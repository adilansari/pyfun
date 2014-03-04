from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    print 'bad password'
    abort(401)

# do a login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # temporary dictionary to store various logins
    logins = {'apple': 'apple1234', 'mango': 'mango1234','coach': 'carter'}
    error = None
    if request.method == 'POST':
        usr = request.form['username']
        if not usr in logins:
            error = "Username not found"
        elif request.form['password'] != logins[usr]:
            error = "invalid password. Please try again!"
        else:
            return redirect(url_for('user', username = usr))
    return render_template('login.html', error = error)

@app.route('/user/<username>')
def user(username):
    return 'home for ' + str(username)

if __name__ == '__main__':
    app.run(debug = True)
