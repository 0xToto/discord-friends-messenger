import requests
import time

# Remplacez par votre token utilisateur Discord (NE JAMAIS PARTAGER CE TOKEN)
USER_TOKEN = "TOKEN"
MESSAGE = "MESSAGE"
DELAY = 3  # Délai en secondes entre chaque message (modifiable)

# URL de l'API Discord
API_BASE_URL = "https://discord.com/api/v9"

# En-têtes avec le token utilisateur
HEADERS = {
    "Authorization": USER_TOKEN,
    "Content-Type": "application/json"
}

# Fonction pour obtenir la liste des amis
def get_friends():
    response = requests.get(f"{API_BASE_URL}/users/@me/relationships", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur pour obtenir la liste des amis : {response.status_code}")
        return []

# Fonction pour envoyer un message
def send_message(user_id, message):
    payload = {"content": message}
    response = requests.post(
        f"{API_BASE_URL}/users/@me/channels",
        headers=HEADERS,
        json={"recipient_id": user_id}
    )
    if response.status_code == 200:
        channel_id = response.json()["id"]
        response = requests.post(
            f"{API_BASE_URL}/channels/{channel_id}/messages",
            headers=HEADERS,
            json=payload
        )
        if response.status_code == 200:
            print(f"Message envoyé à l'utilisateur ID : {user_id}")
        else:
            print(f"Erreur en envoyant le message à {user_id} : {response.status_code}")
    else:
        print(f"Erreur en créant un DM avec {user_id} : {response.status_code}")

# Script principal
if __name__ == "__main__":
    friends = get_friends()
    print(f"Vous avez {len(friends)} amis.")
    
    for friend in friends:
        if friend["type"] == 1:  # Type 1 = ami confirmé
            send_message(friend["id"], MESSAGE)
            time.sleep(DELAY)  # Délai entre chaque message
