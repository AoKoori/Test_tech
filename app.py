from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import requests, json, os

app = Flask(__name__)

def recuperer_donnees():
    url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=ci_courb_a&rows=193"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extraire les champs 'bm_heure' et 'bm_prevision' des données JSON
        donnees_traitees = [
            {"bm_heure": record['fields']['bm_heure'], "bm_prevision": record['fields']['bm_prevision']}
            for record in data['records']
        ]
        print(donnees_traitees)
        # Sauvegarder les données dans un fichier JSON
        with open("donnees.json", "w") as f:
            json.dump(donnees_traitees, f)
    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")

# Planification de la tâche toutes les 5 minutes
recuperer_donnees()
scheduler = BackgroundScheduler()
scheduler.add_job(recuperer_donnees, 'interval', minutes=5)
scheduler.start()

# Charger les données sauvegardées pour l'affichage
def charger_donnees():
    if os.path.exists("donnees.json"):
        with open("donnees.json", "r") as f:
            return json.load(f)
    return []

@app.route('/')
def index():
    donnees = charger_donnees()
    return render_template('index.html', donnees=donnees)

if __name__ == '__main__':
    # Démarrer Flask
    app.run(host="0.0.0.0", port=5000)
