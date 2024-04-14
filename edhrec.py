import re
import requests


def edhrecd_name(name):
    # scryfall uses // to label two named cards. The first one is what we'll use with
    if "//" in name:
        name = name.split(" // ")[0]
    name = name.lower()
    name = name.replace(" ", "-")
    name = re.sub("[^a-zA-Z/-]+", "", name)
    return name


def edhrec_json(name):
    edh_name = edhrecd_name(name)
    try:
        json = requests.get(
            "https://json.edhrec.com/pages/commanders/" + edh_name + ".json"
        ).json()["cardlist"]
        high_synergy_cards = [d for d in json if d["synergy"] > 0.60]
        return high_synergy_cards
    except:
        return False
