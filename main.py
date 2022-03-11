from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return ''


@app.route('/training/<string:prof>')
def index(prof):
    if 'строитель' in prof.lower() or 'инженер' in prof.lower():
        return render_template('index2.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')