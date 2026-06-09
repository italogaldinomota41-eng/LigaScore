"""
Match Repository
Acessa dados de partidas (matches)
"""
from typing import List
from app.models.match import Match
from app.database.db import get_db_connection

class MatchRepository:
    @staticmethod
    def create_match(match: Match) -> Match:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO matches (team1_id, team2_id, team1_goals, team2_goals, events)
            VALUES (?, ?, ?, ?, ?)
            """,
            (match.team1_id, match.team2_id, match.team1_goals, match.team2_goals, match.events)
        )
        conn.commit()
        match.id = cursor.lastrowid
        cursor.execute("SELECT played_at FROM matches WHERE id = ?", (match.id,))
        row = cursor.fetchone()
        if row:
            match.played_at = row[0]
        conn.close()
        return match

    @staticmethod
    def get_matches_by_team(team_id: int) -> List[Match]:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM matches
            WHERE team1_id = ? OR team2_id = ?
            ORDER BY played_at DESC
            """,
            (team_id, team_id)
        )
        rows = cursor.fetchall()
        conn.close()

        matches = []
        for row in rows:
            m = Match(
                id=row[0],
                team1_id=row[1],
                team2_id=row[2],
                team1_goals=row[3],
                team2_goals=row[4],
                events=row[5],
                played_at=row[6],
            )
            matches.append(m)
        return matches

    @staticmethod
    def get_recent_matches(limit: int = 10):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM matches ORDER BY played_at DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "team1_id": row[1],
                "team2_id": row[2],
                "team1_goals": row[3],
                "team2_goals": row[4],
                "events": row[5],
                "played_at": row[6],
            })
        return result
