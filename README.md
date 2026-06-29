# BOBO - Assistant IA Personnel

BOBO est un assistant IA personnel créé pour Mamadou Sow. Propulsé par Claude (Anthropic), il aide dans tous les domaines du développement logiciel et de l'automatisation.

## Langages supportés

| Langage | Support |
|---------|---------|
| Python | Oui |
| JavaScript | Oui |
| HTML/CSS | Oui |
| SQL | Oui |
| Dart (Flutter) | Oui |

## Technologies supportées

| Catégorie | Technologies |
|-----------|--------------|
| **Frameworks** | Flutter, Electron |
| **CMS** | WordPress |
| **Bases de données** | Firebase, Supabase, SQL |
| **Automatisation** | Zapier, Make, n8n |
| **DevOps** | Git, GitHub, Terminal |
| **Sécurité** | Cybersécurité défensive |
| **API** | REST, GraphQL |

## Ce que BOBO peut faire

- Écrire et corriger du code dans plusieurs langages
- Expliquer des concepts de programmation simplement
- Aider avec les commandes Terminal
- Créer des automatisations
- Configurer des bases de données
- Conseiller sur la sécurité
- Gérer des projets Git/GitHub
- Développer des applications mobiles (Flutter)
- Créer des applications desktop (Electron)

---

## Installation Windows

### Prérequis

1. **Python 3.12+** : [python.org/downloads](https://www.python.org/downloads/)
   - Cochez "Add Python to PATH" lors de l'installation
2. **Clé API Anthropic** : [console.anthropic.com](https://console.anthropic.com)

### Installation automatique

1. Téléchargez ce projet (Code > Download ZIP)
2. Extrayez le dossier
3. Clic droit sur `install-windows.ps1` > "Exécuter avec PowerShell"
4. Suivez les instructions

### Installation manuelle

1. Ouvrez PowerShell et installez les dépendances :
```powershell
pip install anthropic
```

2. Configurez votre clé API :
```powershell
setx ANTHROPIC_API_KEY "sk-ant-votre-cle-api"
```

3. Redémarrez PowerShell

### Utilisation (Windows)

Double-cliquez sur `bobo.bat` ou tapez dans PowerShell :
```powershell
python bobo.py
```

---

## Installation macOS

### Prérequis

- Python 3.12+
- Clé API Anthropic : [console.anthropic.com](https://console.anthropic.com)

### Installation

1. Installez les dépendances :
```bash
pip3 install anthropic
```

2. Configurez votre clé API dans `~/.zshrc` :
```bash
export ANTHROPIC_API_KEY="sk-ant-votre-cle-api"
```

3. Rechargez le terminal :
```bash
source ~/.zshrc
```

### Utilisation (macOS)

```bash
python3 bobo.py
```

Ou créez un alias dans `~/.zshrc` :
```bash
alias bobo="python3 ~/projets/bobo-assistant/bobo.py"
```

Puis lancez :
```bash
bobo
```

---

## Installation Linux

Suivez les mêmes étapes que macOS, en remplaçant `~/.zshrc` par `~/.bashrc` si nécessaire.

---

## Commandes

| Commande | Action |
|----------|--------|
| `quit` ou `q` | Quitter BOBO |
| `clear` | Effacer l'écran |

## Auteur

Mamadou Bobo Sow - [@petitsow00](https://github.com/petitsow00)

## Licence

MIT
