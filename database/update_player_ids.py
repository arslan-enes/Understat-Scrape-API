from pymongo_get_database import get_database
import requests


def update_player_ids():
    db = get_database()
    player_ids_collection = db["player_ids_understat"]
    # player_ids_collection.delete_many({}) # delete_all
    res = requests.get('http://127.0.0.1:8000/get-all-player-ids')
    print(res.json())
    # using a list comprehension to get rid of duplicated values.
    player_ids_collection.insert_many([dict(t) for t in {tuple(d.items()) for d in res.json()}])


if __name__ == '__main__':
    print('Player ids re-uploading...')
    update_player_ids()
