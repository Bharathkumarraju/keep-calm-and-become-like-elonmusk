from flask import Flask, render_template, request, escape, session
from wordsearch import search4letters
from dbcm import UseDataBase, ConnectionError
from time import sleep


# If your class defines dunder "enter" and dunder "exit" it's a context manager

vayuputhraapp = Flask(__name__)

vayuputhraapp.config['dbconfig'] = {
    'host': '127.0.0.1',
    'user': 'wordsearch',
    'password': 'wordsearchpassword123',
    'database': 'wordsearchlogDB' }

@vayuputhraapp.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'
@vayuputhraapp.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now loggedout'

def log_request(req: 'flask_request', res: str) -> None:
    """Log details of web requests and results"""
#    sleep(15)
#    raise Exception("Something awfull just happened")
    with UseDataBase(vayuputhraapp.config['dbconfig']) as cursor:
        _SQL = """insert into log(phrase, letters, ip, browser_string, results) values(%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL,(
            req.form['phrase'],
            req.form['letters'],
            req.remote_addr,
            req.user_agent.browser,
            res))

@vayuputhraapp.route('/search4', methods=['POST'])
def search_do() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print('***** Logging failed with the error', str(err))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)
@vayuputhraapp.route('/')
@vayuputhraapp.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search4letters on the web!')

@vayuputhraapp.route('/viewlog')
def view_the_log() -> 'html':
   try:
       with UseDataBase(vayuputhraapp.config['dbconfig']) as cursor:
          _SQL1 = """select phrase, letters, ip, browser_string, results from log"""
          cursor.execute(_SQL1)
          contents = cursor.fetchall()
       titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
       return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents)
   except ConnectionError as err:
       print("Is you database is switched on? Error:", str(err))
   except Exception as err:
       print("Soemthing went wrong", str(err))
   return 'Error'
vayuputhraapp.secret_key = 'Srianjaneyamprasannaanjaneyam'

if __name__ == '__main__':
    vayuputhraapp.run(debug=True)


