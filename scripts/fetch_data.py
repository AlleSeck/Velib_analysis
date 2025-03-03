import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Récupérer la clé API depuis .env
API_KEY = os.getenv("VELIB_API_KEY")

# Vérifier si la clé API est bien chargée
if not API_KEY:
    raise ValueError("❌ Erreur : La clé API VELIB n'a pas été trouvée. Vérifie ton fichier .env !")

# ca Crée le dossier "data" s'il n'existe pas
os.makedirs("data", exist_ok=True)

# URL de l'API Vélib
API_URL = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-emplacement-des-stations/exports/json"

# Faire la requête à l'API
print("📡 Récupération des données Vélib...")
response = requests.get(API_URL)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Convertir en DataFrame Pandas
    df = pd.DataFrame(data)

    # Afficher les colonnes disponibles pour vérification
    print("✅ Colonnes disponibles :", df.columns.tolist())

    # Sélectionner les colonnes pertinentes (adapté selon les vraies colonnes)
    columns_to_keep = ["stationcode", "name", "capacity", "coordonnees_geo", "station_opening_hours"]
    df = df[columns_to_keep]

    # Ajouter une colonne "panne" (si la capacité est 0)
    df["panne"] = df["capacity"] == 0

    # Sauvegarder en CSV
    df.to_csv("data/velib_data.csv", index=False, encoding="utf-8")

    print("✅ Données Vélib récupérées et enregistrées dans 'data/velib_data.csv' !")

else:
    print(f"❌ Erreur lors de la récupération des données (Code {response.status_code})")
