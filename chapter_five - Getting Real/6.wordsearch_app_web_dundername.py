from flask import Flask, render_template, request
from wordsearch import search4letters

vayuputhraapp = Flask(__name__)

@vayuputhraapp.route('/search4', methods=['POST'])
def search_do() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)
@vayuputhraapp.route('/')
@vayuputhraapp.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search4letters on the web!')

if __name__ == '__main__':
    vayuputhraapp.run(debug=True)