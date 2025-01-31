from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/illustration')
def illustration():
    return render_template('illustration.html')

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
