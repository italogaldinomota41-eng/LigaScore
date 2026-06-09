# 🏆 LigaScore - Plataforma de Estatísticas de Futebol

Projeto acadêmico de Arquitetura de Software: uma plataforma completa para gerenciar estatísticas de uma liga fictícia de futebol.

## 📋 Visão Geral

**LigaScore** é uma aplicação web moderna que gerencia uma liga completamente caótica com 6 times fictícios: Íbis, Sampaio Corrêa, Bayern de Belford Roxo, Asa de Arapiraca, Tabajara FC e Merden Bocard.

A plataforma foi desenvolvida seguindo rigorosamente os padrões de arquitetura **MVC (Model-View-Controller)** e **Camadas (Layers)**, com separação física e lógica entre front-end e back-end.

## 🏗️ Arquitetura

```
LigaScore/
├── backend/                 # API REST - FastAPI + SQLite
│   ├── app/
│   │   ├── models/          # Camada de Domínio
│   │   │   └── team.py
│   │   ├── routes/          # Camada de Apresentação (Controllers)
│   │   │   └── teams.py
│   │   ├── services/        # Camada de Negócio
│   │   │   └── league_service.py
│   │   ├── database/        # Camada de Acesso a Dados
│   │   │   ├── db.py
│   │   │   └── team_repository.py
│   │   ├── config/
│   │   │   └── settings.py
│   │   └── main.py
│   ├── requirements.txt
│   ├── Procfile             # Deploy Railway
│   └── .env
│
└── frontend/                # Interface Web - HTML/CSS/JS
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── js/
    │   │   ├── api.js       # Cliente REST
    │   │   └── app.js       # Controlador
    │   └── css/
    │       └── style.css
    ├── package.json
    ├── vercel.json          # Deploy Vercel
    └── README.md
```

## 🎯 Stack Tecnológico

### Back-End
- **Framework**: FastAPI (Python)
- **Banco de Dados**: SQLite (arquivo local)
- **Server**: Uvicorn
- **Padrão**: MVC + Camadas (Layers)

### Front-End
- **Linguagem**: HTML5, CSS3, JavaScript (ES6+)
- **Estilo**: CSS Grid, Flexbox, responsivo
- **Comunicação**: Fetch API (REST)
- **Design**: Mobile-first

## 🚀 Executar Localmente

### Back-End

```bash
cd backend

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar servidor
python -m uvicorn app.main:app --reload --port 8000
```

API: `http://localhost:8000`
Docs: `http://localhost:8000/docs`

### Front-End

```bash
cd frontend

# Opção 1: Python
python -m http.server 5173

# Opção 2: Node.js
npm start

# Opção 3: Abrir arquivo diretamente
# Abrir public/index.html no navegador
```

Front-End: `http://localhost:5173`

## 📡 Endpoints da API

### Teams (Times)
```
GET    /api/teams/standings     Tabela do campeonato ordenada
GET    /api/teams/all           Lista de todos os times
GET    /api/teams/{team_id}     Detalhes e estatísticas de um time
POST   /api/teams/match         Registrar resultado de partida
GET    /api/teams/health/check  Health check
```

### Gerais
```
GET    /                        Info da API
GET    /health                  Health check geral
```

## 📊 Dados Iniciais

A plataforma é pré-carregada com 6 times fictícios:

| Time | V | E | D | GF | GA |
|------|---|---|---|----|-----|
| Íbis | 2 | 3 | 5 | 8 | 15 |
| Sampaio Corrêa | 4 | 2 | 4 | 12 | 10 |
| Bayern de Belford Roxo | 6 | 1 | 3 | 18 | 8 |
| Asa de Arapiraca | 3 | 2 | 5 | 10 | 14 |
| Tabajara FC | 5 | 3 | 2 | 16 | 9 |
| Merden Bocard | 1 | 1 | 8 | 5 | 20 |

## ☁️ Deploy em Nuvem

### Back-End no Railway

1. Fazer push para GitHub
2. Conectar repositório no [Railway.app](https://railway.app)
3. Railway detectará `Procfile` automaticamente
4. Deploy realizado!

**Procfile**:
```
web: cd backend && python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Front-End na Vercel

1. Fazer push para GitHub
2. Conectar repositório no [Vercel](https://vercel.com)
3. Configurar:
   - Build Command: `npm run build`
   - Output Directory: `public`
4. Adicionar variável de ambiente:
   - `VITE_API_URL`: URL da API no Railway
5. Deploy automático!

## 🎓 Requisitos Acadêmicos

### ✅ MVC (Model-View-Controller)
- **Models**: Entidade `Team` em `app/models/team.py`
- **Views**: Front-end em `frontend/public/index.html`
- **Controllers**: Rotas em `app/routes/teams.py`

### ✅ Camadas (Layers)
1. **Camada de Domínio**: Modelos com regras de negócio
2. **Camada de Serviço**: `LeagueService` com lógica de campeonato
3. **Camada de Acesso a Dados**: `TeamRepository` abstrai o banco
4. **Camada de Apresentação**: Routes REST que delegam para Services

### ✅ REST API
- Endpoints HTTP com métodos corretos (GET, POST)
- Comunicação via JSON
- Stateless, baseado em recurso

### ✅ Separação Front/Back
- Front-end isolado em pasta separada
- Back-end totalmente independente
- Front-end acessa dados apenas via API REST

### ✅ Cloud-Ready
- `requirements.txt` para dependências Python
- `Procfile` para Railway
- `vercel.json` para Vercel
- Configuração via variáveis de ambiente

## 📁 Estrutura de Diretórios

```
/home/italo-mota/LigaScore/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── team.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── teams.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── league_service.py
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── db.py
│   │   │   └── team_repository.py
│   │   └── config/
│   │       ├── __init__.py
│   │       └── settings.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── .env
│   └── README.md
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── js/
│   │   │   ├── api.js
│   │   │   └── app.js
│   │   └── css/
│   │       └── style.css
│   ├── package.json
│   ├── vercel.json
│   └── README.md
└── README.md (este arquivo)
```

## 🔐 Variáveis de Ambiente

### Back-End (`.env`)
```
DEBUG=True
HOST=0.0.0.0
PORT=8000
DATABASE_URL=sqlite:///./ligascore.db
```

### Front-End (`.env.local` - opcional)
```
VITE_API_URL=http://localhost:8000
```

## 🧪 Testar a Aplicação

### CURL

```bash
# Obter tabela do campeonato
curl -X GET "http://localhost:8000/api/teams/standings"

# Registrar partida
curl -X POST "http://localhost:8000/api/teams/match" \
  -H "Content-Type: application/json" \
  -d '{"team1_id":1,"team2_id":2,"team1_goals":3,"team2_goals":1}'
```

### Swagger UI
Acesse `http://localhost:8000/docs` para testar endpoints interativamente.

## 📝 Notas Importantes

- O banco de dados SQLite é criado automaticamente na primeira execução
- O front-end consome a API via CORS
- A aplicação está configurada para CORS permissivo em desenvolvimento
- Em produção, especificar domínios permitidos

## 👨‍💻 Autores

Desenvolvido como projeto acadêmico de Arquitetura de Software.

## 📄 Licença

MIT

---

**LigaScore** © 2024 | Plataforma de Estatísticas de Futebol
