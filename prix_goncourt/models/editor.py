# -*- coding: utf-8 -*-

"""
Classe Author
"""

from dataclasses import dataclass, field
from typing import Optional, ClassVar

from .book import Book
from .person import Person


@dataclass
class Editor:
    """Auteur d'un ou plusieurs livres sélectionnés pour le prix Goncourt :
    - id             : clé primaire de l'entité persistante
    - label          : label de l'éditeur
    """
    id: Optional[int] = field(default=None, init=False)
    label: str
    books_edited: list[Book] = field(default_factory=list, init=False)

    def add_book(self, book: Book) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        self.books_edited.append(book)
        book.editor = self

    def __str__(self) -> str:
        return self.label
