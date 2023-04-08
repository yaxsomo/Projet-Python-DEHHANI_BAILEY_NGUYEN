## Plateforme de suivi de satellites

<img width="1266" alt="Capture d’écran 2023-04-08 à 21 17 20" src="https://user-images.githubusercontent.com/71334330/230739058-b0e4bc1a-476c-4281-adc4-06a4b23fc327.png">

## Description:
Le projet consiste en la création d'une plateforme de suivi de satellites. Cette plateforme permettra de collecter des données de différents satellites en orbite et de fournir des informations de suivi à des clients en temps réel. La plateforme sera composée d'un SDK pour accéder aux données, d'un ou plusieurs services pour traiter les données, d'une base de données pour stocker les données, d'outils de simulation pour tester les services, d'un tableau de bord pour visualiser les données, et d'une documentation complète pour faciliter la compréhension et la maintenance du projet.

## Fonctionnalités:

Collecte de données de différents satellites en orbite <br>
Traitement de données pour fournir des informations de suivi en temps réel <br>
Stockage de données dans une base de données pour une consultation ultérieure <br>
Outils de simulation pour tester les services
Tableau de bord pour visualiser les données de suivi des satellites

### Utilisateurs : 
 - Administrateur :
      - Accepter ou refuser une mise en orbite
      - Mettre un satellite en orbite
      - Supprimer des orbites
      - Administration de la base de données
      
 - Client : 
      - Faire une demande de mise en orbite
      - Accéder aux données de tous les satellites

## Métriques :

- Données minimales, maximales et moyennes des satellites en temps réel
- Orbites ( Periapsis, Apoapsis, Eccentricité, Inclinaison, Longitude, Position[True Anomaly] )


## Métriques Optionnelles : 

- Disponibilité du service de suivi
- Taux de réussite de stockage des données dans la base de données
- Nombre de requêtes simultanées supportées
- Temps de réponse pour les requêtes de suivi en temps réel
- Efficacité des outils de simulation
- Vitesse des satellites


## API

 Exemple de réponse API : 
 
 ```json
 {
  "satID": {
    "satNAME": "SPACE STATION",
    "launchDate": "2015-07-10",
    "satAPO":  6.00,
    "satECC":  1.00,
    "satINC":  180,
    "satPER":  360,
    "satLONG": 360,
    "satPOS":  360
    }
}
```

## Technologies:

#### Langages de programmation: Python
#### Base de données: JSON
#### Frameworks: Flask

## Livraison:

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
