# -*- coding: utf-8 -*-

"""
Classe Author
"""

from dataclasses import dataclass, field
from typing import Optional, ClassVar

from .book import Book
from .person import Person
from .selection import Selection
from .vote import Vote


@dataclass
class JuryMember(Person):
    """Auteur d'un ou plusieurs livres sélectionnés pour le prix Goncourt :
    - id_author      : clé primaire de l'entité persistante
    - biography      : biographie de l'auteur (optionnelle)
    - books_written  : livres écrits par l'auteur
    """
    id_jury_member: Optional[int] = field(default=None, init=False)
    votes: list[Vote] = field(default_factory=list, init=False)

    def vote(self, book: Book, selection: Selection, turn: int) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        vote = Vote(book, self, selection, turn)
        self.votes.append(vote)
        book.author = self

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, membre du jury"
