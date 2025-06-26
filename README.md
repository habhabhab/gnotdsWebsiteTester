# gnotdsWebsiteTester

Unser Tool zum Testen von Webseiten. Es bietet ein zusätzliches Frontend für den Website Evidence Collector. Diese Dokumentation liefert zusätzöiche Hinweise zur Installation und zum Betrieb.

## Hinweise für den Nutzer ##

* Eigentlich erklärt unser Skript alle Einzelschritte. Aber es sollte trotzdem erwähnt sein, dass der Webseite Evidence Collector die Ergebnisse immer im selben Ordner `\output` ablegt. **Lasse ich das Skript erneut laufen, werden alte Ergebnisse überschrieben.** Möchte man also mehrere Webseiten nacheinander prüfen, muss man die Ergebnisse (z.B. die Datei `inspection.pdf`) immer erst manuell aus dem Ordner kopieren.
* das bedeutet auch, dass zuerst alte Testdateien zu sehen sind, wenn der `\output`-Ordner von unserem Webseitentestskript göffnet wird. **Bevor du Dateien öffnest also erst warten bis der WEC durchgelaufen ist und sich das Terminal-Fenster geschlossen hat!**
* Sollten Fehler beim Durchlaufen des WEC geworfen werden, kann man sich die gesamte Konsolenausgabe nach Durchlaufen des Programms anzeigen lassen, da im `\output`-Ordner die Datei `inspection.log` angelegt wird.

# Installationsanleitung und Administration

## Website Evidece Collector herunterladen
Damit dieses Skript auf den Website Evidence Collector zugreifen kann, muss er natürlich auf dem PC installiert sein. Es gibt mehrere Stellen, um den Website Evidence Collector herunterzuladen:

* Die zentrale Stelle (zu bevorzugende) ist das [Öffentliche Git auf code.europa.eu](https://code.europa.eu/EDPS/website-evidence-collector). Hier wird man immer die tagesaktuelle Version der Software finden. Hier findet sich außerdem die ausführliche Installationsanleitung für alle notwendigen Softwarepakete, z.B. nodejs.

* Die ["offizielle" Internetseite des Programms](https://www.edps.europa.eu/edps-inspection-software_en) beim Europäischen Datenschutzbeauftragten ist auf Englisch und hat immer nur die aktuellste Version der Software hinter dem Downloadbutton. Als Installationsanleitung wird auf die code.europa.eu-Seite verlinkt.

* Alternativ kann die Software in unterschiedlichen Versionen von der Webseite [Interoperable Europe](https://interoperable-europe.ec.europa.eu/collection/free-and-open-source-software/solution/website-evidence-collector) herunter geladen werden. Sehr hilfreich, wenn man eine ganz bestimmte Version haben möchte.

⚠️ **Achtung:** Google findet auch immer ein [öffentliches GitHub-Repository](https://github.com/EU-EDPS/website-evidence-collector). Dieses ist veraltet! Das Projekt ist auf das EU-eigene GitLab (erster Link oben) umgezogen. Im GitHub findet man nur eine veraltete Version mit Stand Juni 2024. **Diese Quelle also nicht verwenden!**

## Installation unseres Skriptes

1. Website Evidence Collector nach Anleitung installieren. Dabei auch alle notwendigen Dependencies installieren. Diese sind alle in der Installationsanleitung im EU-Git genannt.

2. einen Testlauf starten. Dafür folgenden Code kopieren:   
    ```
    website-evidence-collector https://www.google.de --overwrite
    ```
    und ein Terminal öffnen (`Win`-Taste und dann einfach `cmd` eingeben - das erste Suchergebnis sollte `Ausführen...` sein). Den kopierten Code dort durch Drücken der rechten Maustaste einfügen und einmal `enter` drücken. Man kann schauen wie alles durchläuft. 

3. Sollte alles ohne Fehlermeldung geklappt haben, einfach noch manuell das Ergebnis sichttesten: Öffne den Windows Explorer und navigiere zum Ordner `C:\Users\{username}\output`. Dort findest du die Testergebnisse. Öffne die Datei `inspection.pdf`. Dort solltest du nun die Ergebnisse für google.de mit einem aktuellen Zeitstempel finden.

4. Lade die Skript-Datei `run-wec.bat` aus diesem Repository herunter und lege sie auf dem Desktop ab.

5. Der User kann das Skript jetzt jederzeit durch einfaches Doppelklicken auf die Skriptdatei auf seinem Desktop starten.

6. Einfach einmal testen, indem du den Anweisungen im Terminal folgst. Das Ergebnis des Webseitentests wird in dem Ordner `\output` abgelegt, der immer an dem Ort angelegt wird, an dem auch die .bat liegt. Liegt die Skriptdatei also auf dem Desktop, wird der Ordner für die Ergebnisse auch am Desktop erzeugt. Es sollte sich aber beim Durchlaufen des Skripts ein Explorerfenster für die Ergebnisse öffnen.

## Planned Features ##

* Derzeit sorgt der Website Evidence Collector noch dafür, dass das Terminal-Fenster nach Durchlauf des WEC geschlossen wird. Irgendwann habe ich hoffentlich mal Zeit, dem ganzen auf den Grund zu gehen. Eigentlich wünsche ich mir, dass das Fenster noch geöffnet bleibt.
* Der Befehl zum Öffnen des Output-Ordners wird nicht ausgeführt, wenn der Befehl am Ende des Skripts steht, da das Terminal-Fenster sofort nach Abschluss des WEC geschlossen wird. Dirty workaround ist bisher, dass der Ziel-Ordner erst geöffnet wird und danach das Programm startet.
* Wichtigstes Feature: ASCII-Art
* Weil Windows doof ist musste das Ganze erstmal als Batch-Datei erstellt werden. Zukünfitg möchte ich ein Python-Programm schreiben, das ein wirkliches Frontend anbietet
* Parameter an WEC mitgeben, sodass alte Ergebnisse nicht mehr überschrieben werden.

