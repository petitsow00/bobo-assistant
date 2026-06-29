# BOBO - Script d'installation Windows
# Assistant IA Personnel de Mamadou Sow

Write-Host "=================================================="
Write-Host "  BOBO - Installation Windows"
Write-Host "=================================================="
Write-Host ""

# Vérifier Python
Write-Host "Verification de Python..."
try {
    $pythonVersion = python --version 2>&1
    Write-Host "OK : $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERREUR : Python n'est pas installe." -ForegroundColor Red
    Write-Host "Telechargez-le sur : https://www.python.org/downloads/"
    Write-Host "Cochez 'Add Python to PATH' lors de l'installation !"
    exit 1
}

# Installer les dépendances
Write-Host ""
Write-Host "Installation des dependances..."
pip install anthropic
Write-Host "OK : Dependances installees" -ForegroundColor Green

# Configurer la clé API
Write-Host ""
Write-Host "Configuration de la cle API..."
$apiKey = Read-Host "Entrez votre cle API Anthropic (sk-ant-...)"

if ($apiKey -ne "") {
    [System.Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', $apiKey, 'User')
    $env:ANTHROPIC_API_KEY = $apiKey
    Write-Host "OK : Cle API configuree" -ForegroundColor Green
} else {
    Write-Host "ATTENTION : Pas de cle API configuree" -ForegroundColor Yellow
}

# Créer un raccourci sur le Bureau
Write-Host ""
Write-Host "Creation du raccourci..."
$desktopPath = [Environment]::GetFolderPath("Desktop")
$shortcutPath = Join-Path $desktopPath "BOBO.lnk"
$targetPath = Join-Path $PSScriptRoot "bobo.bat"

$WshShell = New-Object -ComObject WScript.Shell
$shortcut = $WshShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $targetPath
$shortcut.WorkingDirectory = $PSScriptRoot
$shortcut.Description = "BOBO - Assistant IA Personnel"
$shortcut.Save()

Write-Host "OK : Raccourci cree sur le Bureau" -ForegroundColor Green

Write-Host ""
Write-Host "=================================================="
Write-Host "  Installation terminee !"
Write-Host "=================================================="
Write-Host ""
Write-Host "Pour lancer BOBO :"
Write-Host "  - Double-cliquez sur 'BOBO' sur votre Bureau"
Write-Host "  - Ou tapez 'bobo.bat' dans ce dossier"
Write-Host ""
Write-Host "Appuyez sur une touche pour fermer..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
