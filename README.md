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

![Exemple de détection](chemin/vers/capture_ecran.png)

## Technologies Utilisées
- **cvzone==1.5.6** : pour les outils de traitement d'image.
- **matplotlib>=3.9.0** : pour les graphiques et visualisations.
- **opencv-python>=4.8.0** : pour le traitement des images et vidéos.
- **requests>=2.31.0** : pour les requêtes HTTP et l'intégration des API.
- **torch>=2.0.0** : pour le deep learning et l'intégration des modèles YOLOv8.
- **YOLOv8** pour la détection d'objets.

## Améliorations Futures
- Intégration avec des applications mobiles pour des notifications en temps réel.
- Extension du modèle pour gérer des zones de stationnement plus vastes avec plusieurs caméras.
