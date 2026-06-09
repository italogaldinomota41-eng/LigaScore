# 🔌 EXEMPLOS DE REQUISIÇÕES E RESPOSTAS DA API

## Base URL
```
http://localhost:8000  (desenvolvimento)
```

---

## 📊 GET /api/teams/standings
**Obtém a tabela do campeonato ordenada por pontos, saldo de gols e gols a favor.**

### Request
```bash
curl -X GET "http://localhost:8000/api/teams/standings"
```

### Response (200 OK)
```json
[
  {
    "id": 3,
    "name": "Bayern de Belford Roxo",
    "position": 1,
    "points": 19,
    "games_played": 10,
    "wins": 6,
    "draws": 1,
    "losses": 3,
    "goals_for": 18,
    "goals_against": 8,
    "goal_difference": 10
  },
  {
    "id": 5,
    "name": "Tabajara FC",
    "position": 2,
    "points": 18,
    "games_played": 10,
    "wins": 5,
    "draws": 3,
    "losses": 2,
    "goals_for": 16,
    "goals_against": 9,
    "goal_difference": 7
  },
  {
    "id": 2,
    "name": "Sampaio Corrêa",
    "position": 3,
    "points": 14,
    "games_played": 10,
    "wins": 4,
    "draws": 2,
    "losses": 4,
    "goals_for": 12,
    "goals_against": 10,
    "goal_difference": 2
  },
  {
    "id": 4,
    "name": "Asa de Arapiraca",
    "position": 4,
    "points": 11,
    "games_played": 10,
    "wins": 3,
    "draws": 2,
    "losses": 5,
    "goals_for": 10,
    "goals_against": 14,
    "goal_difference": -4
  },
  {
    "id": 1,
    "name": "Íbis",
    "position": 5,
    "points": 9,
    "games_played": 10,
    "wins": 2,
    "draws": 3,
    "losses": 5,
    "goals_for": 8,
    "goals_against": 15,
    "goal_difference": -7
  },
  {
    "id": 6,
    "name": "Merden Bocard",
    "position": 6,
    "points": 4,
    "games_played": 10,
    "wins": 1,
    "draws": 1,
    "losses": 8,
    "goals_for": 5,
    "goals_against": 20,
    "goal_difference": -15
  }
]
```

---

## 📋 GET /api/teams/all
**Retorna todos os times com seus dados atuais.**

### Request
```bash
curl -X GET "http://localhost:8000/api/teams/all"
```

### Response (200 OK)
```json
[
  {
    "id": 1,
    "name": "Íbis",
    "wins": 2,
    "draws": 3,
    "losses": 5,
    "goals_for": 8,
    "goals_against": 15,
    "games_played": 10,
    "points": 9,
    "goal_difference": -7
  },
  {
    "id": 2,
    "name": "Sampaio Corrêa",
    "wins": 4,
    "draws": 2,
    "losses": 4,
    "goals_for": 12,
    "goals_against": 10,
    "games_played": 10,
    "points": 14,
    "goal_difference": 2
  },
  {
    "id": 3,
    "name": "Bayern de Belford Roxo",
    "wins": 6,
    "draws": 1,
    "losses": 3,
    "goals_for": 18,
    "goals_against": 8,
    "games_played": 10,
    "points": 19,
    "goal_difference": 10
  },
  {
    "id": 4,
    "name": "Asa de Arapiraca",
    "wins": 3,
    "draws": 2,
    "losses": 5,
    "goals_for": 10,
    "goals_against": 14,
    "games_played": 10,
    "points": 11,
    "goal_difference": -4
  },
  {
    "id": 5,
    "name": "Tabajara FC",
    "wins": 5,
    "draws": 3,
    "losses": 2,
    "goals_for": 16,
    "goals_against": 9,
    "games_played": 10,
    "points": 18,
    "goal_difference": 7
  },
  {
    "id": 6,
    "name": "Merden Bocard",
    "wins": 1,
    "draws": 1,
    "losses": 8,
    "goals_for": 5,
    "goals_against": 20,
    "games_played": 10,
    "points": 4,
    "goal_difference": -15
  }
]
```

---

## 👤 GET /api/teams/{team_id}
**Retorna dados e estatísticas detalhadas de um time específico.**

### Request
```bash
curl -X GET "http://localhost:8000/api/teams/3"
```

### Response (200 OK)
```json
{
  "team": {
    "id": 3,
    "name": "Bayern de Belford Roxo",
    "wins": 6,
    "draws": 1,
    "losses": 3,
    "goals_for": 18,
    "goals_against": 8,
    "games_played": 10,
    "points": 19,
    "goal_difference": 10
  },
  "averageGoalsPerGame": 1.8,
  "averageGoalsAgainstPerGame": 0.8,
  "winPercentage": 60.0
}
```

### Response (404 Not Found)
```json
{
  "detail": "Time não encontrado"
}
```

---

## ⚽ POST /api/teams/match
**Registra o resultado de uma partida e atualiza os times.**

