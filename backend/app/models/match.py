"""
Model: Match (Entidade de Domínio)
Representa uma partida jogada entre dois times e eventos associados.
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Match:
    id: Optional[int] = None
    team1_id: int = 0
    team2_id: int = 0
    team1_goals: int = 0
    team2_goals: int = 0
    events: Optional[str] = None
    played_at: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "team1_id": self.team1_id,
            "team2_id": self.team2_id,
            "team1_goals": self.team1_goals,
            "team2_goals": self.team2_goals,
            "events": self.events,
            "played_at": self.played_at,
        }
