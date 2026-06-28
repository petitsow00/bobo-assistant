# BOBO - Assistant IA Personnel

BOBO est un assistant IA personnel créé pour Mamadou Sow.

## Fonctionnalités

- Aide au développement logiciel
- Support pour Python, JavaScript, HTML, CSS, SQL
- Assistance pour VS Code et Terminal macOS
- Aide avec Git et GitHub
- Support WordPress
- Aide en intelligence artificielle
- Automatisations (Zapier, Make, n8n)
- Bases de données (Firebase, Supabase)
- Electron et Flutter
- Cybersécurité défensive
- Administration système
- Gestion des API

## Installation

### Prérequis

- Python 3.12+
- Une clé API Gemini (gratuite sur [aistudio.google.com](https://aistudio.google.com/apikey))

### Installation des dépendances

```bash
pip3 install google-genai
```

### Configuration

Ajoutez votre clé API Gemini dans votre fichier `~/.zshrc` :

```bash
export GEMINI_API_KEY="votre-clé-api"
```

## Utilisation

```bash
python3 bobo.py
```

Ou ajoutez un alias dans `~/.zshrc` :

```bash
alias bobo="python3 ~/projets/bobo-assistant/bobo.py"
```

Puis lancez simplement :

```bash
bobo
```

## Commandes

- `quit` ou `q` : Quitter BOBO
- `clear` : Effacer l'écran

## Auteur

Mamadou Bobo Sow - [@petisow00](https://github.com/petisow00)

## Licence

MIT