### Request
```bash
curl -X POST "http://localhost:8000/api/teams/match" \
  -H "Content-Type: application/json" \
  -d '{
    "team1_id": 3,
    "team2_id": 5,
    "team1_goals": 2,
    "team2_goals": 1
  }'
```

### Request Body
```json
{
  "team1_id": 3,
  "team2_id": 5,
  "team1_goals": 2,
  "team2_goals": 1
}
```

### Response (200 OK)
```json
{
  "message": "Partida registrada com sucesso",
  "team1": {
    "id": 3,
    "name": "Bayern de Belford Roxo",
    "wins": 7,
    "draws": 1,
    "losses": 3,
    "goals_for": 20,
    "goals_against": 9,
    "games_played": 11,
    "points": 22,
    "goal_difference": 11
  },
  "team2": {
    "id": 5,
    "name": "Tabajara FC",
    "wins": 5,
    "draws": 3,
    "losses": 3,
    "goals_for": 17,
    "goals_against": 11,
    "games_played": 11,
    "points": 18,
    "goal_difference": 6
  }
}
```

### Errors

#### 400 Bad Request - Time não encontrado
```json
{
  "detail": "Time não encontrado"
}
```

#### 422 Unprocessable Entity - Validação falhou
```json
{
  "detail": [
    {
      "loc": ["body", "team1_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

---

## ❤️ GET /api/teams/health/check
**Verifica a saúde do servidor de times.**

### Request
```bash
curl -X GET "http://localhost:8000/api/teams/health/check"
```

### Response (200 OK)
```json
{
  "status": "healthy",
  "message": "API de Estatísticas de Futebol está funcionando"
}
```

---

## 🏥 GET /health
**Health check geral da aplicação.**

### Request
```bash
curl -X GET "http://localhost:8000/health"
```

### Response (200 OK)
```json
{
  "status": "healthy",
  "service": "LigaScore - Plataforma de Estatísticas de Futebol"
}
```

---

## 📚 GET /
**Informações sobre a API.**

### Request
```bash
curl -X GET "http://localhost:8000/"
```

### Response (200 OK)
```json
{
  "name": "LigaScore - Plataforma de Estatísticas de Futebol",
  "version": "1.0.0",
  "message": "Bem-vindo à API de Estatísticas de Futebol!",
  "endpoints": {
    "standings": "GET /api/teams/standings",
    "all_teams": "GET /api/teams/all",
    "team_details": "GET /api/teams/{team_id}",
    "record_match": "POST /api/teams/match",
    "health": "GET /api/teams/health/check",
    "docs": "GET /docs",
    "redoc": "GET /redoc"
  }
}
```

---

## 🧪 Testando com Swagger UI

FastAPI gera documentação interativa automaticamente:

1. Abra `http://localhost:8000/docs` no navegador
2. Todos os endpoints estão listados
3. Clique em qualquer endpoint para expandir
4. Clique em "Try it out"
5. Preencha os parâmetros
6. Clique em "Execute"
7. Veja a resposta em tempo real

---

## 📝 Notas Importantes

- **Todos os times têm IDs de 1 a 6**
- **Pontos são calculados automaticamente**: Vitória=3, Empate=1, Derrota=0
- **Saldo de gols é usado como critério de desempate**
- **Partidas devem ser entre times diferentes**
- **Todos os endpoints retornam JSON**
- **CORS está habilitado para desenvolvimento**

---

## 🔄 Fluxo Típico de Uso

```
1. GET /api/teams/standings
   └─ Mostra tabela atual

2. POST /api/teams/match
   └─ Registra partida (ex: Bayern 2x1 Tabajara)

3. GET /api/teams/standings
   └─ Tabela atualizada (Bayern sobe de posição)

4. GET /api/teams/3
   └─ Detalhes atualizados do Bayern
```

---

## 🐍 Exemplo em Python

```python
import requests

API_URL = "http://localhost:8000"

# Obter tabela
response = requests.get(f"{API_URL}/api/teams/standings")
standings = response.json()
for team in standings:
    print(f"{team['position']}. {team['name']} - {team['points']}pts")

# Registrar partida
match_data = {
    "team1_id": 3,
    "team2_id": 5,
    "team1_goals": 2,
    "team2_goals": 1
}
response = requests.post(f"{API_URL}/api/teams/match", json=match_data)
result = response.json()
print(result["message"])
```

---

## 🌐 Exemplo em JavaScript

```javascript
const API_URL = "http://localhost:8000";

// Obter tabela
fetch(`${API_URL}/api/teams/standings`)
  .then(response => response.json())
  .then(standings => {
    standings.forEach(team => {
      console.log(`${team.position}. ${team.name} - ${team.points}pts`);
    });
  });

// Registrar partida
const matchData = {
  team1_id: 3,
  team2_id: 5,
  team1_goals: 2,
  team2_goals: 1
};

fetch(`${API_URL}/api/teams/match`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(matchData)
})
.then(response => response.json())
.then(result => console.log(result.message));
```

---

**API Reference gerada para LigaScore**
