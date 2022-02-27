"""Represents an Ingestor specified for .txt files.

References:
Lesson 4, Concept 8: Exercise - Strategy Objects
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/cac8a587-58ea-44d2-927f-0c9badb7a8e9/concepts/8e2fb5c6-33ef-4b5b-a01d-8f422a88fa1b
Lesson 5, Concept 7: Exercise - Complex Strategy:
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/93decac5-5e75-4573-b28e-ad1218ec04d3/concepts/6733fc76-b1a7-4c42-9a67-622af43b8cd5
"""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Create an Concrete Class Object for parsing txt file pathways.

    param allowed_extensions: File pathway allowed in this ingestor.
    """
    
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest txt File, return list of quotes.

        param path {str}: txt file pathway, origin of quotes.
        return: Quotes stored in txt file.
        """
        if not cls.can_ingest(path):
            raise Exception('TXT-Only Diet, Cannot Ingest!')

        quotes = []
        with open(path, 'r') as infile:
            for line in infile.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    meme_text = QuoteModel(parse[0], parse[1])
                    quotes.append(meme_text)

            infile.close()
            return quotes
