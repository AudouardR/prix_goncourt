# Prix Goncourt

Application Python portant sur le Prix Goncourt avec un _design pattern_ DAO, pour l'examen Python Avancé.

## Dossiers

`.venv` : Environnement virtuel pour exécuter le programme  
`bdd` : Base de données (prix_goncourt.sql)  
`doc` : Diagrammes UML (cas d'utilisation et classes) et MCD  
`prix_goncourt` (sous-répertoire) : Code Python   
* `business` : classe principale Goncourt
* `daos`: design pattern DAO
* `models` : classes

## Lancer l'application

Faire ceci sur le sous-répertoire `prix_goncourt` du répertoire principal `prix_goncourt` pour indiquer à PyCharm qu'il s'agit du répertoire de l'application
(pour ne pas avoir d'avertissements sur des `import` non résolus) :
* clic-droit > _Mark directory as_ > _Sources root_
* Menu > File > _Invalidate Caches_ > _Invalidate and Restart_

Pour exécuter le programme, sur PyCharm, exécuter le fichier `main.py` dans le sous-répertoire `prix_goncourt`