# AssistantVocal

## Carnet de produit

#### Sprint 1 (30 Mai - 13 Juin)
* Convertir une commande vocale en texte en utilisant pyaudio et speech_recognition
* Convertir du texte en son en utilisant pyttsx3
* Aller chercher la météo du moment en utilisant Selenium

#### Sprint 2 (14 Juin - 27 Juin)
* Créer une réponse si commande n'est pas comprise
* Créer une commande pour aller chercher la météo pour une ville donnée
* Créer une commande pour avoir l'heure dans un pays donné
* Créer une interface graphique avec 2 boutons : Démarrer et Arrêter, pour envoyer des commandes au besoin à l'assistant

#### Sprint 3 (28 Juin - 11 Juillet)
* Travailler sur les éventuels defects / amélioration / refactorisation
* Préparer la présentation à faire en classe
* Si le temps le permet :
  * Créer de nouvelles commandes (ex: garder en mémoire des rendez-vous et prévenir l'utilisateur d'un rendez-vous imminent)
  * Rendre l'assistant 'résistant' aux variations de mots dans la commande par l'implémentation d'un réseau de neurones
  * Rendre l'assistant capable de faire une recherche par lui même en cas de commande inconnue. En cas de bonne réponse, l'assistant pourrait apprendre cette commande
  * Transformer l'application en une application Android

## Set up

* Télécharger et installer Anaconda avec la dernière version de Python (3.5 ou 3.6)
Lien pour windows : https://conda.io/docs/user-guide/install/windows.html
* Installer PyAudio via Anaconda Prompt https://anaconda.org/anaconda/pyaudio
* Installer pyttsx3 via Anaconda Prompt https://anaconda.org/auto/pyttsx
* Installer speech_recognition via Anaconda Prompt https://anaconda.org/conda-forge/speechrecognition
* Installer Selenium via Anaconda Prompt https://anaconda.org/conda-forge/selenium
* Télécharger la dernière version de chromedriver https://sites.google.com/a/chromium.org/chromedriver/home et la placer dans C:\Program Files (x86)\Chrome
TODO : quand le temps le permettra, faire en sorte au moment de bootstrap l'application, de télécharger le chromedriver et de le placer dans le dossier voulu si jamais il n'est pas déjà installé


## Lancer l'application

* Cloner le repo git du projet
* Ouvrir le fichier Main.py dans l'IDE Spyder (fais partie du bundle téléchargé avec Anaconda)
* Exécuter le fichier (F5 ou flèche verte) : l'interface va apparaître dans une fenêtre séparée
* Cliquer Start pour donner une commande
* Pour le moment, il faut attendre que la phrase 'Say something!' apparaisse dans la console de Spyder pour pouvoir dire quelque chose. Il faut également donner la commande rapidement. La commande comprise pour le moment est weather

## Méthodologie Git pour pusher son travail
* télécharger Git bash
* dans git bash, exécuter les commandes suivantes :
  * git add . 
  * git commit -m "Mettre un message explicitant les changements"
  * git pull --rebase
  * git push origin master

