# Discord Friends Messenger

Un script Python pour envoyer un message prédéfini à tous vos amis Discord.

⚠️ **Avertissement important**  
Ce script utilise un token utilisateur Discord pour interagir avec l'API. 
L'utilisation de ce script peut violer les [conditions d'utilisation de Discord](https://discord.com/terms) 
et entraîner la suspension de votre compte. **Utilisez-le à vos risques et périls.**

---

## Fonctionnalités

- Envoie un message personnalisé à tous vos amis, qu'ils soient en ligne ou non.
- Ajout d'un délai configurable entre chaque message pour simuler un comportement humain et ainsi, éviter de se faire bannir.

---

## Prérequis

1. **Python 3.x** installé sur votre machine. [Téléchargez ici](https://www.python.org/downloads/).
2. Les bibliothèques suivantes (installables via `pip`) :
   - `requests`

---

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/0xToto/discord-friends-messenger.git
   cd discord-friends-messenger

2. Utilisation :
    > Modifier le Token (ligne 5) et le message (ligne 6)
    ```bash
    python3 send_message.py