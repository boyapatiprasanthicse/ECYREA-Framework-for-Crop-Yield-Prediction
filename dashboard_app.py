from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Smart Agriculture Dashboard'

if __name__ == '__main__':
    app.run(debug=True)
