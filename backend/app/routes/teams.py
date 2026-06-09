"""
Teams Routes (Controllers REST)
Camada de apresentação - Expõe endpoints REST para o front-end.
Cada rota delega a lógica de negócio para o Service.
"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from app.services.league_service import LeagueService
from app.database.team_repository import TeamRepository

# Router para as rotas de times
router = APIRouter(prefix="/api/teams", tags=["teams"])

# Modelos Pydantic para validação de entrada/saída
class MatchRequest(BaseModel):
    """Request body para registrar uma partida"""
    team1_id: int
    team2_id: int
    team1_goals: int = Field(ge=0)
    team2_goals: int = Field(ge=0)
    events: Optional[str] = None

class TeamResponse(BaseModel):
    """Response de um time"""
    id: int
    name: str
    position: int
    points: int
    games_played: int
    wins: int
    draws: int
    losses: int
    goals_for: int
    goals_against: int
    goal_difference: int

# ===== ENDPOINTS REST =====

@router.get("/standings", response_model=List[dict])
def get_standings():
    """
    GET /api/teams/standings
    
    Endpoint: Obtém a tabela do campeonato ordenada por pontos.
    Delega para o LeagueService que implementa a lógica de cálculo.
    """
    standings = LeagueService.get_league_standings()
    return standings

@router.get("/all", response_model=List[dict])
def get_all_teams():
    """
    GET /api/teams/all
    
    Endpoint: Retorna todos os times com seus dados.
    Acessa diretamente o Repository (sem lógica de negócio complexa).
    """
    teams = TeamRepository.get_all_teams()
    return [team.to_dict() for team in teams]

@router.get("/health/check", response_model=dict)
def health_check():
    """
    GET /api/teams/health/check

    Endpoint: Verifica se a API está funcionando.
    """
    return {
        "status": "healthy",
        "message": "API de Estatísticas de Futebol está funcionando"
    }

@router.get("/{team_id}", response_model=dict)
def get_team_by_id(team_id: int):
    """
    GET /api/teams/{team_id}
    
    Endpoint: Retorna dados e estatísticas de um time específico (inclui histórico de partidas).
    """
    statistics = LeagueService.get_team_statistics(team_id)
    if "error" in statistics:
        raise HTTPException(status_code=404, detail=statistics["error"])
    return statistics

@router.post("/match", response_model=dict, status_code=status.HTTP_201_CREATED)
def record_match(match: MatchRequest):
    """
    POST /api/teams/match
    
    Endpoint: Registra o resultado de uma partida.
    Delega para o LeagueService que atualiza os dados dos times.
    
    Request body:
    {
        "team1_id": 1,
        "team2_id": 2,
        "team1_goals": 2,
        "team2_goals": 1
    }
    """
    try:
        result = LeagueService.record_match(
            match.team1_id,
            match.team2_id,
            match.team1_goals,
            match.team2_goals,
            match.events
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao registrar partida"
        ) from exc

    if "error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])

    return result
