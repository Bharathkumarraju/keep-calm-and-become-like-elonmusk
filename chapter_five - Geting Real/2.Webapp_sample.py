from flask import Flask

hanumanapp = Flask(__name__)

@hanumanapp.route('/')
def hello() -> str:
    return "SRI ANJANEYAM"

hanumanapp.run()

