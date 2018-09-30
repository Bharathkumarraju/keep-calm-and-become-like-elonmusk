from flask import Flask
import wordsearch

hanumanapp = Flask(__name__)

@hanumanapp.route('/')
def hello() -> str:
    return "SRI ANJANEYAM"

@hanumanapp.route('/search')
def do_serch() -> str:
    return str(wordsearch.search4letters("Hanuman", "Chaleesaaa"))

@hanumanapp.route('/search4')
def search_do() -> str:
    return str(wordsearch.search4letters('life, the universe, and everything', 'eiru,!'))

hanumanapp.run()

