# Système de Détection d'Espaces de Stationnement

## Aperçu du Projet
La gestion des espaces de stationnement dans les zones urbaines est devenue un enjeu majeur, nécessitant des solutions innovantes pour améliorer l’expérience des conducteurs. Ce projet vise à développer un **système de détection des espaces de stationnement en temps réel** en utilisant le modèle **YOLOv8**, capable d’identifier les places disponibles et occupées.

## Fonctionnalités
- **Détection en temps réel** des places de stationnement disponibles et occupées.
- Affichage des informations cruciales sur une **interface de contrôle** :
  - État de la caméra.
  - Nombre de places de stationnement disponibles.
  - Alertes et notifications en temps réel.

En fournissant ces données, notre solution contribue à réduire le temps de recherche de stationnement, optimisant ainsi l'utilisation de l'espace urbain.

## Capture d'écran
Voici un exemple de détection en temps réel des espaces de stationnement :

![Exemple de détection](C:\Users\Asus\Desktop\mesVDs\detection.png)

## Technologies Utilisées
- **cvzone** : pour les outils de traitement d'image.
- **matplotlib** : pour les graphiques et visualisations.
- **opencv-python** : pour le traitement des images et vidéos.
- **requests** : pour les requêtes HTTP et l'intégration des API.
- **torch** : pour le deep learning et l'intégration des modèles YOLOv8.
- **YOLOv8** pour la détection d'objets.

## Améliorations Futures
- Extension du modèle pour gérer des **parkings plus grands**, permettant de détecter les places disponibles et occupées sur plusieurs niveaux ou zones étendues.
- Ajout de fonctionnalités supplémentaires, comme :
  - Réservation de places de stationnement à l'avance.
  - Intégration avec des systèmes de gestion de paiement automatique.
  - Analyse des données pour prévoir les heures de forte affluence et optimiser la gestion du parking.
  - Notifications basées sur la localisation pour guider les conducteurs vers les places disponibles les plus proches.

