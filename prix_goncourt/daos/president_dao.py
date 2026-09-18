# -*- coding: utf-8 -*-

"""
Classe Dao[President]
"""
from models.president import President
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class PresidentDao(Dao[President]):
    def create(self, president: President) -> int:
        """Crée en BD l'entité President correspondant au président du jury

                :param president: à créer sous forme d'entité President en BD
                :return: l'id de l'entité insérée en BD (0 si la création a échoué)
                """
        if self.read(president.id) is None:

            with Dao.connection.cursor() as cursor:
                # Ajouter le président du jury dans la table Person
                sql = "INSERT INTO person(first_name, last_name) VALUES (%s, %s)"
                cursor.execute(sql, (president.first_name, president.last_name))

                # ID généré par la BDD
                president.id_person = cursor.lastrowid

                # Ajouter le président du jury dans la table JuryMember
                sql = "INSERT INTO jury_member(id_person) VALUES (%s)"
                cursor.execute(sql, president.id_person,)

                # ID généré par la BDD
                president.id_jury_member = cursor.lastrowid

                # Ajouter le président du jury dans la table President
                sql = "INSERT INTO president(id_jury_member) VALUES (%s)"
                cursor.execute(sql, president.id_jury_member,)

                # ID généré par la BDD
                president.id = cursor.lastrowid

            Dao.connection.commit()

            # Si le membre du jury a été créé, retourner son numéro
            return president.id

        # Si la création a échoué, retourner 0
        return 0

    def read(self, id_president: int) -> Optional[President]:
        """Renvoie le membre du jury correspondant à l'entité dont l'id est id_president
           (ou None si elle n'a pu être trouvée)"""

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT pr.id_president, j.id_jury_member, p.id_person, p.first_name, p.last_name
                FROM president pr
                JOIN jury_member j
                ON pr.id_jury_member = j.id_jury_member
                JOIN person p 
                ON j.id_person = p.id_person
                WHERE pr.id_president = %s
            """
            cursor.execute(sql, (id_president,))
            record = cursor.fetchone()

        if record is not None:
            president = President(
                record['first_name'],
                record['last_name']
            )
            president.id_person = record['id_person']
            president.id_jury_member = record['id_jury_member']
            president.id = record['id_president']
            return president

        return None

    def update(self, president: President) -> bool:
        """Met à jour en BD l'entité President correspondant à president, pour y correspondre

        :param president: membre du jury déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM president WHERE id_president=%s"
            cursor.execute(sql, (president.id,))
            record = cursor.fetchone()
            if record is not None:
                sql = "UPDATE person SET first_name=%s, last_name=%s WHERE id_person=%s"
                cursor.execute(sql, (president.first_name, president.last_name, president.id_person))
                Dao.connection.commit()

        if self.read(president.id) == president:
            return True

        return False

    def delete(self, president: President) -> bool:
        """Supprime en BD l'entité President correspondant à president

        :param president: président du jury dont l'entité President correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            # Sélectionner l'id_jury_member du président du jury dans la table President et enregistrer la sélection
            sql = "SELECT id_jury_member FROM president WHERE id_president=%s"
            cursor.execute(sql, (president.id,))
            record = cursor.fetchone()
            if record is not None:
                # Supprimer le président du jury de la table President
                sql = "DELETE FROM president WHERE id_president=%s"
                cursor.execute(sql, (president.id,))

            # Sélectionner l'id_person du président du jury dans la table JuryMember et enregistrer la sélection
            sql = "SELECT id_person FROM jury_member WHERE jury_member=%s"
            cursor.execute(sql, (president.id_jury_member,))
            record = cursor.fetchone()
            if record is not None:
                # Supprimer le président du jury de la table JuryMember
                sql = "DELETE FROM jury_member WHERE jury_member=%s"
                cursor.execute(sql, (president.id_jury_member,))

                # Supprimer le président du jury de la table Person
                sql = "DELETE FROM person WHERE id_person=%s"
                cursor.execute(sql, (president.id_person,))

        Dao.connection.commit()

        return self.read(president.id) is None