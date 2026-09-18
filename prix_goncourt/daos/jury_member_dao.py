# -*- coding: utf-8 -*-

"""
Classe Dao[JuryMember]
"""
from daos.address_dao import AddressDao
from models.jury_member import JuryMember
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class JuryMemberDao(Dao[JuryMember]):
    def create(self, jury_member: JuryMember) -> int:
        """Crée en BD l'entité JuryMember correspondant à le membre du jury JuryMember

                :param jury_member: à créer sous forme d'entité JuryMember en BD
                :return: l'id de l'entité insérée en BD (0 si la création a échoué)
                """
        if self.read(jury_member.id_jury_member) is None:

            with Dao.connection.cursor() as cursor:
                # Ajouter le membre du jury dans la table Person
                sql = "INSERT INTO person(first_name, last_name) VALUES (%s, %s)"
                cursor.execute(sql, (jury_member.first_name, jury_member.last_name))

                # ID généré par la BDD
                jury_member.id_person = cursor.lastrowid

                # Ajouter le membre du jury dans la table JuryMember
                sql = "INSERT INTO jury_member(id_person) VALUES (%s)"
                cursor.execute(sql, jury_member.id_person)

                jury_member.id_jury_member = cursor.lastrowid

            Dao.connection.commit()

            # Si le membre du jury a été créé, retourner son numéro
            return jury_member.id_jury_member

        # Si la création a échoué, retourner 0
        return 0

    def read(self, id_jury_member: int) -> Optional[JuryMember]:
        """Renvoie le membre du jury correspondant à l'entité dont l'id est id_jury_member
           (ou None si elle n'a pu être trouvée)"""

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT j.id_jury_member, p.id_person, p.first_name, p.last_name
                FROM jury_member j
                JOIN person p 
                ON j.id_person = p.id_person
                WHERE j.id_jury_member = %s
            """
            cursor.execute(sql, (id_jury_member,))
            record = cursor.fetchone()

        if record is not None:
            jury_member = JuryMember(
                record['first_name'],
                record['last_name']
            )
            jury_member.id_person = record['id_person']
            jury_member.id_jury_member = record['id_jury_member']
            return jury_member

        return None

    def update(self, jury_member: JuryMember) -> bool:
        """Met à jour en BD l'entité JuryMember correspondant à jury_member, pour y correspondre

        :param jury_member: membre du jury déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM jury_member WHERE id_jury_member=%s"
            cursor.execute(sql, (jury_member.id_jury_member,))
            record = cursor.fetchone()
            if record is not None:
                sql = "UPDATE person SET first_name=%s, last_name=%s WHERE id_person=%s"
                cursor.execute(sql, (jury_member.first_name, jury_member.last_name, jury_member.id_person))
                Dao.connection.commit()

        if self.read(jury_member.id_jury_member) == jury_member:
            return True

        return False

    def delete(self, jury_member: JuryMember) -> bool:
        """Supprime en BD l'entité JuryMember correspondant à jury_member

        :param jury_member: membre du jury dont l'entité JuryMember correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            # Sélectionner l'id_person du membre du jury dans la table JuryMember et enregistrer la sélection
            sql = "SELECT id_person FROM jury_member WHERE id_jury_member=%s"
            cursor.execute(sql, (jury_member.id_jury_member,))
            record = cursor.fetchone()
            if record is not None:
                # Supprimer le membre du jury de la table JuryMember
                sql = "DELETE FROM jury_member WHERE id_jury_member=%s"
                cursor.execute(sql, (jury_member.id_jury_member,))

                # Supprimer le membre du jury de la table Person
                sql = "DELETE FROM person WHERE id_person=%s"
                cursor.execute(sql, (jury_member.id_person,))

        Dao.connection.commit()

        return self.read(jury_member.id_jury_member) is None