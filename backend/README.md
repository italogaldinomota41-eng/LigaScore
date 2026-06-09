# LigaScore Backend

API REST para a Plataforma de Estatísticas de Futebol

## Sobre

Back-end em FastAPI que implementa a lógica de negócio e acesso a dados para a plataforma de estatísticas de futebol. Segue rigorosamente os padrões de arquitetura MVC e Camadas (Layers).

## Stack

- **Framework**: FastAPI (Python)
- **Banco de Dados**: SQLite
- **Servidor**: Uvicorn
- **Arquitetura**: MVC + Camadas (Layers)

## Arquitetura (MVC + Camadas)

```
app/
├── models/              # Camada de Domínio (Entidades)
│   └── team.py          # Modelo Team
├── routes/              # Camada de Apresentação (Controllers REST)
│   └── teams.py         # Rotas de times
├── services/            # Camada de Negócio (Business Logic)
│   └── league_service.py # Serviço de campeonato
├── database/            # Camada de Acesso a Dados (Repository)
│   ├── db.py            # Configuração do banco
│   └── team_repository.py # Repository de times
├── config/              # Configuração
│   └── settings.py      # Variáveis de ambiente
└── main.py              # Aplicação FastAPI principal
```

## Executar Localmente

### Pré-requisitos

- Python 3.9+
- pip (gerenciador de pacotes)

### Instalação

```bash
# 1. Entrar no diretório backend
cd backend

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Executar servidor
python -m uvicorn app.main:app --reload --port 8000
```

A API estará disponível em `http://localhost:8000`

### Documentação Interativa

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Endpoints

### Times

- `GET /api/teams/standings` - Tabela do campeonato ordenada
- `GET /api/teams/all` - Lista de todos os times
- `GET /api/teams/{team_id}` - Detalhes de um time com estatísticas
- `POST /api/teams/match` - Registrar resultado de partida
- `GET /api/teams/health/check` - Health check

### Gerais

- `GET /` - Informações sobre a API
- `GET /health` - Health check geral

## Exemplo de Requisições

### Obter Tabela do Campeonato

```bash
curl -X GET "http://localhost:8000/api/teams/standings"
```

Response:
```json
[
  {
    "id": 1,
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
  }
]
```

### Registrar Partida

```bash
curl -X POST "http://localhost:8000/api/teams/match" \
  -H "Content-Type: application/json" \
  -d '{
    "team1_id": 1,
    "team2_id": 2,
    "team1_goals": 3,
    "team2_goals": 1
  }'
```

## Deploy no Railway

### Pré-requisitos

- Conta no [Railway.app](https://railway.app)
- GitHub com repositório public

### Passos

1. Fazer push do código para GitHub
2. Conectar repositório no Railway
3. Configurar variáveis de ambiente:
   - `PORT`: 8000
   - `DATABASE_URL`: `sqlite:///./ligascore.db`
4. Railway detectará `Procfile` e fará deploy automático

### Arquivo Procfile

```
web: cd backend && python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## Banco de Dados

### Inicialização

O banco de dados SQLite é inicializado automaticamente ao executar a aplicação. A tabela `teams` é criada com os dados mock dos 6 times fictícios.

### Dados Iniciais

```
1. Íbis (2V, 3E, 5D)
2. Sampaio Corrêa (4V, 2E, 4D)
3. Bayern de Belford Roxo (6V, 1E, 3D)
4. Asa de Arapiraca (3V, 2E, 5D)
5. Tabajara FC (5V, 3E, 2D)
6. Merden Bocard (1V, 1E, 8D)
```

### Schema

```sql
CREATE TABLE teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    wins INTEGER DEFAULT 0,
    draws INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,
    goals_for INTEGER DEFAULT 0,
    goals_against INTEGER DEFAULT 0
)
```

## Regras de Negócio

### Cálculo de Pontos
- Vitória: 3 pontos
- Empate: 1 ponto
- Derrota: 0 pontos

### Ordenação da Tabela
1. Pontos (descendente)
2. Saldo de gols (descendente)
3. Gols a favor (descendente)

## Estrutura do Código

### Camada de Domínio (Models)
Contém a entidade `Team` com propriedades calculadas:
- `points`: Calcula total de pontos
- `games_played`: Total de jogos
- `goal_difference`: Saldo de gols

### Camada de Negócio (Services)
`LeagueService` implementa as regras do domínio:
- `get_league_standings()`: Ordena times por pontos
- `record_match()`: Registra partida e atualiza dados
- `get_team_statistics()`: Calcula estatísticas

### Camada de Acesso a Dados (Repository)
`TeamRepository` abstrai acesso ao banco:
- `get_all_teams()`: Retorna todos os times
- `get_team_by_id()`: Retorna um time específico
- `update_team()`: Atualiza um time
- `create_team()`: Cria novo time

### Camada de Apresentação (Routes)
Rotas FastAPI que expõem endpoints REST:
- Delegam para `Services` (lógica de negócio)
- Não implementam lógica complexa
- Fazem validação de entrada com Pydantic

## Variáveis de Ambiente

Criar arquivo `.env`:

```
DEBUG=True
HOST=0.0.0.0
PORT=8000
DATABASE_URL=sqlite:///./ligascore.db
```

## Testes

Para testar a API localmente:

```bash
# Testar endpoint de standings
curl -X GET "http://localhost:8000/api/teams/standings" | python -m json.tool

# Testar health check
curl -X GET "http://localhost:8000/health"

# Testar registrar partida
curl -X POST "http://localhost:8000/api/teams/match" \
  -H "Content-Type: application/json" \
  -d '{"team1_id":1,"team2_id":2,"team1_goals":2,"team2_goals":1}'
```

## Requisitos do Projeto Acadêmico

✓ **MVC**: Separação clara entre Routes (Controllers), Services (Lógica) e Models
✓ **Camadas**: Modelos → Repository → Services → Routes
✓ **REST API**: FastAPI expõe endpoints HTTP
✓ **Isolamento**: Back-end independente do front-end
✓ **Cloud-Ready**: Configurado para Railway com Procfile
✓ **Dados Mock**: 6 times fictícios pré-carregados

## Autores

Desenvolvido como projeto acadêmico de Arquitetura de Software
