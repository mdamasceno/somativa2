from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/random')
def random_number():
    number = random.randint(0, 100)
    return render_template('random.html', number=number)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
