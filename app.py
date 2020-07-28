import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://dog.ceo/api/breeds/image/random'
    reponse = requests.get(url).json()
    content = reponse['message']
    title = "Hello World, This Is Dog"
    return render_template('doggo.html', title=title, content=content)


if __name__ == '__main__':
    app.run(debug=True)
