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

    school: Goncourt = Goncourt()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves
    school.display_courses_list()


    # Insertion des étudiants
    for student in school.students:
        print(school.create_student(student))
    input("Etudiants ajoutés. Appuyez sur Entrée pour continuer...\n")

    # Insertion des enseignants
    for teacher in school.teachers:
        print(school.create_teacher(teacher))
    input("Enseignants ajoutés. Appuyez sur Entrée pour continuer...\n")

    # Insertion des cours
    for course in school.courses:
        print(school.create_course(course))
    input("Etudiants ajoutés. Appuyez sur Entrée pour continuer...\n")


    # Affichage des étudiants
    for student in school.students:
        print(school.get_student_by_number(student.student_nbr))
    input("Etudiants affichés. Appuyez sur Entrée pour continuer...\n")

    # Affichage des enseignants
    for teacher in school.teachers:
        print(school.get_teacher_by_id(teacher.id_teacher))
    input("Enseignants affichés. Appuyez sur Entrée pour continuer...\n")

    # Affichage des cours
    for course in school.courses:
        print(school.get_course_by_id(course.id))
    input("Cours affichés. Appuyez sur Entrée pour continuer...\n")


    # Suppression des étudiants
    for student in school.students:
        print(school.delete_student(student))
    input("Etudiants supprimés. Appuyez sur Entrée pour continuer...\n")

    # Suppression des cours
    for course in school.courses:
        print(school.delete_course(course))
    input("Cours supprimés. Appuyez sur Entrée pour continuer...\n")

    # Suppression des enseignants
    for teacher in school.teachers:
        print(school.delete_teacher(teacher))
    input("Enseignants supprimés. Appuyez sur Entrée pour terminer le programme...\n")

    # Réinitialisation des auto-increment
    print("Réinitialisation des auto-increment...")
    with Dao.connection.cursor() as cursor:
        for table in ["address","student","course","teacher","person"]:
            sql = f"ALTER TABLE {table} AUTO_INCREMENT = 1;"
            cursor.execute(sql)
    Dao.connection.commit()


if __name__ == '__main__':
    main()
