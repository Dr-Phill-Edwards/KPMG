from flask import Flask, redirect

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello():
    return redirect('/static/index.html', 301)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
