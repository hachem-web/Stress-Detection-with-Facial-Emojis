# Projet d'apprentissage automatique - README

Bienvenue dans le référentiel du projet **Détection du stress à l'aide du Machine Learning** ! Dans ce projet, nous explorons le domaine de l'apprentissage automatique pour relever le défi de la détection du stress provenant de diverses sources.
# Projet d'apprentissage automatique - README

Bienvenue dans le référentiel du projet Détection du stress à l'aide du Machine Learning ! Dans ce projet, nous explorons le domaine de l'apprentissage automatique pour relever le défi de la détection du stress provenant de diverses sources.

## Dépendances

1. **Installez Python** :
    - Téléchargez et installez la dernière version de Python depuis [python.org](https://www.python.org/downloads/).
    - Lors de l'installation, cochez l'option permettant d'ajouter Python au PATH de votre système.

2. **Conditions préalables**
    Vous aurez besoin des logiciels et bibliothèques suivants installés pour exécuter ce projet :
    - Python 3.x
    - Flask
    - TensorFlow
    - Numpy
## Vous pouvez installer les bibliothèques Python nécessaires en utilisant pip :
   
pip install Flask tensorflow numpy

##Exécution de l'application Flask:
Pour exécuter l'application Flask, utilisez la commande suivante :

python main.py

Ouvrez un navigateur web et visitez http://localhost:5000/ pour accéder à l'outil de détection du stress.

### Données
L'ensemble de données utilisé pour ce projet provient de Kaggle. Pour acquérir et prétraiter les données, procédez comme suit :

Accédez à la page de l'ensemble de données Kaggle https://www.kaggle.com/datasets/janithukwattage/stress-faces-dataset.

Si vous n'avez pas de compte Kaggle, vous devrez en créer un.

Une fois connecté, cliquez sur le bouton « Télécharger » sur la page de l'ensemble de données pour télécharger les fichiers de l'ensemble de données.

Extrayez les fichiers téléchargés dans un répertoire de votre choix.

Prétraitez les données en suivant les instructions fournies dans le notebook data_preprocessing.ipynb situé dans le répertoire data de ce référentiel.

Veuillez noter qu'en raison de la confidentialité des données et des restrictions de licence, nous ne pouvons pas fournir l'ensemble de données directement dans ce référentiel.

#**Des modèles**
#Création et évaluation du modèle CNN
Nous avons implémenté un modèle de réseau neuronal convolutif (CNN) pour la détection du stress. Voici un aperçu général des étapes que nous avons suivies pour créer et évaluer le modèle :

#Préparation des données :
 Nous avons initialisé le générateur de données à l'aide de ImageDataGenerator de TensorFlow, ce qui nous a permis d'effectuer une augmentation des données pour améliorer la généralisation du modèle.

# Architecture CNN :
 Nous avons conçu l'architecture CNN pour la détection du stress. Cette architecture se compose de couches convolutives pour l'extraction de fonctionnalités, suivies de couches entièrement connectées pour la classification. Nous avons ajusté le nombre de couches, de filtres et la taille du noyau pour atteindre un équilibre entre complexité du modèle et performances.

# Compilation de modèles :
 Nous avons compilé le modèle à l'aide d'une fonction de perte et d'un optimiseur appropriés. Cette étape est cruciale pour entraîner efficacement le modèle.

#Formation du modèle :
 Nous avons entraîné le modèle à l'aide de l'ensemble de données de formation et surveillé ses performances sur l'ensemble de validation. L’objectif était de minimiser la perte et de maximiser la précision.

#Évaluation : 
Après la formation, nous avons évalué le modèle sur l'ensemble de données de test pour évaluer ses performances sur des données invisibles. Les métriques que nous avons obtenues étaient les suivantes :

Perte : 0,6236
Précision : 0,6434
Augmentation des données
L'augmentation des données est une technique puissante pour augmenter artificiellement la taille de l'ensemble de données d'entraînement en appliquant diverses transformations aux images originales. Cela aide le modèle à mieux généraliser les données invisibles.

Couche d'augmentation des données : Nous avons reconstruit l'architecture du modèle avec une couche d'augmentation des données à l'aide de « ImageDataGenerator » de TensorFlow. Cette couche a appliqué des transformations aléatoires telles que la rotation, le zoom et le retournement des images pendant l'entraînement.

#Recyclage :
 Nous avons recyclé le modèle à l'aide de l'ensemble de données augmenté et observé des améliorations dans ses performances et sa généralisation.

Pour une implémentation plus détaillée et des exemples de code, reportez-vous au répertoire « models » dans ce référentiel.

Le modèle entraîné est enregistré dans le répertoire « EmotionDetector_2 » en tant qu'actifs.


Résultats
Nos modèles ont montré des résultats prometteurs dans la détection des niveaux de stress. Après une formation sur l'ensemble de données et une évaluation sur l'ensemble de test, nous avons obtenu les métriques suivantes :

Perte : 0,6236
Précision : 0,6434
Ces mesures indiquent que notre modèle apprend à distinguer efficacement les modèles de stress.

Résultat de la classification d'une image unique
Nous avons testé notre modèle entraîné sur une seule image de dimensions 48x48 pixels. Voici les détails du test et de la prédiction :

Dimensions de l'image : (1, 48, 48, 3)
Prédiction : Stress
Confiance : 70,77%
La prédiction du modèle suggère que l'image donnée appartient très probablement à la catégorie « stress » avec un degré de confiance de 70,77 %.

Cela démontre la capacité du modèle à faire des prédictions sur des instances individuelles et à fournir un aperçu de l'état émotionnel véhiculé par l'image.

#Utilisation
Téléchargez une image que vous souhaitez analyser pour le stress.
Cliquez sur le bouton "Soumettre".
L'outil traitera l'image et affichera le résultat de la




