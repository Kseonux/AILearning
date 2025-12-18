
import requests

baseurl = "https://pokeapi.co/api/v2/"

def get_pok_info(name):
    url = f"{baseurl}/pokemon/{name}"
    bro = requests.get(url)

    if bro.status_code == 200 :
        print ("Data diterima bos")
    else :
        print (f"Data gagal diterima boy, error {bro.status_codes}")

pokemonah_name = "ditto"
data = get_pok_info(pokemonah_name)

print (data)






























