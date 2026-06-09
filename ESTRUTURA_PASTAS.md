# 📁 ESTRUTURA COMPLETA DO PROJETO FLASHSCORE

```
/home/italo-mota/LigaScore/
│
├── 📄 README.md                          # Documentação principal do projeto
├── 📄 ARQUITETURA_JUSTIFICATIVA.md      # Justificativa acadêmica (3 parágrafos)
│
│
├── 📂 backend/                           # API REST - FastAPI + SQLite
│   │
│   ├── 📂 app/                           # Aplicação principal
│   │   │
│   │   ├── 📂 models/                    # CAMADA DE DOMÍNIO (Domain Layer)
│   │   │   ├── __init__.py
│   │   │   └── team.py                   # Entidade Team com propriedades calculadas
│   │   │                                  # - points (vitória=3, empate=1)
│   │   │                                  # - goal_difference
│   │   │                                  # - games_played
│   │   │
│   │   ├── 📂 routes/                    # CAMADA DE APRESENTAÇÃO (Controllers REST)
│   │   │   ├── __init__.py
│   │   │   └── teams.py                  # Rotas/Endpoints REST
│   │   │                                  # GET  /api/teams/standings
│   │   │                                  # GET  /api/teams/all
│   │   │                                  # GET  /api/teams/{id}
│   │   │                                  # POST /api/teams/match
│   │   │
│   │   ├── 📂 services/                  # CAMADA DE SERVIÇO (Business Logic)
│   │   │   ├── __init__.py
│   │   │   └── league_service.py         # Lógica de negócio do campeonato
│   │   │                                  # - get_league_standings()
│   │   │                                  # - record_match()
│   │   │                                  # - get_team_statistics()
│   │   │
│   │   ├── 📂 database/                  # CAMADA DE ACESSO A DADOS (Repository)
│   │   │   ├── __init__.py
│   │   │   ├── db.py                     # Configuração SQLite
│   │   │   │                              # - init_db() - cria tabelas
│   │   │   │                              # - get_db_connection()
│   │   │   │                              # - Dados mock pré-carregados
│   │   │   │
│   │   │   └── team_repository.py        # Repository Pattern
│   │   │                                  # - get_all_teams()
│   │   │                                  # - get_team_by_id()
│   │   │                                  # - update_team()
│   │   │                                  # - create_team()
│   │   │
│   │   ├── 📂 config/                    # Configuração
│   │   │   ├── __init__.py
│   │   │   └── settings.py               # Variáveis de ambiente
│   │   │
│   │   ├── __init__.py
│   │   └── main.py                       # Aplicação FastAPI
│   │                                      # - Inicialização
│   │                                      # - CORS Middleware
│   │                                      # - Registro de rotas
│   │
│   ├── 📄 requirements.txt                # Dependências Python
│   │                                      # fastapi==0.104.1
│   │                                      # uvicorn==0.24.0
│   │                                      # pydantic==2.5.0
│   │                                      # python-dotenv==1.0.0
│   │
│   ├── 📄 Procfile                        # Deploy no Railway
│   │                                      # web: python -m uvicorn app.main:app ...
│   │
│   ├── 📄 .env                            # Variáveis de ambiente
│   │
│   └── 📄 README.md                       # Documentação do back-end
│
│
└── 📂 frontend/                          # Interface Web - HTML/CSS/JS
    │
    ├── 📂 public/                         # Arquivos estáticos
    │   └── index.html                     # Arquivo principal
    │                                      # - Header com branding
    │                                      # - Navigation (4 views)
    │                                      # - Main content area
    │                                      # - Views:
    │                                      #   * standings (tabela)
    │                                      #   * teams (cards)
    │                                      #   * match (form)
    │                                      #   * about (info)
    │
    ├── 📂 src/                            # Source code
    │   │
    │   ├── 📂 js/                         # JavaScript
    │   │   ├── api.js                     # Cliente REST (APIClient)
    │   │   │                              # - getStandings()
    │   │   │                              # - getAllTeams()
    │   │   │                              # - recordMatch()
    │   │   │                              # - healthCheck()
    │   │   │
    │   │   └── app.js                     # Controlador principal
    │   │                                  # - Navegação entre views
    │   │                                  # - loadStandings()
    │   │                                  # - loadTeams()
    │   │                                  # - Form de partida
    │   │                                  # - Requisições REST
    │   │
    │   └── 📂 css/                        # Estilos
    │       └── style.css                  # CSS3 Responsivo
    │                                      # - Grid Layout
    │                                      # - Flexbox
    │                                      # - Mobile-first
    │                                      # - Tema gradient
    │
    ├── 📄 package.json                    # Configuração npm
    │                                      # - Scripts (dev, start)
    │                                      # - Informações do projeto
    │
    ├── 📄 vercel.json                     # Deploy na Vercel
    │                                      # - Build config
    │                                      # - Output directory
    │
    └── 📄 README.md                       # Documentação do front-end
```

---

## 📊 RESUMO DA ESTRUTURA

### Organização por Arquitetura

#### **CAMADA DE DOMÍNIO** (Models)
```
backend/app/models/team.py
├── Team (Entidade)
│   ├── properties: id, name, wins, draws, losses, goals_for, goals_against
│   ├── calculated properties:
│   │   ├── points
│   │   ├── games_played
│   │   └── goal_difference
│   └── methods:
│       └── to_dict()
```

