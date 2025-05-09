@echo off
:: Sauvegarde du dossier C:\Dev\PPL-formulaires vers OneDrive avec horodatage

set SRC=C:\Dev\PPL-formulaires
set DST=C:\Users\jacqu\OneDrive\90 dev\sauvegardes_PPL

:: Générer un horodatage AAAA-MM-JJ_HH-MM
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd_HH-mm"') do set DATETIME=%%i

set DEST_DIR=%DST%\%DATETIME%
echo 🔄 Sauvegarde de "%SRC%" vers "%DEST_DIR%"
xcopy "%SRC%" "%DEST_DIR%" /E /I /Y

echo ✅ Sauvegarde terminée dans : %DEST_DIR%
pause
