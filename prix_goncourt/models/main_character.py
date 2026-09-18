# -*- coding: utf-8 -*-

"""
Classe Author
"""

from dataclasses import dataclass, field
from typing import Optional, ClassVar
from xmlrpc.client import DateTime

from .author import Author
from .book import Book
from .editor import Editor
from .selection import Selection


@dataclass
class MainCharacter:
    """Auteur d'un ou plusieurs livres sélectionnés pour le prix Goncourt :
    - id             : clé primaire de l'entité persistante
    - biography      : biographie de l'auteur (optionnelle)
    - books_written  : livres écrits par l'auteur
    """
    id: Optional[int] = field(default=None, init=False)
    name: str
    book: Book

    def __str__(self) -> str:
        return (f"{self.name}, du livre {self.book}")
