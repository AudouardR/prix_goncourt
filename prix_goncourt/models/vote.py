# -*- coding: utf-8 -*-

"""
Classe Author
"""

from dataclasses import dataclass, field
from typing import Optional, ClassVar, List

from .book import Book
from .jury_member import JuryMember
from .president import President
from .selection import Selection


@dataclass
class Vote:
    """Auteur d'un ou plusieurs livres sélectionnés pour le prix Goncourt :
    - id             : clé primaire de l'entité persistante
    - label          : label de l'éditeur
    """
    _votes: List["Vote"] = field(default_factory=list, init=False)
    book: Book
    jury_member: JuryMember
    selection: Selection
    turn: int

    def count_votes(self, book: Book, selection: Selection) -> int:
        count = 0
        for vote in Vote.get_all():
            if vote.book == book and vote.selection == selection:
                count += 1
                # Le vote compte double pour le président du jury
                if isinstance(vote.jury_member, President):
                    count += 1
        return count

    @classmethod
    def get_all(cls) -> List["Vote"]:
        """Return a list of all Vote instances."""
        return cls._votes.copy()  # Return a copy to prevent external modification

    def __str__(self) -> str:
        return f"(Sélection {self.selection.selection_nbr}, tour {self.turn})"
