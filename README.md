# AssistantVocal

## Carnet de produit

#### Sprint 1 (30 Mai - 13 Juin)
* Convertir une commande vocale en texte en utilisant pyaudio et speech_recognition
* Convertir du texte en son en utilisant pyttsx3
* Aller chercher la météo du moment en utilisant Selenium

#### Sprint 2 (14 Juin - 27 Juin)
* Créer une réponse si commande n'est pas comprise
* Créer une commande pour aller chercher la météo à Montréal
* Créer une commande pour avoir l'heure dans une ville donnée
* Créer une interface graphique avec un bouton start pour envoyer des commandes à l'assistant

#### Sprint 3 (28 Juin - 11 Juillet)
* Créer un fichier exécutable windows pour l'application
* Régler les defects
* Nettoyer le code
* Créer une commande pour sauvegarder des rendez-vous
* Créer une commande pour se faire rappeler les rendez-vous
* Créer une commande d'aide
* Créer une commande énumérant toute les commandes existante
* Rajouter une liste des commandes disponible dans l'interface graphique
* Rajouter des paramètres d'application
* Créer une commande permettant de modifier les paramètres de l'application

#### Sprint 4 (12 Juillet - 25 Juillet)
* Préparer la présentation à faire en classe

## Set up

* Télécharger et installer Anaconda avec la dernière version de Python (3.5 ou 3.6)
Lien pour windows : https://conda.io/docs/user-guide/install/windows.html
* Installer PyAudio via Anaconda Prompt https://anaconda.org/anaconda/pyaudio
* Installer pyttsx3 via Anaconda Prompt https://anaconda.org/auto/pyttsx
* Installer speech_recognition via Anaconda Prompt https://anaconda.org/conda-forge/speechrecognition
* Installer Selenium via Anaconda Prompt https://anaconda.org/conda-forge/selenium
* Télécharger la dernière version de chromedriver https://sites.google.com/a/chromium.org/chromedriver/home et la placer dans C:\Program Files (x86)\Chrome

## Lancer l'application avec Spyder

* Cloner le repo git du projet
* Ouvrir le fichier Main.py dans l'IDE Spyder (fais partie du bundle téléchargé avec Anaconda)
* Exécuter le fichier (F5 ou flèche verte) : l'interface va apparaître dans une fenêtre séparée
* Cliquer Start pour donner une commande
* Pour le moment, il faut attendre que la phrase 'Say something!' apparaisse dans la console de Spyder pour pouvoir dire quelque chose. Il faut également donner la commande rapidement. La commande comprise pour le moment est weather

## Lancer l'application avec l'exécutable
* Aller dans le fichier dist
* Double cliquer sur Main.exe (cet exécutable est seulement compatible Windows 10)

## Méthodologie Git pour pusher son travail
* télécharger Git bash
* dans git bash, exécuter les commandes suivantes :
  * git add . 
  * git commit -m "Mettre un message explicitant les changements"
  * git pull --rebase
  * git push origin master
  
## Méthodologie pour créer l'exécutable python de l'application
* Need to install pyinstaller in Anaconda Prompt : pip install pyinstaller
* In the dist folder at the root of the app, add the chromedriver.exec file and the app_properties and meeting_data files
* Also add to manually add in the dist folder several drivers (see platforms, sqldrivers and pyttsx3 folders) 
* Still in Anaconda prompt, create the exe file : pyinstaller --onefile <script_entry_point>.py
	* In our case, the entry point of the application is Main.py.
	* All the dependencies starting from Main.py will be added to the exec file.

### Possible issues when creating the exec file
* Enable debug option to investigate the issue. Running the pyinstaller command will create a <script_entry_point>.spec file
	at the root of the project. Edit this file to put debug=True
* Issue with pyttsx3. See workaround here : https://github.com/pyinstaller/pyinstaller/issues/3268. In short, the workaround is :
	* Add a pyttsx3 hook at the root of the project
	* Commented out all the content in the C:\Users\Admin\Anaconda3\Lib\site-packages\PyInstaller\loader\rthooks\py_rth_win32comgenpy file
	* Launch the pyinstaller using the hook : pyinstaller --onefile --additional-hooks-dir=. Main.py

