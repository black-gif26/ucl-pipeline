"""Europa League results played before matchday 3.

Scores are the 90-minute results on the UEFA league-phase page.
Matchday 3, 22 October 2026, is not in this list.
https://www.uefa.com/uefaeuropaleague/news/02a8-2174cafa5bb6-82bbc20c9b92-1000--2026-27-europa-league-all-the-league-phase-fixtures-and-re/
"""

from __future__ import annotations

from datetime import date

from ucl_pipeline.models import Match

_NAME = {
    "Ararat-Armenia": "FC Ararat-Armenia",
    "Sparta Praha": "AC Sparta Praha",
    "Omonia": "AC Omonia",
    "Celta": "RC Celta de Vigo",
    "Milan": "AC Milan",
    "Benfica": "Sport Lisboa e Benfica",
    "Leverkusen": "Bayer 04 Leverkusen",
    "Celje": "NK Celje",
    "Hapoel Beer-Sheva": "Hapoel Be'er Sheva",
    "GNK Dinamo": "GNK Dinamo Zagreb",
    "Olympiacos": "Olympiakos Piraeus",
    "Jagiellonia": "Jagiellonia Białystok",
    "Anderlecht": "RSC Anderlecht",
    "Lyon": "Olympique Lyonnais",
    "Sturm Graz": "SK Sturm Graz",
    "Rennes": "Stade Rennais FC 1901",
    "Sunderland": "Sunderland AFC",
    "AZ Alkmaar": "AZ",
    "OFI Crete": "OFI Heraklion",
    "Hoffenheim": "TSG 1899 Hoffenheim",
    "Levski Sofia": "PFC Levski Sofia",
    "Salzburg": "FC Red Bull Salzburg",
    "Beşiktaş": "Beşiktaş",
    "Marseille": "Olympique de Marseille",
    "Celtic": "Celtic FC",
    "Ferencváros": "Ferencvárosi TC",
    "Crystal Palace": "Crystal Palace FC",
    "Lech Poznań": "Lech Poznań",
    "Viktoria Plzeň": "Viktoria Plzeň",
    "Union SG": "Union Saint-Gilloise",
    "Juventus": "Juventus FC",
    "N.E.C.": "NEC",
    "Lillestrøm": "Lillestrøm SK",
    "Torreense": "SCU Torreense",
    "Real Sociedad": "Real Sociedad de Fútbol",
    "Bournemouth": "AFC Bournemouth",
}

# (date, home, away, home goals, away goals). Matchday 1 then matchday 2.
_RESULTS = (
    (date(2026, 9, 16), "Ararat-Armenia", "Sparta Praha", 1, 4),
    (date(2026, 9, 16), "Omonia", "Celta", 1, 0),
    (date(2026, 9, 16), "Milan", "Benfica", 0, 2),
    (date(2026, 9, 16), "Leverkusen", "Celje", 2, 0),
    (date(2026, 9, 16), "Hapoel Beer-Sheva", "GNK Dinamo", 0, 0),
    (date(2026, 9, 16), "Olympiacos", "Jagiellonia", 2, 1),
    (date(2026, 9, 16), "Anderlecht", "Lyon", 1, 2),
    (date(2026, 9, 16), "Sturm Graz", "Rennes", 0, 0),
    (date(2026, 9, 16), "Sunderland", "AZ Alkmaar", 1, 0),
    (date(2026, 9, 17), "OFI Crete", "Hoffenheim", 2, 0),
    (date(2026, 9, 17), "Levski Sofia", "Salzburg", 0, 1),
    (date(2026, 9, 17), "Beşiktaş", "Marseille", 4, 1),
    (date(2026, 9, 17), "Celtic", "Ferencváros", 1, 3),
    (date(2026, 9, 17), "Crystal Palace", "Lech Poznań", 4, 0),
    (date(2026, 9, 17), "Viktoria Plzeň", "Union SG", 0, 3),
    (date(2026, 9, 17), "Juventus", "N.E.C.", 5, 0),
    (date(2026, 9, 17), "Lillestrøm", "Torreense", 1, 2),
    (date(2026, 9, 17), "Real Sociedad", "Bournemouth", 1, 2),
    (date(2026, 10, 15), "Sparta Praha", "Lillestrøm", 1, 1),
    (date(2026, 10, 15), "AZ Alkmaar", "Hapoel Beer-Sheva", 2, 1),
    (date(2026, 10, 15), "Salzburg", "Milan", 0, 4),
    (date(2026, 10, 15), "Lech Poznań", "Leverkusen", 0, 4),
    (date(2026, 10, 15), "Celje", "Omonia", 0, 3),
    (date(2026, 10, 15), "Lyon", "Crystal Palace", 3, 2),
    (date(2026, 10, 15), "Union SG", "Real Sociedad", 1, 1),
    (date(2026, 10, 15), "Torreense", "Sunderland", 1, 2),
    (date(2026, 10, 15), "Bournemouth", "Sturm Graz", 3, 0),
    (date(2026, 10, 15), "Ferencváros", "Viktoria Plzeň", 2, 1),
    (date(2026, 10, 15), "GNK Dinamo", "Anderlecht", 1, 0),
    (date(2026, 10, 15), "Jagiellonia", "Ararat-Armenia", 3, 1),
    (date(2026, 10, 15), "N.E.C.", "Levski Sofia", 1, 1),
    (date(2026, 10, 15), "Marseille", "Olympiacos", 0, 1),
    (date(2026, 10, 15), "Celta", "Juventus", 1, 2),
    (date(2026, 10, 15), "Benfica", "Celtic", 4, 1),
    (date(2026, 10, 15), "Rennes", "OFI Crete", 2, 1),
    (date(2026, 10, 15), "Hoffenheim", "Beşiktaş", 2, 3),
)


def europa_results_before(cutoff: date) -> list[Match]:
    """Played Europa league-phase matches dated strictly before cutoff."""
    rows = []
    for played, home, away, home_goals, away_goals in _RESULTS:
        if played >= cutoff:
            continue
        rows.append(
            Match(
                date=played,
                season="2026-27",
                competition="UEFA Europa League",
                stage="League phase",
                home_team=_NAME[home],
                away_team=_NAME[away],
                home_goals=home_goals,
                away_goals=away_goals,
                source="uefa.com",
                priority=1,
            )
        )
    return rows
