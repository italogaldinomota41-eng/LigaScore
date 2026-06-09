"""
League Service
Camada de negócio que implementa a lógica de cálculo da tabela de campeonato.
Esta camada encapsula todas as regras de negócio do domínio.
"""
from typing import List, Optional
from app.models.team import Team
from app.models.match import Match
from app.database.team_repository import TeamRepository
from app.database.match_repository import MatchRepository

class LeagueService:
    """
    Service - Camada de Lógica de Negócio
    Implementa as regras de cálculo da tabela do campeonato.
    Não acessa diretamente o banco; usa o Repository.
    """
    
    @staticmethod
    def get_league_standings() -> List[dict]:
        """
        Retorna a tabela do campeonato ordenada por:
        1. Pontos (vitória=3, empate=1, derrota=0)
        2. Saldo de gols (gols a favor - gols contra)
        3. Gols a favor (como critério de desempate final)
        
        Esta é a REGRA DE NEGÓCIO principal do domínio.
        """
        teams = TeamRepository.get_all_teams()
        
        # Ordenar pela lógica de campeonato
        standings = sorted(
            teams,
            key=lambda t: (t.points, t.goal_difference, t.goals_for),
            reverse=True
        )
        
        # Converter para dicts e adicionar posição na tabela
        result = []
        for position, team in enumerate(standings, 1):
            team_dict = team.to_dict()
            team_dict["position"] = position
            result.append(team_dict)
        
        return result
    
    @staticmethod
    def record_match(team1_id: int, team2_id: int,
                     team1_goals: int, team2_goals: int,
                     events: Optional[str] = None) -> dict:
        """
        Registra o resultado de uma partida entre dois times.
        Atualiza vitórias, empates, derrotas e gols.
        
        REGRA DE NEGÓCIO: 
        - Vitória: +3 pontos
        - Empate: +1 ponto
        - Derrota: 0 pontos
        """
        if team1_id == team2_id:
            return {"error": "Selecione dois times diferentes"}

        if team1_goals < 0 or team2_goals < 0:
            return {"error": "Gols não podem ser negativos"}

        team1 = TeamRepository.get_team_by_id(team1_id)
        team2 = TeamRepository.get_team_by_id(team2_id)

        if not team1 or not team2:
            return {"error": "Time não encontrado"}

        LeagueService._apply_match_result(team1, team2, team1_goals, team2_goals)

        # Primeiro persiste a classificação dos dois times.
        updated_team1 = TeamRepository.update_team(team1)
        updated_team2 = TeamRepository.update_team(team2)

        # Só depois salva o histórico da partida, com eventos opcionais.
        match = Match(
            team1_id=team1_id,
            team2_id=team2_id,
            team1_goals=team1_goals,
            team2_goals=team2_goals,
            events=events.strip() if events else None,
        )
        saved_match = MatchRepository.create_match(match)

        return {
            "success": True,
            "message": "Partida registrada com sucesso e tabela atualizada",
            "score": f"{updated_team1.name} {team1_goals} x {team2_goals} {updated_team2.name}",
            "team1": updated_team1.to_dict(),
            "team2": updated_team2.to_dict(),
            "match": saved_match.to_dict(),
        }

    @staticmethod
    def _apply_match_result(team1: Team, team2: Team,
                            team1_goals: int, team2_goals: int) -> None:
        """Aplica gols, vitórias, empates, derrotas e pontos derivados na entidade Team."""
        team1.goals_for += team1_goals
        team1.goals_against += team2_goals
        team2.goals_for += team2_goals
        team2.goals_against += team1_goals

        if team1_goals > team2_goals:
            team1.wins += 1
            team2.losses += 1
        elif team1_goals < team2_goals:
            team2.wins += 1
            team1.losses += 1
        else:
            team1.draws += 1
            team2.draws += 1
    
    @staticmethod
    def get_team_statistics(team_id: int) -> dict:
        """Retorna estatísticas detalhadas de um time"""
        team = TeamRepository.get_team_by_id(team_id)
        
        if not team:
            return {"error": "Time não encontrado"}
        
        # Recuperar partidas do time
        matches = MatchRepository.get_matches_by_team(team_id)
        matches_list = [m.to_dict() for m in matches]

        return {
            "team": team.to_dict(),
            "matches": matches_list,
            "averageGoalsPerGame": round(
                team.goals_for / team.games_played, 2
            ) if team.games_played > 0 else 0,
            "averageGoalsAgainstPerGame": round(
                team.goals_against / team.games_played, 2
            ) if team.games_played > 0 else 0,
            "winPercentage": round(
                (team.wins / team.games_played) * 100, 2
            ) if team.games_played > 0 else 0,
        }
