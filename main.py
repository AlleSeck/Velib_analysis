import os

print("🚀 Lancement de l'analyse Vélib'...")

# Étape 1 : Récupérer les données
os.system("python scripts/fetch_data.py")

# Étape 2 : Analyser les données
os.system("python scripts/analysis.py")
