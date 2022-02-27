"""Create and initialize a library of essential modules.

Reference:
Lesson 5, Concept 7: Exercise - Complex Strategy:
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/93decac5-5e75-4573-b28e-ad1218ec04d3/concepts/6733fc76-b1a7-4c42-9a67-622af43b8cd5
"""
from .QuoteModel import QuoteModel

from .Ingestor import Ingestor

from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
