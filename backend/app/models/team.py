"""
Model: Team (Entidade de Domínio)
Representa um time de futebol com seus atributos.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Team:
    """
    Entidade Team - Modelo de Domínio
    Armazena informações de um time de futebol.
    """
    id: Optional[int] = None
    name: str = ""
    wins: int = 0
    draws: int = 0
    losses: int = 0
    goals_for: int = 0
    goals_against: int = 0
    
    @property
    def games_played(self) -> int:
        """Calcula total de jogos"""
        return self.wins + self.draws + self.losses
    
    @property
    def points(self) -> int:
        """Calcula pontos no campeonato (vitória=3, empate=1, derrota=0)"""
        return (self.wins * 3) + (self.draws * 1)
    
    @property
    def goal_difference(self) -> int:
        """Calcula saldo de gols"""
        return self.goals_for - self.goals_against
    
    def to_dict(self) -> dict:
        """Converte para dicionário (para serialização JSON)"""
        return {
            "id": self.id,
            "name": self.name,
            "wins": self.wins,
            "draws": self.draws,
            "losses": self.losses,
            "goals_for": self.goals_for,
            "goals_against": self.goals_against,
            "games_played": self.games_played,
            "points": self.points,
            "goal_difference": self.goal_difference,
        }
