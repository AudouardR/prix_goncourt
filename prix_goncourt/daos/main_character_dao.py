# -*- coding: utf-8 -*-

"""
Classe Dao[MainCharacter]
"""
from models.main_character import MainCharacter
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class MainCharacterDao(Dao[MainCharacter]):
    def create(self, main_character: MainCharacter) -> int:
        """Crée en BD l'entité MainCharacter correspondant au personnage principal MainCharacter

                :param main_character: à créer sous forme d'entité MainCharacter en BD
                :return: l'id de l'entité insérée en BD (0 si la création a échoué)
                """
        if self.read(main_character.id) is None:

            with Dao.connection.cursor() as cursor:
                # Ajouter le personnage principal dans la table Person
                sql = "INSERT INTO main_character(name, isbn) VALUES (%s, %s)"
                cursor.execute(sql, (main_character.name, main_character.book.isbn,))

                main_character.id = cursor.lastrowid

            Dao.connection.commit()

            # Si le personnage principal a été créé, retourner son identifiant
            return main_character.id

        # Si la création a échoué, retourner 0
        return 0

    def read(self, id_main_character: int) -> Optional[MainCharacter]:
        """Renvoie le personnage principal correspondant à l'entité dont l'id est id_main_character
           (ou None si elle n'a pu être trouvée)"""

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM main_character WHERE id_main_character=%s"
            cursor.execute(sql, (id_main_character,))
            record = cursor.fetchone()

        if record is not None:
            main_character = MainCharacter(
                record['name'],
                record['isbn']
            )
            main_character.id = record['id_main_character']
            return main_character

        return None

    def update(self, main_character: MainCharacter) -> bool:
        """Met à jour en BD l'entité MainCharacter correspondant à main_character, pour y correspondre

        :param main_character: personnage principal déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM main_character WHERE id_main_character=%s"
            cursor.execute(sql, (main_character.id,))
            record = cursor.fetchone()
            if record is not None:
                sql = "UPDATE main_character SET name=%s, isbn=%s WHERE id_main_character=%s"
                cursor.execute(sql, (main_character.name, main_character.book.isbn, main_character.id,))
                Dao.connection.commit()

        return self.read(main_character.id) == main_character


    def delete(self, main_character: MainCharacter) -> bool:
        """Supprime en BD l'entité MainCharacter correspondant à main_character

        :param main_character: personnage principal dont l'entité MainCharacter correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            # Supprimer le personnage principal de la table MainCharacter
            sql = "DELETE FROM main_character WHERE id_main_character=%s"
            cursor.execute(sql, (main_character.id,))

        Dao.connection.commit()

        return self.read(main_character.id) is None