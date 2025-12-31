import requests 


try :
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    r.raise_for_status()  # Raise an error for HTTP errors
    j = r.json()
    print(f"{j['setup']} - {j['punchline']}")
except requests.RequestException as e:
    print(f"error cak {e}")























