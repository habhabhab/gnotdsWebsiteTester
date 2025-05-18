@echo off
set /p url="Bitte geben Sie die URL ein: "
website-evidence-collector %url% --overwrite
pause
