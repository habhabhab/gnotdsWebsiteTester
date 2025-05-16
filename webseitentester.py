"""webseitentester

No English docs.

Dieses Skript bietet ein kleines Frontend für die Software
Website Evidence Collector. Es ist nur noch die Eingabe der
Ziel-URL notwendig, z.B. durch copypaste mittels RMB.

Es wird eine funktionierende Installation des Website Evidence
Collectors verlangt. Der WEC kann hier gefunden werden:
https://code.europa.eu/EDPS/website-evidence-collector

Dieses Skript kann als Modul eingebunden werden und bietet
folgende Funktionen:

    * test_website - runs website evidence collector on specified url
    * main - main funtion of the script

<by Hannes Breuer, hannes.breuer@gnotds.de, 2025>
""" 

print("===============================================================================================================================================================\n")
print(" ..|'''.|  '|.   '|'           .   '||''|.    .|'''.|     '|| '||'  '|'         '||                      ||    .                      .                    .   ")
print(".|'     '   |'|   |    ...   .||.   ||   ||   ||..  '      '|. '|.  .'    ....   || ...   ....    ....  ...  .||.    ....  .. ...   .||.    ....   ....  .||.  ")
print("||    ....  | '|. |  .|  '|.  ||    ||    ||   ''|||.       ||  ||  |   .|...||  ||'  || ||. '  .|...||  ||   ||   .|...||  ||  ||   ||   .|...|| ||. '   ||   ")
print("'|.    ||   |   |||  ||   ||  ||    ||    || .     '||       ||| |||    ||       ||    | . '|.. ||       ||   ||   ||       ||  ||   ||   ||      . '|..  ||   ")
print("''|...'|  .|.   '|   '|..|'  '|.' .||...|'  |'....|'         |   |      '|...'  '|...'  |'..|'  '|...' .||.  '|.'  '|...' .||. ||.  '|.'  '|...' |'..|'  '|.'  \n")
print("===============================================================================================================================================================")
print("\n")
print("Willkommen beim GNotDS-internen Tool zum Testen von Webseiten!\n")
print("1. Kopiere die Adresse (Startseite) der Notarwebseite. Beachte: es muss das http:// oder https:// dabei sein!")
print("2. Füge die URL in diesem Fenster durch klicken mit der rechten Maustaste ein.")
print("3. Drücke enter.")
print("4. Magic happens. Warte bis das Skript durchgelaufen ist.")
print("5. Kopiere die Ergebnisdatei, z.B. die inspection.pdf, in einen anderen Ordner oder auf deinen Desktop bevor du einen erneuten Test ausführst. Die Ergebnisse im Zielordner werden bei jedem Test überschrieben.")
print("\n\n")

input("press enter to exit")