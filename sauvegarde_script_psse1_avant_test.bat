@echo off
:: Sauvegarder une copie du script passe1 avant test
set SRC=C:\Dev\PPL-formulaires\scripts\passe1_docx_lin_to_txt.py
set DST=C:\Dev\PPL-formulaires\scripts\_sauvegardes

:: Créer le dossier de sauvegarde s'il n'existe pas
if not exist "%DST%" mkdir "%DST%"

:: Ajouter horodatage pour nom unique
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set DATETIME=%%i

:: Construire le nom de fichier final
set FILENAME=passe1_docx_lin_to_txt_%DATETIME%.py

copy "%SRC%" "%DST%\%FILENAME%"

echo ✅ Script sauvegardé : %DST%\%FILENAME%
pause
