

from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_speak', methods=['POST'])
def run_speak():
    subprocess.Popen(['python', 'speak.py'])
    return redirect(url_for('index'))

@app.route('/run_main', methods=['POST'])
def run_main():
    subprocess.Popen(['python', 'main.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
