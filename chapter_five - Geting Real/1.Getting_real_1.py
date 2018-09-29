from flask import Flask

bharathapp = Flask(__name__)

@bharathapp.route('/hanuman')
def hello() -> str:
    return "Jai Bhajrang Bhali"

bharathapp.run()
