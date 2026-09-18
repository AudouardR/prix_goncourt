# -*- coding: utf-8 -*-

"""
Classe Dao[Editor]
"""
from models.editor import Editor
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class EditorDao(Dao[Editor]):
    def create(self, editor: Editor) -> int:
        """Crée en BD l'entité Editor correspondant à l'éditeur Editor

                :param editor: à créer sous forme d'entité Editor en BD
                :return: l'id de l'entité insérée en BD (0 si la création a échoué)
                """
        if self.read(editor.id) is None:

            with Dao.connection.cursor() as cursor:
                # Ajouter l'éditeur dans la table Person

                sql = "INSERT INTO editor(label) VALUES (%s)"
                cursor.execute(sql, (editor.label,))

                editor.id = cursor.lastrowid

            Dao.connection.commit()

            # Si l'éditeur a été créé, retourner son identifiant
            return editor.id

        # Si la création a échoué, retourner 0
        return 0

    def read(self, id_editor: int) -> Optional[Editor]:
        """Renvoie l'éditeur correspondant à l'entité dont l'id est id_editor
           (ou None si elle n'a pu être trouvée)"""

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM editor WHERE id_editor=%s"
            cursor.execute(sql, (id_editor,))
            record = cursor.fetchone()

        if record is not None:
            editor = Editor(
                record['label']
            )
            editor.id = record['id_editor']
            return editor

        return None

    def update(self, editor: Editor) -> bool:
        """Met à jour en BD l'entité Editor correspondant à editor, pour y correspondre

        :param editor: éditeur déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM editor WHERE id_editor=%s"
            cursor.execute(sql, (editor.id,))
            record = cursor.fetchone()
            if record is not None:
                sql = "UPDATE editor SET label=%s WHERE id_editor=%s"
                cursor.execute(sql, (editor.label, editor.id,))
                Dao.connection.commit()

        return self.read(editor.id) == editor


    def delete(self, editor: Editor) -> bool:
        """Supprime en BD l'entité Editor correspondant à editor

        :param editor: éditeur dont l'entité Editor correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """

        with Dao.connection.cursor() as cursor:
            # Supprimer l'éditeur de la table Editor
            sql = "DELETE FROM editor WHERE id_editor=%s"
            cursor.execute(sql, (editor.id,))

        Dao.connection.commit()

        return self.read(editor.id) is None