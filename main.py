import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Chargement et nettoyage des données
df = pd.read_csv("netflix_titles.csv")

# Suppression des lignes contenant des valeurs manquantes dans le dataset
df = df.dropna()

# Encodage des variables catégorielles
encoder = LabelEncoder()

# Encodage des colonnes 'country', 'rating', 'director'
df['country'] = encoder.fit_transform(df['country'])
df['rating'] = encoder.fit_transform(df['rating'])
df['director'] = encoder.fit_transform(df['director'])

# Transformation de la colonne 'duration' pour extraire les minutes comme valeur entière
df['duration'] = df['duration'].apply(lambda x: int(x.split()[0]) if isinstance(x, str) else x)

# Vérification rapide des transformations
print(df.head())

# Définir les caractéristiques (X) et la cible (y) pour l'arbre de décision
X = df[['duration', 'country', 'rating', 'release_year']]
y = df['type']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création du modèle d'arbre de décision avec une profondeur maximale de 5 pour éviter le sur-apprentissage
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Tracé de l'arbre de décision
plt.figure(figsize=(15, 10))

# L'arbre de décision
plot_tree(
    clf,
    feature_names=X.columns,  # Afficher les noms des caractéristiques
    class_names=["Movie", "TV Show"],  # Nom des classes à prédire
    filled=True,  # Remplir les noeuds avec des couleurs distinctes pour chaque classe
    rounded=True,  # Bordures arrondies pour plus de clarté
    proportion=True,  # Afficher les proportions des classes à chaque noeud
    fontsize=12,  # Taille de la police pour les textes
)

# Ajout d'un titre à l'arbre de décision
plt.title("Arbre de Décision - Prédiction du Type de Contenu Netflix", fontsize=14, fontweight='bold', color='red')

# Affichage du graphique
plt.show()

# Evaluation du modèle
# Prédiction des valeurs sur l'ensemble de test
y_pred = clf.predict(X_test)

# Affichage de la précision du modèle sur les données de test
accuracy = clf.score(X_test, y_test)
print(f"Précision du modèle sur les données de test : {accuracy:.2f}")

# Calcul de la matrice de confusion pour évaluer la performance du modèle sur chaque classe
cm = confusion_matrix(y_test, y_pred)

# Affichage de la matrice de confusion pour voir les erreurs de classification par classe
print("Matrice de Confusion :")
print(cm)

# Affichage du rapport de classification pour obtenir des métriques détaillées par classe (précision, rappel, F1-score)
print("Rapport de classification :")
print(classification_report(y_test, y_pred))
