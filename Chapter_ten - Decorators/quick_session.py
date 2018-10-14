from flask import Flask,session

hanumanapp = Flask(__name__)
hanumanapp.secret_key = 'hanuamanisgreat123'


@hanumanapp.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@hanumanapp.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

if __name__ == '__main__':
    hanumanapp.run(debug=True)
