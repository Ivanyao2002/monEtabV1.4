# monEtabV1.4
Projet mon Etab, gestion d'un établissement ; Au démarage de l'application, l'administrateur est amené à configurer d'entrée les paramètres de l'établissement puis de l'école, ensuite il enregistre son compte pour acceder à l'interface d'administration de l'école.

## Les étapes d'installation de l'application :
- Ouvrer un terminal puis cloner le lien github de l'application : git clone https://github.com/Ivanyao2002/monEtabV1.4.git
- Créer un environnement virtuel dans le repertoire ( python ou python3 pour Unix -m venv venv ou env)
- Naviguer vers le fichier activate.bat soit dans scripts ou bin, puis activer l'environnement (source activate ou activate pour windows)
- Revener au repertoire de votre projet puis installer les dépendances de l'application à partir du fichier requirements.txt (pip ou pip3 install -r requirements.txt)
- Installez et configurez une base de données Postgresql ou autre puis configurer les accès dans le fichier settings.py
- Naviguez vers le repertoire source (src) puis créer et appliquer les migrations : python manage.py makemigrations ensuite python manage.py migrate
  
## Les instructions de démarrage :
- Naviguez vers le repertoire source (src) puis lancer le server : python manage.py runserver, vous pouvez preciser le port python manage.py runserver numeros_port ( exple : python manage.py runserver 8888)
  
## Description des fonctionnalités principales de l'application :
- CRUD des proefesseurs
- CRUD des étudiants
- CRUD des addresses
- CRUD de l'absence d'un élève
- CRUD des utilisateurs
- CRUD d'une carte étudiant
- Activer ou désactiver un compte
- Edition de rapports en pdf ou en excel
- Possibilité de faire des recherches sur toutes les listes


