#!/usr/bin/env python3
"""
BOBO - Assistant IA Personnel de Mamadou Sow
Propulsé par Claude (Anthropic)
"""

import anthropic
import os

# Configuration
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

if not ANTHROPIC_API_KEY:
    print("Erreur : Clé API Anthropic non trouvée.")
    print("Ajoutez-la avec : export ANTHROPIC_API_KEY='votre-clé'")
    exit(1)

# Prompt système de BOBO
SYSTEM_PROMPT = """Tu es BOBO, l'assistant IA personnel de Mamadou Sow.

## Identité
- Tu t'appelles BOBO.
- Tu réponds toujours en français, sauf si l'utilisateur demande une autre langue.
- Tu t'adresses à l'utilisateur de manière professionnelle, simple et respectueuse.
- Tu expliques les notions complexes avec des exemples concrets.

## Ton rôle
Tu aides Mamadou dans :
- le développement logiciel
- Python, JavaScript, HTML, CSS et SQL
- VS Code et Terminal macOS
- Git et GitHub
- WordPress
- l'intelligence artificielle
- Zapier, Make, n8n et les automatisations
- Firebase, Supabase et les bases de données
- Electron
- Flutter
- la cybersécurité défensive
- l'administration système
- les API
- les projets professionnels

## Fonctionnement
Avant de répondre :
1. Comprends précisément la demande.
2. Choisis la meilleure solution.
3. Donne une réponse claire.
4. Propose ensuite une amélioration si elle est utile.

## Développement
Quand Mamadou code :
- analyse les erreurs
- explique leur cause
- propose une correction
- génère un code propre et commenté
- respecte les bonnes pratiques

## Assistance Terminal
Quand Mamadou travaille dans le terminal :
- explique chaque commande avant qu'elle soit exécutée
- n'utilise jamais de commande destructive sans confirmation
- indique toujours le résultat attendu

## Cybersécurité
Tu aides uniquement pour :
- la sécurité défensive
- les audits autorisés
- la protection des systèmes
- les bonnes pratiques de sécurité
Tu refuses toute demande visant à attaquer un système sans autorisation.

## Style
Toujours :
- précis
- structuré
- pédagogique
- efficace
- patient

Si une information est inconnue, indique-le clairement au lieu d'inventer une réponse.

## Objectif principal
Ton objectif est d'aider Mamadou à créer des logiciels, automatiser ses tâches, apprendre la programmation et développer ses projets jusqu'à leur mise en production.
"""

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_header():
    print("=" * 50)
    print("  BOBO - Assistant IA Personnel de Mamadou Sow")
    print("  Propulsé par Claude (Anthropic)")
    print("=" * 50)
    print("  Tapez 'quit' ou 'q' pour quitter")
    print("  Tapez 'clear' pour effacer l'écran")
    print("=" * 50)
    print()

def main():
    clear_screen()
    print_header()

    # Initialiser le client
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        print("Vérifiez votre clé API Anthropic.")
        return

    # Historique de conversation
    history = []

    print("BOBO: Bonjour Mamadou ! Je suis BOBO, ton assistant personnel.")
    print("      Propulsé par Claude. Comment puis-je t'aider aujourd'hui ?")
    print()

    while True:
        try:
            # Lire l'entrée utilisateur
            user_input = input("Vous: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['quit', 'q', 'exit', 'quitter']:
                print("\nBOBO: Au revoir Mamadou ! À bientôt !")
                break

            if user_input.lower() == 'clear':
                clear_screen()
                print_header()
                continue

            # Ajouter le message à l'historique
            history.append({
                "role": "user",
                "content": user_input
            })

            # Envoyer le message à Claude
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",  # Modèle Claude Haiku 4.5 (économique)
                max_tokens=2048,
                system=SYSTEM_PROMPT,
                messages=history
            )

            # Récupérer la réponse
            assistant_message = response.content[0].text

            # Ajouter la réponse à l'historique
            history.append({
                "role": "assistant",
                "content": assistant_message
            })

            print()
            print(f"BOBO: {assistant_message}")
            print()

        except KeyboardInterrupt:
            print("\n\nBOBO: Au revoir Mamadou ! À bientôt !")
            break
        except anthropic.APIError as e:
            print(f"\nErreur API: {e}")
            print("Vérifiez votre crédit sur console.anthropic.com\n")
        except Exception as e:
            print(f"\nErreur: {e}")
            print("Réessayez votre question.\n")

if __name__ == "__main__":
    main()
