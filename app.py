from flask import Flask, render_template

from data import COURSES, pws

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/courses/<course_name>/<module_name>')
def pws_1(course_name, module_name):
    filepath = f'courses/{course_name}/{module_name}.html'
    return render_template(filepath)



if __name__ == '__main__':
    app.run(debug=True)