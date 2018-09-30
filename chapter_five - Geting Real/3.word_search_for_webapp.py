from flask import Flask, render_template, request
import wordsearch


vayuputhraapp = Flask(__name__)

@vayuputhraapp.route('/')
def hello():
    return "Jai hanuman 123"

@vayuputhraapp.route('/search4', methods=['POST'])
def search_do() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(wordsearch.search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)
@vayuputhraapp.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search4letters on the web!')

vayuputhraapp.run(debug=True)