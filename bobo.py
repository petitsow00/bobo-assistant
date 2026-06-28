#!/usr/bin/env python3
"""
BOBO - Assistant IA Personnel de Mamadou Sow
"""

from google import genai
from google.genai import types
import os

# Configuration
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Erreur : Clé API Gemini non trouvée.")
    print("Ajoutez-la avec : export GEMINI_API_KEY='votre-clé'")
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
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        print("Vérifiez votre clé API Gemini.")
        return

    # Historique de conversation
    history = []

    print("BOBO: Bonjour Mamadou ! Je suis BOBO, ton assistant personnel.")
    print("      Comment puis-je t'aider aujourd'hui ?")
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
            history.append(types.Content(
                role="user",
                parts=[types.Part(text=user_input)]
            ))

            # Envoyer le message à Gemini
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=history,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.7,
                    max_output_tokens=2048,
                )
            )

            # Récupérer la réponse
            assistant_message = response.text

            # Ajouter la réponse à l'historique
            history.append(types.Content(
                role="model",
                parts=[types.Part(text=assistant_message)]
            ))

            print()
            print(f"BOBO: {assistant_message}")
            print()

        except KeyboardInterrupt:
            print("\n\nBOBO: Au revoir Mamadou ! À bientôt !")
            break
        except Exception as e:
            error_msg = str(e)
            if "quota" in error_msg.lower() or "429" in error_msg:
                print("\n⚠️  Limite API atteinte. Attendez quelques secondes et réessayez.")
                print("    Ou créez une nouvelle clé sur: https://aistudio.google.com/apikey\n")
            else:
                print(f"\nErreur: {e}")
                print("Réessayez votre question.\n")

if __name__ == "__main__":
    main()
