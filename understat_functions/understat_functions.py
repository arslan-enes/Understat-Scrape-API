import aiohttp
from understat import Understat
import pandas as pd
import json


async def get_player_grouped_stats(player_id=619, stat_type='season'):
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        grouped_stats = await understat.get_player_grouped_stats(player_id)
        return grouped_stats[stat_type]


async def get_player_ids(league, season):
    """
    Get player ids from understat
    :param league: league name
    :param season: season year
    :return: Player ids dataframe
    """
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_league_players(
            league,
            season
        )
        return players
