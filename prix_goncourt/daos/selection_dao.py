# -*- coding: utf-8 -*-

"""
Classe Dao[Selection]
"""
from daos.book_dao import BookDao
from daos.main_character_dao import MainCharacterDao
from models import president
from models.author import Author
from models.book import Book
from models.president import President
from models.selection import Selection
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.editor import Editor


@dataclass
class SelectionDao(Dao[Selection]):
    def create(self, selection: Selection) -> int:
        """Crée en BD l'entité Selection correspondant à la sélection Selection

                :param selection: à créer sous forme d'entité Selection en BD
                :return: le numéro de l'entité insérée en BD (0 si la création a échoué)
                """
        if self.read(selection.selection_nbr) is None:

            with Dao.connection.cursor() as cursor:
                # Ajouter la sélection dans la table Selection
                sql = "INSERT INTO selection(selection_nbr, selection_date, id_president) VALUES (%s, %s, %s)"
                cursor.execute(sql, (selection.selection_nbr, selection.selection_date, selection.president.id))

                # Ajouter les livres sélectionnés dans la table SelectionBook
                for book_selected in selection.books_selected:
                    # Vérifier s'ils sont déjà dans la table
                    sql = "SELECT * FROM selection_book WHERE selection_nbr = %s AND isbn = %s"
                    cursor.execute(sql, (selection.selection_nbr, book_selected.isbn))
                    record = cursor.fetchone()
                    #Insérer les livres dans la table
                    if record is None:
                        sql = "INSERT INTO selection_book(selection_nbr, isbn) VALUES (%s, %s)"
                        cursor.execute(sql, (selection.selection_nbr, book_selected.isbn))

            Dao.connection.commit()

            # Si la sélection a été créé, retourner son numéro
            return selection.selection_nbr

        # Si la création a échoué, retourner 0
        return 0

    def read(self, selection_nbr: int) -> Optional[Selection]:
        """Renvoie la sélection correspondant à l'entité dont le numéro est selection_nbr
           (ou None si elle n'a pu être trouvée)"""
        selection: Optional[Selection]

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT s.* 
                FROM selection_book s 
                JOIN president pr
                ON s.id_president = pr.id_president
                JOIN jury_member j
                ON pr.id_jury_member = j.id_jury_member
                JOIN person p 
                ON j.id_person = p.id_person
                WHERE sb.selection_nbr = %s
            """
            cursor.execute(sql, (selection_nbr,))
            record = cursor.fetchone()
            if record is not None:

                # Créer l'objet Président à inclure dans la sélection
                president = President(record["first_name"], record["last_name"])

                # Créer l'objet Selection à afficher
                selection = Selection(
                    record['selection_nbr'], record['selection_date'], president
                )

                sql = """
                    SELECT sb.*
                    FROM selection_book sb
                    JOIN selection s e ON sb.selection_nbr = s.selection_nbr
                    JOIN book b ON sb.isbn = b.isbn
                    WHERE sb.selection_nbr = %s
                """
                cursor.execute(sql, (selection_nbr,))
                record_books = cursor.fetchall()

                if record_books is not None:
                    for record_book in record_books:
                        book_dao = BookDao()
                        book = book_dao.get_book(record_book)

                        if book is not None:
                            selection.select_book(book)

                return selection

        return None



    def update(self, selection: Selection) -> bool:
        """Met à jour en BD l'entité Selection correspondant à selection, pour y correspondre

        :param selection: sélection déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """

        with (Dao.connection.cursor() as cursor):
            sql = "SELECT * FROM selection WHERE selection_nbr=%s"
            cursor.execute(sql, (selection.selection_nbr,))
            record = cursor.fetchone()
            if record is not None:
                # Supprimer les livres retirés de l'objet selection dans la BDD
                sql = """
                    SELECT sb.*
                    FROM selection_book sb
                    JOIN selection s e ON sb.selection_nbr = s.selection_nbr
                    JOIN book b ON sb.isbn = b.isbn
                    WHERE sb.selection_nbr = %s
                """
                cursor.execute(sql, (selection.selection_nbr,))
                record_books = cursor.fetchall()
                for record_book in record_books:
                    book_dao = BookDao()
                    book_to_delete = book_dao.get_book(record_book)
                    if book_to_delete not in selection.books_selected:
                        sql = "DELETE FROM selection_book WHERE selection_nbr = %s AND isbn = %s"
                        cursor.execute(sql, (selection.selection_nbr, book_to_delete.isbn))

                # Ajouter les nouveaux livres dans la table SelectionBook
                for book_selected in selection.books_selected:
                    # Vérifier s'ils sont déjà dans la table
                    sql = "SELECT * FROM selection_book WHERE selection_nbr = %s AND isbn = %s"
                    cursor.execute(sql, (selection.selection_nbr, book_selected.isbn))
                    record_new_book = cursor.fetchone()
                    # Insérer les nouveaux livres
                    if record_new_book is None:
                        sql = "INSERT INTO selection_book(selection_nbr, isbn) VALUES (%s, %s)"
                        cursor.execute(sql, (selection.selection_nbr, book_selected.isbn))

                Dao.connection.commit()

        return self.read(selection.selection_nbr) == selection

    def delete(self, selection: Selection) -> bool:
        """Supprime en BD l'entité Selection correspondant à selection

        :param selection: sélection dont l'entité Selection correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        # Supprimer les personnages principaux de la sélection
        if selection.main_characters is not None:
            main_character_dao: MainCharacterDao = MainCharacterDao()
            for main_character in selection.main_characters:
                main_character_dao.delete(main_character)

        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM selection WHERE selection_nbr=%s"
            cursor.execute(sql, (selection.selection_nbr,))

        Dao.connection.commit()

        return self.read(selection.selection_nbr) is None