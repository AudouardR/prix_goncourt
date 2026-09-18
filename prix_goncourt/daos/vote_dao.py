# -*- coding: utf-8 -*-

"""
Classe Dao[Vote]
"""
from models.book import Book
from models.jury_member import JuryMember
from models.selection import Selection
from models.vote import Vote
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class VoteDao(Dao[Vote]):
    def create(self, vote: Vote) -> Optional[str]:
        """Crée en BD l'entité Vote correspondant au vote Vote

                :param vote: à créer sous forme d'entité Vote en BD
                :return: l'isbn du livre correspondant au vote (None si la création a échoué)
                """
        if self.read_vote(vote.book, vote.jury_member, vote.selection) is None:

            with Dao.connection.cursor() as cursor:
                # Ajouter le vote dans la table Vote
                sql = "INSERT INTO vote(isbn, id_jury_member, selection_nbr) VALUES (%s)"
                cursor.execute(sql, (vote.book.isbn, vote.jury_member.id_jury_member,
                                     vote.selection.selection_nbr,))

            Dao.connection.commit()

            # Si le vote a été créé, retourner son identifiant
            return vote.book.isbn

        # Si la création a échoué, retourner 0
        return None

    def read(self, useless_number: int) -> str:
        return f"""
                Mauvaise méthode, désolé... ^^' \n
                À cause de la classe mère Dao, la méthode read() de VoteDao est limitée à un argument, 
                or il y a besoin de 3 arguments (livre, membre du jury, sélection) pour trouver un vote, 
                le vote n'a pas d'id.
                Veuillez utiliser la méthode read_vote(self, book, jury_member, selection) pour lire un vote. \n
                Argument donné : {useless_number}
            """

    @staticmethod
    def read_vote(book: Book, jury_member: JuryMember, selection: Selection) -> Optional[Vote]:
        """Renvoie le vote du membre du jury jury_member pour le livre book dans la sélection selection
           (ou None si elle n'a pu être trouvée)"""

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM vote WHERE isbn=%s AND id_jury_member=%s AND selection_nbr=%s"
            cursor.execute(sql, (book.isbn, jury_member.id_jury_member, selection.selection_nbr,))
            record = cursor.fetchone()

        if record is not None:
            vote = Vote(
                record['isbn'],
                record['id_jury_member'],
                record['selection_nbr'],
                record['turn']
            )
            return vote

        return None

    def update(self, vote: Vote) -> bool:
        """Met à jour en BD l'entité Vote correspondant à vote, pour y correspondre

        :param vote: éditeur déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM vote WHERE isbn=%s AND id_jury_member=%s AND selection_nbr=%s"
            cursor.execute(sql, (vote.book.isbn, vote.jury_member.id_jury_member,
                                     vote.selection.selection_nbr,))
            record = cursor.fetchone()
            if record is not None:
                sql = "UPDATE vote SET turn=%s WHERE isbn=%s AND id_jury_member=%s AND selection_nbr=%s"
                cursor.execute(sql, (vote.turn, vote.book.isbn, vote.jury_member.id_jury_member,
                                     vote.selection.selection_nbr,))
                Dao.connection.commit()

        return self.read_vote(vote.book, vote.jury_member, vote.selection) == vote


    def delete(self, vote: Vote) -> bool:
        """Supprime en BD l'entité Vote correspondant à vote

        :param vote: éditeur dont l'entité Vote correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            # Supprimer le vote de la table Vote
            sql = "DELETE FROM vote WHERE isbn=%s AND id_jury_member=%s AND selection_nbr=%s"
            cursor.execute(sql, (vote.book.isbn, vote.jury_member.id_jury_member,
                                     vote.selection.selection_nbr,))

        Dao.connection.commit()

        return self.read_vote(vote.book, vote.jury_member, vote.selection) is None