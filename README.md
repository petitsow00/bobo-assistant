# BOBO - Assistant IA Personnel

BOBO est un assistant IA personnel créé pour Mamadou Sow. Il aide dans tous les domaines du développement logiciel et de l'automatisation.

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

| Commande | Action |
|----------|--------|
| `quit` ou `q` | Quitter BOBO |
| `clear` | Effacer l'écran |

## Auteur

Mamadou Bobo Sow - [@petitsow00](https://github.com/petitsow00)

## Licence

MIT
