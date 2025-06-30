# Installationshinweise WEC

Die Installationsanleitung für den WEC im offiziellen Repo beschränkt sich auf Linux-Systeme und ist nicht 1:1 auf Windows anwendbar. Hier ist die angepasste Installationsanleitung.

## Abhängigkeiten installieren

#### 1. Auf dem Gerät muss Node.js installiert sein: https://nodejs.org/en/download 
* Bei der Installation darauf achten, dass NPM mit installiert wird (vorausgewählt).
* Bei ```Automatically install the necessary tools. ...``` muss ein Häkchen gesetzt werden.
* Nach dem Durchlaufen des Windows Installers für Node.js öffnet sich eine Powershell für die Installation der zusätzlichen Softwarepackages. Einfach durchklicken.

#### 2. Überprüfen ob die Installation geklappt hat
* im Terminal ```node -v``` und ```npm -v``` eingeben und schauen, ob für beide eine Versionsnummer zurück kommt. Dann hat die Installation geklappt.

## WEC installieren

#### 3. EDPS dem Nodepackage hinzufügen
* im Ordner ```C:\Users\<Username>\``` muss die Datei ```.npmrc``` abgelegt werden.
* Sollte diese Datei noch nicht dort sein, einfach die Datei aus diesem Repo herunterladen.

#### 4. WEC installieren
* folgenden Befehl im Terminal ausführen: 
```bash
npm install --global @EDPS/website-evidence-collector
```
* Zuschauen und staunen.

#### 5. Installation testen
* Nach dem Abschluss der Installation einfach folgenden Befehl in ein Terminal kopieren und mit Enter bestätigen:
```
website-evidence-collector http://www.gnotds.de --overwrite
```
* Danach sollte im Ordner ```C:\Users\<Username>\output``` eine aktuelle Überprüfung unserer Webseite sichtbar sein.

## Unser Skript hinzufügen

#### 6. Unser Skript startklar machen
* Lade die Datei ```run-wec.bat``` aus diesem Repo herunter und lege sie auf dem Desktop ab.

### 7. Testlauf
* Doppelklick auf die ```.bat```-Datei öffnet ein Terminal.
* einfach irgendeine Webseite testen, z.B. einfach diese URL hineinkopieren:
```
https://www.google.de
```
* das Ergebnis wird im Ordner ```\output\``` abgelegt. Der Ordner wird in dem Ordner erzeugt, in dem auch die Datei ```zun-wec``` liegt, also z.B. auf dem Desktop.