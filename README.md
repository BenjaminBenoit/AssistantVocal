# AssistantVocal

## Carnet de produit

#### Sprint 1 (30 Mai - 13 Juin)
* Convertir une commande vocale en texte en utilisant pyaudio et speech_recognition
* Convertir du texte en son en utilisant pyttsx3
* Aller chercher la météo du moment en utilisant scrappy

#### Sprint 2 (14 Juin - 27 Juin)
* Créer une commande pour éteindre l'assistant
* Créer une réponse si commande n'est pas comprise
* Créer une commande pour aller chercher la météo
* Créer une commande pour avoir l'heure dans un pays donné
* Créer une interface graphique avec 2 boutons : Démarrer et Arrêter, pour envoyer des commandes au besoin à l'assistant

#### Sprint 3 (28 Juin - 11 Juillet)
* Travailler sur les éventuels defects / amélioration
* Préparer la présentation à faire en classe
* Si le temps le permet :
  * Créer de nouvelles commandes (ex: garder en mémoire des rendez-vous et prévenir l'utilisateur d'un rendez-vous imminent)
  * Rendre l'assistant 'résistant' aux variations de mots dans la commande par l'implémentation d'un réseau de neurones
  * Rendre l'assistant capable de faire une recherche par lui même en cas de commande inconnue. En cas de bonne réponse, l'assistant pourrait apprendre cette commande

## Set up

* Télécharger et installer Anaconda avec la dernière version de Python (3.6) pour l'OS adéquat https://anaconda.org/anaconda/python
* Install pyaudio library using command line (syntax depend on OS)
* Install pyttsx3 library using command line
* Install speech_recognition library using command line
* Install scrappy library using command line

## Lancer l'application

* Cloner le repo git du projet
* Ouvrir le fichier POC_Assistant.py dans l'IDE Spyder (fais partie du bundle téléchargé avec Anaconda)
* Exécuter le fichier (F5 ou flèche verte)

## Méthodologie Git pour pusher son travail
* télécharger Git bash
* dans git bash, exécuter les commandes suivantes :
  * git add . 
  * git commit -m "Mettre un message explicitant les changements"
  * git pull --rebase
  * git push origin master

