"""
We can store browsers specific state in session ,
no matter how many browsers interact with our webapp,
each browsers server side data is managed for us by Flask whenever session is used
"""
from flask import Flask, session
from checker import check_logged_in
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


#@bharathapp.route('/status')
#def check_status() -> str:
#    if 'logged_in' in session:
#        return 'You are currently logged in'
#    return "You are not logged in"

@bharathapp.route('/page1')
@check_logged_in
def page1() -> str:
    return "this is page1"

@bharathapp.route('/page2')
@check_logged_in
def page2() -> str:
    return "this is page2"

@bharathapp.route('/page3')
@check_logged_in
def page3() -> str:
    return "this is page3"


if __name__ == '__main__':
    bharathapp.run(debug=True)