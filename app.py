import random
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://api.giphy.com/v1/gifs/search?api_key=1pWzCn1B7t8IvfYRqYMwEZsPk7Q7Ww37&q=funny dog&' \
          'limit=1008&offset=0&rating=g&lang=en'
    reponse = requests.get(url).json()['data']
    content = reponse[random.randint(0, 50)]['images']['downsized_large']['url']
    title = "Hello World, This Is Dog"
    return render_template('doggo.html', title=title, content=content)


if __name__ == '__main__':
    app.run(debug=True)
