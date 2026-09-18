# -*- coding: utf-8 -*-

"""
Classe Author
"""

from dataclasses import dataclass, field
from typing import Optional, ClassVar

from .book import Book
from .person import Person


@dataclass
class Author(Person):
    """Auteur d'un ou plusieurs livres sélectionnés pour le prix Goncourt :
    - id_author      : clé primaire de l'entité persistante
    - biography      : biographie de l'auteur (optionnelle)
    - books_written  : livres écrits par l'auteur
    """
    id: Optional[int] = field(default=None, init=False)
    biography: Optional[str] = field(default=None, init=False)
    books_written: list[Book] = field(default_factory=list, init=False)

    def add_book(self, book: Book) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        self.books_written.append(book)
        book.author = self

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}"
