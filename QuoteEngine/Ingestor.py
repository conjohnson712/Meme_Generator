"""Represents the main library for all pathway-specific quote ingestors."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Encapsulates Concrete Ingestor Classes, Realizes IngestorInterface.

    param ingestors: A list of different accepted Ingestors.
    """

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes according to file pathway type.

        param path: The desired file pathway.
        return: A list of QuoteModels from each Ingestor type.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
