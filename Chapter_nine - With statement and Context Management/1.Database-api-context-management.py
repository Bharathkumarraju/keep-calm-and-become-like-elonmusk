from flask import Flask, render_template, request, escape
from wordsearch import search4letters
from dbcm import UseDataBase
import mysql.connector

# If your class defines dunder "enter" and dunder "exit" it's a context manager

vayuputhraapp = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {
        'host': '127.0.0.1',
        'user': 'wordsearch',
        'password': 'wordsearchpassword',
        'database': 'wordsearchlogDB'
    }

#    conn = mysql.connector.connect(**dbconfig)
#    cursor = conn.cursor()
    with UseDataBase(dbconfig) as cursor:
        _SQL = """insert into log(phrase, letters, ip, browser_string, results) values(%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL,(
            req.form['phrase'],
            req.form['letters'],
            req.remote_addr,
            req.user_agent.browser,
            res, ))
#    conn.commit()
#    cursor.close()
#    conn.close()

#    with open('webappsearch.log','a') as log:
#        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@vayuputhraapp.route('/search4', methods=['POST'])
def search_do() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
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
def view_the_log() -> str:
    contents=[]
    with open('webappsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Formdata', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents)
if __name__ == '__main__':
    vayuputhraapp.run(debug=True)


