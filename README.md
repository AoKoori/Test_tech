# Application de Trafic Bordeaux - DevOps Test

## Fonctionnalités

- Récupération des données sur le trafic depuis l'API publique de Bordeaux Open Data.
- Récupération des données toutes les 5 minutes en arrière-plan grâce à **APScheduler**.
- Affichage des données sous forme de tableau HTML dans un serveur **Flask**.
- Conteneurisation de l'application avec Docker.

## Prérequis

- Docker
- Python 3.x
- `pip` pour installer les dépendances Python

## Création de l'image

```bash
docker build -t trafic-bordeaux-app .
```

## Run l'App

```bash
docker run -p 5000:5000 trafic-bordeaux-app
```

## Structure du projet

📦Test_tech
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📜app.py
 ┣ 📜Dockerfile
 ┣ 📜README.md
 ┗ 📜requirements.txt
 