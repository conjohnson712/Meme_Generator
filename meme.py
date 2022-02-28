"""File responsible for generating a meme via CLI.

Reference:
Lesson 5, Concept 4: Exercise - Argparser:
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/93decac5-5e75-4573-b28e-ad1218ec04d3/concepts/aec5a0a6-45ac-4138-a6f5-f83ae270869e
"""

import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote.

    param path: The file pathway of the quote.
    param body: The quote text.
    param author: The author of the quote.
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('No Anonymous Quotes, Author Required.')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    """Use ArgumentParser to parse CLI arguments.

    param path: path to an image file
    param body: quote body to add to the image
    param author: quote author to add to the image
    Return: A generated meme
    """
    parser = argparse.ArgumentParse(description="Meme Generator")
    parser.add_argument('--path', type=str, default=None,
                        help="The written origin of the quote.")
    parser.add_argument('--body', type=str, default=None,
                        help="The wisdom of our canine friends")
    parser.add_argument('--author', type=str, default=None,
                        help="The canine friend who bestowed the wisdow")

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
