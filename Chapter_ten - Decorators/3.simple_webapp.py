"""
We can store browsers specific state in session ,
no matter how many browsers interact with our webapp,
each browsers server side data is managed for us by Flask whenever session is used
"""
from flask import Flask, session
bharathapp = Flask(__name__)

@bharathapp.route('/')
def hello() -> str:
    return "hello from bharaths web"

@bharathapp.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are logged in'

bharathapp.secret_key = 'hanumanchalisa123'

@bharathapp.route('/logout')
def do_logout() -> str:
    session.pop("logged_in")
    return "you are now logged out"


@bharathapp.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in'
    return "You are not logged in"





@bharathapp.route('/page1')
def page1() -> str:
    if 'logged_in' in session:
        return 'This is page1'
    return 'You are not logged in'

@bharathapp.route('/page2')
def page2() -> str:
    if 'logged_in' in session:
        return 'This is Page 2'
    return 'You are not logged in'

@bharathapp.route('/page3')
def page3() -> str:
    if 'logged_in' in session:
        return 'This is page 3'
    return 'You are not logged in'



# Instead of repeating condition in all functions lets write a separate function and call that function

def check_logged_in() -> bool:
    if 'logged_in' in session:
        return True
    return False

@bharathapp.route('/page4')
def page4() -> str:
    if not check_logged_in():
        return 'You are not logged in'
    return 'This is page4'

@bharathapp.route('/page5')
def page5() -> str:
    if not check_logged_in():
        return 'You are not logged in'
    return 'This is page5'

if __name__ == '__main__':
    bharathapp.run(debug=True)