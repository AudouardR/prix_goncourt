# -*- coding: utf-8 -*-

"""
Classe Author
"""

from dataclasses import dataclass, field
from typing import Optional, ClassVar
from xmlrpc.client import DateTime

from .book import Book
from .person import Person
from .president import President


@dataclass
class Selection:
    """Auteur d'un ou plusieurs livres sélectionnés pour le prix Goncourt :
    - id             : clé primaire de l'entité persistante
    - label          : label de l'éditeur
    """
    selection_nbr: int
    selection_date: DateTime
    president: President
    books_selected: list[Book] = field(default_factory=list, init=False)

    def select_book(self, book: Book) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        self.books_selected.append(book)
        book.selections.append(self)

    def __str__(self) -> str:
        display = f"Sélection {self.selection_nbr}, début : {self.selection_date}"
        if self.books_selected:
            display = display+" : \n"
            for book in self.books_selected:
                display += f"- {book} \n"
        return display
