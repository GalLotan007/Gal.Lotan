from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/redirect-catalogs')
def redirect_catalogs():
    return redirect('/catalogs')


@app.route('/redirect-items')
def redirect_items():
    return redirect(url_for('get_items'))


@app.route('/catalogs')
def get_catalogs():
    return 'Catalogs Page'


@app.route('/items')
def get_items():
    return 'Items Page'


if __name__ == '__main__':
    app.run()
