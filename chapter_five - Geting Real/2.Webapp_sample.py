from flask import Flask
import vsearch

hanumanapp = Flask(__name__)

@hanumanapp.route('/')
def hello() -> str:
    return "SRI ANJANEYAM"

@hanumanapp.route('/search')
def do_serch() ->str:
    vsearch.search4letters('Sri Anjaneyam', 'Bhajrang Bhaleu')


hanumanapp.run()

