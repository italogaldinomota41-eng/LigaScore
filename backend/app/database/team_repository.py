"""
Team Repository
Camada de acesso a dados para times.
Implementa padrão Repository para isolamento de dados.
"""
from typing import List, Optional
from app.models.team import Team
from app.database.db import get_db_connection

class TeamRepository:
    """
    Repository Pattern - Abstração para acesso a dados de times
    Encapsula toda lógica de persistência do banco de dados
    """
    
    @staticmethod
    def get_all_teams() -> List[Team]:
        """Retorna todos os times do banco de dados"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams ORDER BY id")
        rows = cursor.fetchall()
        conn.close()
        
        teams = []
        for row in rows:
            team = Team(
                id=row["id"],
                name=row["name"],
                wins=row["wins"],
                draws=row["draws"],
                losses=row["losses"],
                goals_for=row["goals_for"],
                goals_against=row["goals_against"],
            )
            teams.append(team)
        
        return teams
    
    @staticmethod
    def get_team_by_id(team_id: int) -> Optional[Team]:
        """Retorna um time específico pelo ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams WHERE id = ?", (team_id,))
        row = cursor.fetchone()
        conn.close()
        
        if not row:
            return None
        
        return Team(
            id=row["id"],
            name=row["name"],
            wins=row["wins"],
            draws=row["draws"],
            losses=row["losses"],
            goals_for=row["goals_for"],
            goals_against=row["goals_against"],
        )
    
    @staticmethod
    def update_team(team: Team) -> Team:
        """Atualiza os dados de um time no banco de dados"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE teams 
            SET wins=?, draws=?, losses=?, goals_for=?, goals_against=?
            WHERE id=?
        """, (team.wins, team.draws, team.losses, 
              team.goals_for, team.goals_against, team.id))
        conn.commit()
        conn.close()
        
        return team
    
    @staticmethod
    def create_team(team: Team) -> Team:
        """Cria um novo time no banco de dados"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO teams (name, wins, draws, losses, goals_for, goals_against)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (team.name, team.wins, team.draws, team.losses, 
              team.goals_for, team.goals_against))
        conn.commit()
        team.id = cursor.lastrowid
        conn.close()
        
        return team