#### **CAMADA DE SERVIÇO** (Business Logic)
```
backend/app/services/league_service.py
├── LeagueService
│   ├── get_league_standings() - Retorna times ordenados
│   ├── record_match() - Registra partida, atualiza stats
│   └── get_team_statistics() - Calcula estatísticas
```

#### **CAMADA DE ACESSO A DADOS** (Repository + DB)
```
backend/app/database/
├── db.py
│   ├── init_db() - Cria tabelas
│   ├── get_db_connection()
│   └── Dados mock (Íbis, Sampaio Corrêa, Bayern de Belford Roxo, etc)
│
└── team_repository.py (Repository Pattern)
    ├── get_all_teams()
    ├── get_team_by_id()
    ├── update_team()
    └── create_team()
```

#### **CAMADA DE APRESENTAÇÃO** (Routes + Views)
```
backend/app/routes/teams.py (Controllers REST)
├── @router.get("/standings")
├── @router.get("/all")
├── @router.get("/{team_id}")
├── @router.post("/match")
└── @router.get("/health/check")

frontend/public/index.html (HTML/CSS/JS View)
├── Tabela de Standings
├── Cards de Times
├── Form de Partida
└── Info Sobre
```

---

## 🔄 FLUXO DE DADOS

```
┌─────────────────────────────────────────────────────────────────┐
│  FRONT-END (HTML/CSS/JS)                                         │
│  ├── Clica em "Carregar Tabela"                                 │
│  └── fetch("/api/teams/standings")                              │
└──────────────────────┬──────────────────────────────────────────┘
                       │ HTTP GET
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  BACK-END - ROUTES (teams.py - Controller)                      │
│  ├── @router.get("/standings")                                  │
│  └── standings = LeagueService.get_league_standings()           │
│      return standings                                            │
└──────────────────────┬──────────────────────────────────────────┘
                       │ Delega para Service
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  BACK-END - SERVICES (league_service.py)                        │
│  ├── teams = TeamRepository.get_all_teams()                     │
│  ├── Aplica lógica de ordenação:                                │
│  │   1. Por pontos (vitória=3, empate=1)                        │
│  │   2. Por saldo de gols                                       │
│  │   3. Por gols a favor                                        │
│  └── return [Team, Team, ...] ordenados                         │
└──────────────────────┬──────────────────────────────────────────┘
                       │ Solicita dados
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  BACK-END - REPOSITORY (team_repository.py)                     │
│  ├── Executa SQL: SELECT * FROM teams                           │
│  ├── Mapeia rows para objetos Team                              │
│  └── return [Team, Team, ...]                                   │
└──────────────────────┬──────────────────────────────────────────┘
                       │ Acessa
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  BANCO DE DADOS (SQLite - ligascore.db)                        │
│  ├── Table: teams                                               │
│  │   id | name | wins | draws | losses | goals_for | goals_ag  │
│  │  1  | Íbis |  2   |  3    |   5    |     8      |    15      │
│  │  2  | Sampaio Corrêa | 4 |  2    |   4    |    12     |    10 │
│  │  3  | Bayern de Belford Roxo | 6 | 1 | 3 | 18 | 8          │
│  │  ...                                                          │
│  └── response: [rows]                                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📈 FLUXO DE TIMES NA LIGA FICTÍCIA

```
TIMES INICIAIS (pré-carregados):

1. Íbis                        - 2V 3E 5D | 8GF 15GA | 9pts
2. Sampaio Corrêa              - 4V 2E 4D | 12GF 10GA | 14pts
3. Bayern de Belford Roxo      - 6V 1E 3D | 18GF 8GA | 19pts (LIDER)
4. Asa de Arapiraca            - 3V 2E 5D | 10GF 14GA | 11pts
5. Tabajara FC                 - 5V 3E 2D | 16GF 9GA | 18pts
6. Merden Bocard               - 1V 1E 8D | 5GF 20GA | 4pts

USUÁRIO REGISTRA PARTIDA (Bayern 2x1 Tabajara):
│
├─ Bayern: vitória, +1W, +2GF, +1GA = 7V 1E 3D | 20GF 9GA | 22pts
├─ Tabajara: derrota, +1D, +1GF, +2GA = 5V 3E 3D | 17GF 11GA | 18pts
│
└─ NOVA TABELA (re-ordenada):
   1. Bayern de Belford Roxo      - 22pts ✓ NOVO LÍDER
   2. Tabajara FC                 - 18pts
   3. Sampaio Corrêa              - 14pts
   4. Asa de Arapiraca            - 11pts
   5. Íbis                        - 9pts
   6. Merden Bocard               - 4pts
```

---

## 📋 MAPEAMENTO MVC

| Componente MVC | Implementação | Arquivo/Classe |
|---|---|---|
| **Model** | Entidade Team | `app/models/team.py` |
| **View** | Interface HTML | `frontend/public/index.html` |
| **Controller** | Rotas REST | `app/routes/teams.py` |

## 🏗️ MAPEAMENTO CAMADAS

| Camada | Responsabilidade | Arquivo |
|---|---|---|
| **Domínio** | Entidades, regras inerentes | `app/models/` |
| **Serviço** | Lógica de negócio complexa | `app/services/league_service.py` |
| **Repositório** | Abstração de persistência | `app/database/team_repository.py` |
| **Apresentação** | HTTP REST + HTML/CSS/JS | `app/routes/` + `frontend/` |

---

## 🚀 COMANDOS PARA EXECUTAR

### Back-End
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

### Front-End
```bash
cd frontend
python -m http.server 5173
```

---

**Estrutura gerada para LigaScore - Projeto Acadêmico**
