from flask import Flask, render_template, request
from wordsearch import search4letters

vayuputhraapp = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('webappsearch.log','a') as log:
        print(req, res, file=log)

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
    with open('webappsearch.log') as log:
        contents = log.read()
        return contents

if __name__ == '__main__':
    vayuputhraapp.run(debug=True)


