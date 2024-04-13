import constants
import json
import pickle
import requests
import shutil
from pathlib import Path


def latest_bulk_uri():
    bulk_list = requests.get("https://api.scryfall.com/bulk-data").json()["data"]
    latest_bulk_download_uri = next(
        (item for item in bulk_list if item["name"] == "All Cards"), None
    )["download_uri"]
    return latest_bulk_download_uri


def download_bulk(url):
    local_json_filename = url.split("/")[-1]
    # Normally, we'd check the file size with a HEAD request and redownload if there's a mismatch.
    # But scryfall is behind cloudflare and I can't be bothered to fuck with that.
    with requests.get(url, stream=True) as r:
        with open(local_json_filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    return local_json_filename


def allowed_type_line(card):
    try:
        # Fuck regex
        creature_substring = "Creature — "
        if creature_substring in card["type_line"]:
            type_agg = card["type_line"].split(" — ")[1]
            type_list = type_agg.split(" ")
            matched_types = set(type_list) & set(constants.ALLOWED_CREATURES)
            if bool(matched_types):
                return matched_types
        else:
            return False
    except KeyError:
        return False


def desired_properties(card):
    if allowed_type_line(card):
        return all(
            [
                card["object"] == "card",
                card["lang"] == "en",
                card["legalities"]["commander"] == "legal",
            ]
        )


def animal_pools(cards):
    creature_color_count = {}
    for anim in constants.ALLOWED_CREATURES:
        creature_color_count[anim] = []

    for crd in cards:
        # Fuck regex
        creature_substring = "Creature — "
        if creature_substring in crd["type_line"] and desired_properties(crd):
            type_agg = crd["type_line"].split(" — ")[1]
            type_list = type_agg.split(" ")
            matched_types = set(type_list) & set(constants.ALLOWED_CREATURES)
            if bool(matched_types):
                for tpe in matched_types:
                    # colorless bs
                    if "colors" in crd:
                        creature_color_count[tpe].append(crd["colors"])
                    else:
                        creature_color_count[tpe].append("N")
    return creature_color_count


def elligible_cards(raw_file):
    local_pickle_filename = "all-cards.pickle"
    if Path(local_pickle_filename).exists():
        with open(local_pickle_filename, "rb") as store_file:
            pick = pickle.load(store_file)
            return pick
    raw = json.load(open(raw_file))
    cards = []
    for card in raw:
        if desired_properties(card) and (
            card["name"] not in [c["name"] for c in cards]
        ):
            cards.append(card)
    with open(local_pickle_filename, "ab") as store_file:
        pickle.dump(cards, store_file)
    return cards
