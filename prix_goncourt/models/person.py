# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Author et JuryMember
"""

from abc import ABC
from dataclasses import dataclass, field
from typing import ClassVar

from .address import Address


@dataclass
class Person(ABC):
    """Personne liée au prix Goncourt : auteur ou membre du jury."""
    id_person: int = field(default=None, init=False)
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
