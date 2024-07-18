import os
import django
from django.db.models import Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions


def get_tennis_players(search_name=None, search_country=None):
    if search_country is None and search_name is None:
        return ''
    if search_country is not None and search_name is not None:
        players = TennisPlayer.objects.filter(full_name__icontains=search_name, country__icontains=search_country)
    elif search_name is not None:
        players = TennisPlayer.objects.filter(full_name__icontains=search_name)
    else:
        players = TennisPlayer.objects.filter(country__icontains=search_country)

    if not players:
        return ''

    players = players.order_by('ranking')
    result = []

    for player in players:
        result.append(f'Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}')

    return '\n'.join(result)


def get_top_tennis_player():
    player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()
    if player is None:
        return ''
    return f"Top Tennis Player: {player.full_name} with {player.wins_count} wins."


def get_tennis_player_by_matches_count():
    player_with_most_matches = TennisPlayer.objects \
        .annotate(matches_count=Count('matches')) \
        .order_by('-matches_count', 'ranking').first()

    if player_with_most_matches is not None and player_with_most_matches.matches_count:
        return f"Tennis Player: {player_with_most_matches.full_name} with {player_with_most_matches.matches_count} matches played."

    return ''


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ''
    matching_tournaments = Tournament.objects.prefetch_related('matches') \
        .annotate(matches_count=Count('matches')) \
        .filter(surface_type__icontains=surface).order_by('-start_date')
    result = []

    for tournament in matching_tournaments:
        result.append(
            f'Tournament: {tournament.name}, start date: {tournament.start_date}, matches: {tournament.matches_count}')

    return '\n'.join(result) if result else ''


def get_latest_match_info():
    latest_match = Match.objects.prefetch_related('players') \
        .order_by('-date_played', '-id').first()

    if latest_match is None:
        return ''

    players = latest_match.players.order_by('full_name')
    player_1 = players.first().full_name
    player_2 = players.last().full_name
    winner = "TBA" if latest_match.winner is None else latest_match.winner.full_name

    return f"Latest match played on: {latest_match.date_played}, tournament: {latest_match.tournament.name}, " \
           f"score: {latest_match.score}, players: {player_1} vs {player_2}, " \
           f"winner: {winner}, summary: {latest_match.summary}"


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return 'No matches found.'

    matches = Match.objects.select_related('tournament', 'winner') \
        .filter(tournament__name__exact=tournament_name).order_by('-date_played')
    if not matches:
        return 'No matches found.'

    result = []
    [result.append(
        f"Match played on: {m.date_played}, score: {m.score}, winner: {m.winner.full_name if m.winner else 'TBA'}") for
     m in matches]
    return '\n'.join(result)
