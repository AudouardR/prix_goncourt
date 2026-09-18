# -*- coding: utf-8 -*-

"""
Classe Author
"""

from dataclasses import dataclass, field
from typing import Optional, ClassVar
from xmlrpc.client import DateTime

from .author import Author
from .editor import Editor
from .main_character import MainCharacter
from .selection import Selection


@dataclass
class Book:
    """Auteur d'un ou plusieurs livres sélectionnés pour le prix Goncourt :
    - id             : clé primaire de l'entité persistante
    - biography      : biographie de l'auteur (optionnelle)
    - books_written  : livres écrits par l'auteur
    """
    isbn: str
    title: str
    price: float
    publishing_date: DateTime
    nb_pages: int
    author: Author
    editor: Editor
    summary: Optional[str] = field(default=None)
    editor_price: Optional[float] = field(default=None)
    main_characters: list[MainCharacter] = field(default_factory=list, init=False)
    selections: list[Selection] = field(default_factory=list, init=False)

    def add_main_character(self, main_character: MainCharacter) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        self.main_characters.append(main_character)
        main_character.book = self

    def add_to_selection(self, selection: Selection) -> None:
        self.selections.append(selection)
        selection.books_selected.append(self)

    def __str__(self) -> str:
        return (f"{self.title}, écrit par {self.author.first_name} {self.author.last_name}, "
                f"publié par {self.editor} le {self.publishing_date}"
                f"Prix : {self.price}, {self.nb_pages} pages")
