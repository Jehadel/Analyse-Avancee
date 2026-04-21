# Modalités d’évaluation

Enseignant : Jean Delpech

Cours : Analyse de données avancée

Année scolaire : 2025/2026

Dernière mise à jour : avril 2026

------

L’évaluation va consister en trois notes :

- une évaluation du rendu (données : Instacart) de votre travail personnel le lundi 20 avril 2026 matin(coef. 0,25)
- une co-évaluation entre camarade de votre « répétition générale » de la présentation de votre mini-projet le jeudi 23 avril après-midi (coef 0,25)
- un mini-projet qui met en œuvre les techniques vues en cours le vendredi 24 avril matin (coef. 1)

## Mini-projet

Dans le cours vous avez vu les techniques fondamentales suivantes en data science :

- créer des figures et des dashboards à l’aide des outils libre Metabase et Superset
- création d’un environnement et pipeline d’analyse de données (Docker, base PostgreSQL, scripts python)
- rappel théorique des modèles vus dans le cours EDA

### Consigne

Vous êtes data analyst dans une entreprise brésilienne qui offre un service pour le commerce en ligne : Olist.

Votre manager [vous fournit un ensemble de données](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (anonymisées) sous la forme d’un ensemble de fichiers .csv. Ces données couvrent l’activité de l’entreprise sur 2 ans (2016 à 2018). Il vous demande de créer, pour la fin de la semaine, un dashboard à destination des équipe commerciales, qui doit leur permettre de suivre la performance des ventes en ligne. Charge à vous :

- de définir les indicateurs clés à indiquer
- de proposer une ou des analyses qui permettent de guider l’équipe commerciale sur les points à améliorer. Par exemple : quelles sont les variables qui impactent la satisfaction client, dans quelle mesure (p. ex. « x1, x2 et x3 impactent la satisfaction client, quand x1 augmente de 1 alors les chances d’obtenir 5 étoiles augmentent de …) ? Idem concernant un modèle concernant les délais de livraison par exemple, out tout autre indicateur. À vous de choisir en fonction de ce qui vous semble pertinent et exploitable dans les données fournies.
- Vous devrez bien sûr justifier vos choix et vos affirmation qui doivent être le fruit d’une analyse statistique rigoureuse. Ces analyses seront des régressions linéaires ou logistique.

Vendredi vous présenterez le résultat de votre travail en séminaire d’équipe.

### Livrable

- Une présentation de 10mn (+ 5mn de questions), destinée à vos collègues data analysts comme vous afin de défendre votre projet de dashboard et expliquant les analyses que vous avez mené, votre angle d’attaque, etc.
- Une démo de dashboard (sous Metabase ou Superset, avec des données dans une base PostgreSQL) destiné lui à vos collègues de l’équipe commerciale. Il devra montrer des indicateurs clés, des dataviz éclairantes, et aussi une présentation de vos modèles pour guider la décision.
- La grille d’évaluation de ses camarades : jeudi après-midi vous soumettrez votre présentation et démo à vos camarades, qui vous feront des retours, afin de corriger le tir pour le vendredi !

### Critère d’évaluation

La grille d’évaluation comprend les dimensions suivantes :

- qualité de la présentation (clarté, gestion du temps, plan, aisance orale)
- qualité du dashboard: fonctionne correctement, qualité du layout, pertinence des indicateurs et des dataviz, clarté et concision du texte
- qualité des analyses : robustesse des conclusions, interprétation, respect de la méthode (test, conditions d’application, adéquation des modèles choisis)
- compréhension : capacité à expliquer clairement et à démontrer l’assimilation de la théorie
- originalité/créativité dans l’approche du problème et des données