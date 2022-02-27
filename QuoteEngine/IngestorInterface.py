from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel
"""Represents an interface to parse different data types."""


"""References:
Lesson 3: Concept 6:
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/02d7c0d9-c741-424f-99f6-cd914cca1f63/concepts/c9e520e8-7039-4f6a-8973-5e26b8ef67a1

Lesson 3: Concept 8:
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/02d7c0d9-c741-424f-99f6-cd914cca1f63/concepts/77ae24a0-a78d-436a-8f48-589d7ca0b771

Lesson 5, Concept 7:
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/93decac5-5e75-4573-b28e-ad1218ec04d3/concepts/6733fc76-b1a7-4c42-9a67-622af43b8cd5
"""


class IngestorInterface(ABC):
    """Creates an AbstractBaseClass to ingest various file pathways.

    param allowed_extensions: A list of file extensions.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check if a class can be ingested and parsed.

        param path: The path for the file extension.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest an extension pathway and return a list of QuoteModels."""
        pass
