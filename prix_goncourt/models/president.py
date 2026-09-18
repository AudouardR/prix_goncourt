# -*- coding: utf-8 -*-

"""
Classe Author
"""

from dataclasses import dataclass, field
from typing import Optional, ClassVar

from .book import Book
from .jury_member import JuryMember
from .selection import Selection


@dataclass
class President(JuryMember):
    """Auteur d'un ou plusieurs livres sélectionnés pour le prix Goncourt :
    - id_author      : clé primaire de l'entité persistante
    - biography      : biographie de l'auteur (optionnelle)
    - books_written  : livres écrits par l'auteur
    """
    id: Optional[int] = field(default=None, init=False)

    def add_book_to_selection(self, selection: Selection, book: Book) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        selection.books_selected.append(book)
        book.selections.append(selection)

    def __str__(self) -> str:
        jury_member_str = super().__str__()
        return f"{jury_member_str}, président"
