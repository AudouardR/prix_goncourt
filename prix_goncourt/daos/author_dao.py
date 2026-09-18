# -*- coding: utf-8 -*-

"""
Classe Dao[Author]
"""
from models.author import Author
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class AuthorDao(Dao[Author]):
    def create(self, author: Author) -> int:
        """Crée en BD l'entité Author correspondant à l'auteur Author

                :param author: à créer sous forme d'entité Author en BD
                :return: l'id de l'entité insérée en BD (0 si la création a échoué)
                """
        if self.read(author.id) is None:

            with Dao.connection.cursor() as cursor:
                # Ajouter l'auteur dans la table Person

                sql = "INSERT INTO person(first_name, last_name) VALUES (%s, %s)"
                cursor.execute(sql, (author.first_name, author.last_name,))

                # ID généré par la BDD
                author.id_person = cursor.lastrowid

                # Ajouter l'auteur dans la table Author
                if author.biography is not None:
                    sql = "INSERT INTO author(biography, id_person) VALUES (%s, %s)"
                    cursor.execute(sql, (author.biography, author.id_person,))
                else:
                    sql = "INSERT INTO author(id_person) VALUES (%s)"
                    cursor.execute(sql, (author.id_person,))

                author.id = cursor.lastrowid

            Dao.connection.commit()

            # Si l'auteur a été créé, retourner son identifiant
            return author.id

        # Si la création a échoué, retourner 0
        return 0

    def read(self, id_author: int) -> Optional[Author]:
        """Renvoie l'auteur correspondant à l'entité dont l'id est id_author
           (ou None si elle n'a pu être trouvée)"""

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT a.id_author, a.biography, p.id_person, p.first_name, p.last_name
                FROM author a
                JOIN person p 
                ON a.id_person = p.id_person
                WHERE a.id_author = %s
            """
            cursor.execute(sql, (id_author,))
            record = cursor.fetchone()

        if record is not None:
            author = Author(
                record['biography'],
                record['first_name'],
                record['last_name']
            )
            author.id_person = record['id_person']
            author.id = record['id_author']
            return author

        return None

    def update(self, author: Author) -> bool:
        """Met à jour en BD l'entité Author correspondant à author, pour y correspondre

        :param author: auteur déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM author WHERE id_author=%s"
            cursor.execute(sql, (author.id,))
            record = cursor.fetchone()
            if record is not None:
                if author.biography is not None:
                    sql = "UPDATE author SET biography=%s WHERE id_author=%s"
                    cursor.execute(sql, (author.biography, author.id,))
                else:
                    sql = "UPDATE author SET biography=NULL WHERE id_author=%s"
                    cursor.execute(sql, (author.id,))
                sql = "UPDATE person SET first_name=%s, last_name=%s, WHERE id_person=%s"
                cursor.execute(sql, (author.first_name, author.last_name, author.id_person,))
                Dao.connection.commit()

        if self.read(author.id) == author:
            return True

        return False

    def delete(self, author: Author) -> bool:
        """Supprime en BD l'entité Author correspondant à author

        :param author: auteur dont l'entité Author correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            # Sélectionner l'id_person de l'auteur dans la table Author et enregistrer la sélection
            sql = "SELECT id_person FROM author WHERE id_author=%s"
            cursor.execute(sql, (author.id,))
            record = cursor.fetchone()
            if record is not None:
                # Supprimer l'auteur de la table Author
                sql = "DELETE FROM author WHERE id_author=%s"
                cursor.execute(sql, (author.id,))

                # Supprimer l'auteur de la table Person
                sql = "DELETE FROM person WHERE id_person=%s"
                cursor.execute(sql, (author.id_person,))

        Dao.connection.commit()

        return self.read(author.id) is None