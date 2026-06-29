@echo off
REM BOBO - Assistant IA Personnel de Mamadou Sow
REM Version Windows

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installe.
    echo Telechargez-le sur : https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Vérifier si la clé API est configurée
if "%ANTHROPIC_API_KEY%"=="" (
    echo.
    echo Cle API Anthropic non trouvee.
    echo.
    echo Pour configurer votre cle API :
    echo 1. Ouvrez PowerShell en administrateur
    echo 2. Tapez : setx ANTHROPIC_API_KEY "votre-cle-api"
    echo 3. Redemarrez ce terminal
    echo.
    pause
    exit /b 1
)

REM Lancer BOBO
python "%~dp0bobo.py"
pause
