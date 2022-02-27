"""Creates a QuoteModel Class."""

class QuoteModel():
    """Creates a class that formats Quotes and Authors for memes."""

    def __init__(self, body, author):
        """Initialize quote model object.

        param body: The quote
        param author: The author of the quote
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a computer-readable string to represent full quotes."""
        return f"{self.body} + ' - ' + {self.author}"
