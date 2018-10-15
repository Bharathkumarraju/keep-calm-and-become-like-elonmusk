from flask import Flask

anjaneya_app = Flask(__name__)

@anjaneya_app.route("/")
def srianjaneyam() -> str:
    return 'SRI ANJANEYAM PRASANNA ANJANEYAM PABHA DIVYA KAAYAM PRAKEERTHI PRADHAAYAM'

if __name__ == '__main__':
    anjaneya_app.run(debug=True)
