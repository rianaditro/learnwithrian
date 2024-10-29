from flask import Flask, render_template

from data import pythonwebscraping_data as pws

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pythonwebscraping.html', data=pws)

@app.route('/courses/<filepath>')
def open_course(filepath):
    filepath = f'courses/pythonwebscraping/{filepath}'
    return render_template(filepath, slides=pws)



if __name__ == '__main__':
    app.run(debug=True)