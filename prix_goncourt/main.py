#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from business.goncourt import Goncourt
from daos.dao import Dao


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    goncourt: Goncourt = Goncourt()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    goncourt.init_static()

    # Réinitialisation des auto-increment
    print("Réinitialisation des auto-increment...")
    with Dao.connection.cursor() as cursor:
        for table in ["address","student","course","teacher","person"]:
            sql = f"ALTER TABLE {table} AUTO_INCREMENT = 1;"
            cursor.execute(sql)
    Dao.connection.commit()


if __name__ == '__main__':
    main()
