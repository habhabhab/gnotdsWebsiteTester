@echo off

::<by Hannes Breuer, GNotDS, hannes.breuer@gnotds.de, 2025>

::Dieses Skript öffnet den Website Evidence Collector und lässt ihn auf eine abgefragte URL starten
::Website Evidence Collector muss extra installiert werden: https://code.europa.eu/EDPS/website-evidence-collector

::color 17
::Farbschema angepasst

@echo WILLIKOMMEN BEI UNSEREM WEBSEITEN TESTTOOL
@echo Um eine Webseite zu testen, einfach die URL der Webseite kopieren.
@echo Beachte: das "http://" oder "https://" muss enthalten sein.
@echo Beispiel: https://www.beispiel-notar.de
set /p url="Drücke jetzt bitte ein mal die rechte Maustaste, um die URL einzufügen und bestätige deine Einfabe mit ENTER: "

website-evidence-collector %url% --overwrite

pause

%SystemRoot%\explorer.exe ".\output"
pause
