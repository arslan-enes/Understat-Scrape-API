import sys
import requests
import time
sys.path.insert(0, '../..')
from database.pymongo_get_database import get_database


def update_player_grouped_stats(stat_type='season'):
    db = get_database()
    player_grouped_stats_collection = db[f'player_{stat_type}_stats_understat']
    # player_grouped_stats_collection.delete_many({}) # delete_all
    for understat_player in db['player_ids_understat'].find({}):
        res = requests.get(f"http://127.0.0.1:8000/get-player-grouped-stats?player_id={int(understat_player['id'])}&stat_type={stat_type}")
        res = add_id_to_season_stats(res.json(), understat_player['id'])
        player_grouped_stats_collection.insert_many(res)


def add_id_to_season_stats(season_stats: list, understat_id):

    for season_stat in season_stats:
        season_stat['id'] = understat_id

    return season_stats


if __name__ == '__main__':
    update_player_grouped_stats()
