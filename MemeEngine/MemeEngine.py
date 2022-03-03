"""Module responsible for superimposing quotes onto images.

References:
Lesson 4, Concept 6: Exercise - Pillow:
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/cac8a587-58ea-44d2-927f-0c9badb7a8e9/concepts/5d29ecf9-42d4-4e16-9326-6027682b24a0
Knowledge Solution for Corrupted Font:
https://knowledge.udacity.com/questions/542475
"""
from PIL import Image, ImageDraw, ImageFont
from random import randint
import os


class MemeEngine():
    """Creates memes by placing quotes onto images."""

    def __init__(self, meme_folder: str):
        """Initialize the MemeEngine object.

        param meme_folder: Storage location of finished memes
        """
        self.meme_folder = meme_folder

    def make_meme(self, img_path: str, body: str, author: str,
                  width: int = 500) -> str:
        """Create a memes a meme by superimposing a random quote over \
           a random image.

        param img_path: The file pathway for the input image.
        param body: The quote that will be superimposed on the image.
        param author: The author of the quote, displayed with quote.
        param width: The width of the displayed image.
        Return:
            str: The file pathway for the output image.
        """
        with Image.open(img_path) as image:
            # Resize
            if width is not None:
                ratio = width/float(image.size[0])
                height = int(ratio*float(image.size[1]))
                image = image.resize((width, height), Image.NEAREST)

            if body is not None:
                full_quote = f'{body}\n - {author}'
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype(
                            "./MemeEngine/font/LilitaOne-Regular.ttf",
                            size=22)
                body = draw.text((33, 55), full_quote, font=font,
                                 fill='white', stroke_width=2,
                                 stroke_fill='black')

            # Create a Temporary Random Name to add to finished meme
            trn = f'/{randint(0,1000)}.jpg'
            finished_meme = f'{self.meme_folder}/{trn}'
            image.save(finished_meme)

        return finished_meme
