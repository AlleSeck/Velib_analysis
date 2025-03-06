import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = "data/velib_data.csv"

# check if the file exist
try:
    df = pd.read_csv(file_path)
    print("✅ Données chargées avec succès !")
except FileNotFoundError:
    print(f"❌ Erreur : Le fichier {file_path} n'existe pas. Exécute d'abord fetch_data.py.")
    exit()

# Display the first rows for verification
print(df.head())
print(df.tail())  #the first rows

# 📊 1️⃣ Histogram of station capacity
plt.figure(figsize=(10, 5))
ax = sns.histplot(df["capacity"], bins=20, kde=True, color="blue")
# Add a legend
hist_patch = plt.Rectangle((0, 0), 1, 1, fc="blue", alpha=0.5, label="Histogramme (fréquence)")
kde_line, = ax.lines  # Récupérer la ligne KDE
kde_line.set_label("Courbe KDE (densité)")

plt.legend()
plt.title("Distribution de la capacité des stations Vélib'")
plt.xlabel("Capacité des stations")
plt.ylabel("Nombre de stations")
plt.show(block=False)


# 📊 2️⃣ Distribution of stations with or without breakdowns
plt.figure(figsize=(6, 4))
df["panne"].value_counts().plot(kind="bar", color=["green", "red"])
plt.xticks(ticks=[0, 1], labels=["Fonctionnelles", "En panne"], rotation=0)
plt.title("Stations Vélib fonctionnelles vs en panne")
plt.xlabel("Statut")
plt.ylabel("Nombre de stations")
plt.legend(["Fonctionnelles", "En panne"])
plt.show()

# # 📊 3️⃣ Number of mechanical vs electric bikes
# if "mechanical" in df.columns and "ebike" in df.columns:
#     plt.figure(figsize=(6, 4))
#     df[["mechanical", "ebike"]].sum().plot(kind="bar", color=["blue", "orange"])
#     plt.title("Nombre total de vélos mécaniques et électriques")
#     plt.xticks(rotation=0)
#     plt.ylabel("Nombre de vélos")
#     plt.legend(["Vélos mécaniques", "Vélos électriques"])  # Ajouter la légende ici
#     plt.show()
# else:
#     print("❌ Erreur : Les colonnes 'mechanical' et 'ebike' ne sont pas présentes dans les données")

