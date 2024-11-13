# Analyse de l'Arbre de Décision pour la Prédiction du Type de Contenu Netflix

Cet arbre de décision vise à prédire le type de contenu sur Netflix (Movies ou TV Show) en se basant sur plusieurs attributs, notamment la durée, le pays, et le classement. Les noeuds de l'arbre représentent les décisions prises en fonction de ces attributs, tandis que les feuilles correspondent aux prédictions finales du modèle (classe Movie ou TV Show).

# Chaque noeud affiche des informations clés :
  
Condition : La règle appliquée pour décider de la branche à suivre (ex. : duration <= 10.5).
Gini : Indice de Gini, qui mesure l'impureté du noeud. Un indice de Gini de 0 signifie que le noeud est pur, c'est-à-dire qu'il contient des exemples appartenant à une seule classe.
Samples : Pourcentage de l'ensemble des échantillons qui atteignent ce noeud.
Value : Distribution des échantillons entre les classes Movie et TV Show.
Class : Prédiction finale du noeud pour cette branche de l'arbre.

# Analyse des Noeuds et de la Prédiction : 
# Noeud Racine (Node #0) :
Condition : duration <= 10.5
Gini : 0.052
Samples : 100.0% des données
Value : [0.973, 0.027]
Classe prédite : Movie
Interprétation : À ce niveau, l'arbre commence par la durée du contenu. Si la durée est inférieure ou égale à 10.5 minutes, l'arbre passe à la branche de gauche, sinon il passe à la droite.

# Noeud Gauche (Node #1) :
Condition : Aucune, car il s'agit d'une feuille
Gini : 0.0 (noeud pur)
Samples : 2.7% des données
Value : [0.0, 1.0]
Classe prédite : TV Show
Interprétation : Pour une faible durée (<= 10.5 minutes), l'arbre prédit avec certitude que le contenu est une TV Show. Ce noeud est pur, signifiant que tous les exemples ayant atteint ce point appartiennent à la classe TV Show.

# Noeud Droit (Node #2) :
Condition : duration <= 16.0
Gini : 0.0
Samples : 97.3% des données
Value : [1.0, 0.0]
Classe prédite : Movie
Interprétation : Si la durée dépasse 10.5 minutes mais est inférieure ou égale à 16.0 minutes, l'arbre prédit Movie avec une forte certitude. Ici aussi, le noeud est pur.

# Noeud Droit du Node #2 (Node #3) :
Condition : country <= 495.5
Gini : 0.32
Samples : 0.1% des données
Value : [0.8, 0.2]
Classe prédite : Movie
Interprétation : Dans certains cas très rares (0.1% des échantillons), si la durée dépasse 16 minutes, l'arbre examine le pays d'origine du contenu pour faire une distinction supplémentaire. Cependant, cette condition n'a qu'un impact mineur car la majorité des contenus plus longs sont classés comme Movie.

# Dernier Noeud Gauche de Node #3 (Node #4) :
Condition : Aucune, feuille pure
Gini : 0.0
Samples : 0.1% des données
Value : [1.0, 0.0]
Classe prédite : Movie
Interprétation : Si toutes les conditions précédentes sont remplies, l'arbre prédit Movie avec une certitude totale pour ces échantillons spécifiques.

# Dernier Noeud Droit (Node #5) :
Condition : Aucune, feuille pure
Gini : 0.0
Samples : 0.0% des données
Value : [0.0, 1.0]
Classe prédite : TV Show
Interprétation : Dans un cas extrêmement rare où toutes les autres conditions sont satisfaites, le modèle prédit une TV Show. Cependant, cette branche a un impact très limité en raison de la taille très faible de l'échantillon (0.0%).

# Évaluation du Modèle

Après l'entraînement de l'arbre de décision, nous avons évalué les performances du modèle sur les données de test. Voici les résultats détaillés :


# Matrice de Confusion

La matrice de confusion permet de visualiser la performance du modèle en affichant le nombre d'exemples classés correctement ou incorrectement pour chaque classe. 
# Interprétation de la Matrice de Confusion :

# Ligne 1 (Movie) :
1034 : Nombre de films correctement classés comme "Movie" (vrai positif).
1 : Nombre de films incorrectement classés comme "TV Show" (faux négatif).

# Ligne 2 (TV Show) :
0 : Nombre de TV Shows incorrectement classés comme "Movie" (faux positif).
32 : Nombre de TV Shows correctement classés comme "TV Show" (vrai positif).
# Cette matrice montre que le modèle a très bien performé, avec seulement une petite erreur où un film a été classé comme TV Show. Il n'y a eu aucune erreur de classification d'une TV Show en tant que film.

# Rapport de Classification

# Precision :
Pour les films (Movie), la précision est parfaite à 1.00, ce qui signifie que chaque fois que le modèle a prédit "Movie", il avait raison.
Pour les séries (TV Show), la précision est de 0.97, ce qui indique une légère erreur, mais très faible.

# Rappel :
Pour les films, le rappel est parfait (1.00), indiquant qu'aucun film n'a été laissé de côté.
Pour les séries, le rappel est également parfait (1.00), montrant que toutes les TV Shows ont été correctement identifiées.

# Score F1 : 
Le score F1 pour les films est de 1.00, indiquant une excellente performance.
Le score F1 pour les séries est de 0.98, toujours excellent, mais légèrement inférieur à celui des films.

# Conclusion :
L'arbre de décision montre une très bonne performance dans la classification des films et des séries sur Netflix. La durée du contenu est le facteur le plus discriminant pour le modèle, avec une très faible incidence des autres facteurs comme le pays et le classement.
En somme, le modèle a une précision de 100% pour les films et un score F1 globalement élevé pour les séries, avec un léger déclin pour les TV Shows, mais dans une mesure négligeable.Les autres facteurs, comme le pays, n'interviennent que pour des cas très rares, indiquant que leur impact est moindre.
