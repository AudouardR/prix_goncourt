# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""
from daos.main_character_dao import MainCharacterDao
from models.author import Author
from models.book import Book
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any

from models.editor import Editor


@dataclass
class BookDao(Dao[Book]):
    def create(self, book: Book) -> Optional[str]:
        """Crée en BD l'entité Book correspondant au livre Book

                :param book: à créer sous forme d'entité Book en BD
                :return: l'isbn de l'entité insérée en BD (None si la création a échoué)
                """
        if self.read(book.isbn) is None:

            with Dao.connection.cursor() as cursor:
                # Ajouter le livre dans la table Book
                arguments = (book.isbn, book.title, book.price, book.publishing_date,
                             book.nb_pages, book.author.id, book.editor.id)
                sql = "INSERT INTO book(isbn, title, price, publishing_date, nb_pages, id_author, id_editor"
                if book.summary is not None:
                    sql += ", summary"
                    arguments += (book.summary, )
                if book.editor_price is not None:
                    sql += ", editor_price"
                    arguments += (book.editor_price, )
                sql += ") VALUES (%s" + ", %s"*(len(arguments)-1) + ")"
                cursor.execute(sql, arguments)

            # Ajouter les personnages principaux du livre
            if book.main_characters is not None:
                main_character_dao: MainCharacterDao = MainCharacterDao()
                for main_character in book.main_characters:
                    # ID créé pour chaque personnage principal
                    main_character.id = main_character_dao.create(main_character)

            Dao.connection.commit()

            # Si le livre a été créé, retourner son isbn
            return book.isbn

        # Si la création a échoué, retourner None
        return None

    def read(self, isbn: str) -> Optional[Book]:
        """Renvoie le livre correspondant à l'entité dont l'id est isbn
           (ou None si elle n'a pu être trouvée)"""
        book: Optional[Book]

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT b.isbn, b.title, b.summary, 
                    b.price, b.publishing_date, 
                    b.nb_pages, b.editor_price,
                    b.id_editor, e.label, 
                    b.id_author, a.biography, 
                    a.id_person, p.first_name, p.last_name
                FROM book b
                JOIN editor e ON b.id_editor = e.id_editor
                JOIN author a ON b.id_author = a.id_author
                JOIN person p ON a.id_person = p.id_person
                WHERE b.isbn = %s
            """
            cursor.execute(sql, (isbn,))
            record = cursor.fetchone()
        if record is not None:
            book = self.get_book(record)

            return book

        return None

    @staticmethod
    def get_book(record: tuple[Any, ...]) -> Book | None:
        """
        Convertir un livre récupéré de la BDD en objet
        """
        # Auteur et éditeur du livre
        author: Author = Author(record['id_author'])
        editor: Editor = Editor(record['id_editor'])

        # Créer l'objet Livre à afficher
        if record['summary'] is not None:
            if record['editor_price'] is not None:
                book = Book(
                    record['isbn'], record['title'], record['price'],
                    record['publishing_date'], record['nb_pages'],
                    author, editor, record['summary'], record['editor_price']
                )
            else:
                book = Book(
                    record['isbn'], record['title'], record['price'],
                    record['publishing_date'], record['nb_pages'],
                    author, editor, record['summary']
                )
        else:
            if record['editor_price'] is not None:
                book = Book(
                    record['isbn'], record['title'], record['price'],
                    record['publishing_date'], record['nb_pages'],
                    author, editor, record['editor_price']
                )
            else:
                book = Book(
                    record['isbn'], record['title'], record['price'],
                    record['publishing_date'], record['nb_pages'],
                    author, editor
                )
        return book

    def update(self, book: Book) -> bool:
        """Met à jour en BD l'entité Book correspondant à book, pour y correspondre

        :param book: livre déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        # Modifier les personnages principaux du livre
        if book.main_characters is not None:
            main_character_dao: MainCharacterDao = MainCharacterDao()
            for main_character in book.main_characters:
                main_character_dao.update(main_character)

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM book WHERE isbn=%s"
            cursor.execute(sql, (book.isbn,))
            record = cursor.fetchone()
            if record is not None:
                if book.summary is not None:
                    # Arguments de la commande SQL
                    arguments = (book.title, book.price, book.publishing_date, book.nb_pages,
                                book.author.id, book.editor.id,)

                    # Commande SQL
                    sql = ("UPDATE book "
                           "SET title=%s, price=%s, publishing_date=%s, nb_pages=%s, "
                           "id_author=%s, id_editor=%s")

                    # Modifier le résumé s'il existe
                    if book.summary is not None:
                        sql += ", summary=%s"
                        arguments += (book.summary, )

                    # Modifier le prix d'éditeur s'il existe
                    if book.editor_price is not None:
                        sql += ", editor_price=%s"
                        arguments += (book.editor_price, )

                    # Ajouter l'ISBN comme dernier argument
                    sql += " WHERE isbn=%s"
                    arguments += (book.isbn,)

                    cursor.execute(sql, arguments)
                Dao.connection.commit()

        return self.read(book.isbn) == book

    def delete(self, book: Book) -> bool:
        """Supprime en BD l'entité Book correspondant à book

        :param book: livre dont l'entité Book correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        # Supprimer les personnages principaux du livre
        if book.main_characters is not None:
            main_character_dao: MainCharacterDao = MainCharacterDao()
            for main_character in book.main_characters:
                main_character_dao.delete(main_character)

        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM selection_book WHERE isbn=%s"
            cursor.execute(sql, (book.isbn,))

            sql = "DELETE FROM book WHERE isbn=%s"
            cursor.execute(sql, (book.isbn,))

        Dao.connection.commit()

        return self.read(book.isbn) is None