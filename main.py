import understat_functions.understat_functions as uf
import asyncio
from fastapi import FastAPI, Path
import nest_asyncio
nest_asyncio.apply()

app = FastAPI()


@app.get("/get-player-grouped-stats")
async def get_player_grouped_stats(player_id: int = 619, stat_type: str = 'season'):
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(uf.get_player_grouped_stats(player_id, stat_type))
    return data


@app.get("/get-all-player-ids")
async def get_all_player_ids():
    loop = asyncio.get_event_loop()
    seasons = ['2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014']
    leagues = ['epl', 'la_liga', 'bundesliga', 'serie_a', 'ligue_1']

    total_data = []
    for league in leagues:
        for season in seasons:
            data = loop.run_until_complete(uf.get_player_ids(season=season, league=league))
            data = [{'id': x['id'], 'player_name': x['player_name']} for x in data]
            total_data += data
            print(f"{season}-{league} added.")

    return total_data
