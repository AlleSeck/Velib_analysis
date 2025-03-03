import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
file_path = "data/velib_data.csv"

# Vérifier si le fichier existe
try:
    df = pd.read_csv(file_path)
    print("✅ Données chargées avec succès !")
except FileNotFoundError:
    print(f"❌ Erreur : Le fichier {file_path} n'existe pas. Exécute d'abord fetch_data.py.")
    exit()

# Afficher les premières lignes pour vérification
print(df.head())

# 📊 1️⃣ Histogramme du nombre de vélos disponibles par station
plt.figure(figsize=(10, 5))
sns.histplot(df["capacity"], bins=20, kde=True, color="blue")
plt.title("Distribution de la capacité des stations Vélib'")
plt.xlabel("Capacité des stations")
plt.ylabel("Nombre de stations")
plt.show()

# 📊 2️⃣ Répartition des stations avec ou sans panne
plt.figure(figsize=(6, 4))
df["panne"].value_counts().plot(kind="bar", color=["green", "red"])
plt.xticks(ticks=[0, 1], labels=["Fonctionnelles", "En panne"], rotation=0)
plt.title("Stations Vélib fonctionnelles vs en panne")
plt.xlabel("Statut")
plt.ylabel("Nombre de stations")
plt.show()

# 📊 3️⃣ Nombre de vélos mécaniques vs électriques
plt.figure(figsize=(6, 4))
df[["mechanical", "ebike"]].sum().plot(kind="bar", color=["blue", "orange"])
plt.title("Nombre total de vélos mécaniques et électriques")
plt.xticks(rotation=0)
plt.ylabel("Nombre de vélos")
plt.show()
