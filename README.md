## Plateforme de suivi de satellites

## Description:
Le projet consiste en la création d'une plateforme de suivi de satellites. Cette plateforme permettra de collecter des données de différents satellites en orbite et de fournir des informations de suivi à des clients en temps réel. La plateforme sera composée d'un SDK pour accéder aux données, d'un ou plusieurs services pour traiter les données, d'une base de données pour stocker les données, d'outils de simulation pour tester les services, d'un tableau de bord pour visualiser les données, et d'une documentation complète pour faciliter la compréhension et la maintenance du projet.

## Fonctionnalités:

Collecte de données de différents satellites en orbite
Traitement de données pour fournir des informations de suivi en temps réel
Stockage de données dans une base de données pour une consultation ultérieure
Outils de simulation pour tester les services
Tableau de bord pour visualiser les données de suivi des satellites

### Utilisateurs : 
 - Administrateur :
      - Accepter ou refuser une mise en orbit
      - Mettre un satellite en orbite
      - Supprimer des orbites
      - Administration de la base de données
      
 - Client : 
      - Faire une demande de mise en orbite
      - Accéder aux données de tous les satellites

## Métriques :

- Position des satellites en temps réel
- Orbites
- Périapsis
- Apoapsis


## Métriques Optionnelles : 

- Disponibilité du service de suivi
- Taux de réussite de stockage des données dans la base de données
- Nombre de requêtes simultanées supportées
- Temps de réponse pour les requêtes de suivi en temps réel
- Efficacité des outils de simulation
- Vitesse des satellites

 Exemple de réponse API : 
 
 ```json
 {
  "satID": {
    "satNAME": "SPACE STATION",
    "satLAT": -39.90318514,
    "satLONG": 158.28897924,
    "launchDate": "2015-07-10",
    "satALT": 417.85,
    "satAZ": 254.31,
    "elevation": -69.09,
    "ra": 44.77078138,
    "dec": -43.99279118
    }
}
```

## Technologies:

#### Langages de programmation: Python
#### Base de données: MongoDB
#### Frameworks: Flask

### Livraison:

SDK pour accéder aux données de suivi des satellites
Service de suivi de satellites en temps réel
Base de données pour stocker les données de suivi
Outils de simulation pour tester les services de suivi
Tableau de bord pour visualiser les données de suivi des satellites
Documentation complète du projet, des tests unitaires, des logs, et des simulations réalistes.
Évaluation:

- Découpage et qualité du code
- Documentation du projet
- Tests unitaires
- Logs
- Réalisme des simulations
- Temps de réponse pour accéder aux données
- Disponibilité du service de suivi
- Taux de réussite de stockage des données dans la base de données
- Temps de réponse pour les requêtes de suivi en temps réel
- Nombre de requêtes simultanées supportées

## Credits : 

### Yassine DEHHANI
### Emile BAILEY
### David NGUYEN
