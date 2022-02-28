"""Creates a web-based application to generate memes.

Reference:
Lesson 6, Concept 5: Exercise - Saving with Requests
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/b727b572-3590-43d3-bd66-699da5bf1cf6/concepts/96a16de1-5229-48bb-b405-00202717b378
Lesson 6, Concept 7: Exercise - Flask App
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/b727b572-3590-43d3-bd66-699da5bf1cf6/concepts/3ccf344d-171f-4487-b7aa-f1f7c6b91ca0
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from .QuoteEngine import Ingestor, QuoteModel
from .MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme.

    param img: A randomized image from images.
    param quote: A randomized quote from quotes.
    param path: Gathers the materials to make a meme.
    return: A rendered template containing the contents of path.
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    param image_url: Request the url of the image file.
    param quote_body: Request the body of the quote.
    param quote_author: Request the author of the quote.
    """
    image_url = request.form.get('image_url')
    quote_body = request.form.get('body')
    quote_author = request.form.get('author')

    r = requests.get(image_url)
    tmp_meme = f'./tmp_{random.randint(0, 100000)}.jpg'
    open(tmp_meme, 'wb').write(r.content)

    path = meme.make_meme(tmp_meme, quote_body, quote_author)
    print(tmp_meme)

    os.remove(tmp_meme)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
