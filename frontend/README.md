# LigaScore Frontend

Front-end para a Plataforma de Estatísticas de Futebol

## Sobre

Aplicação web responsiva desenvolvida em HTML/CSS/JavaScript puro. Consome a API REST do back-end para exibir dados de times e tabela de campeonato.

## Stack

- **HTML5**: Estrutura e semântica
- **CSS3**: Estilos responsivos com Grid e Flexbox
- **JavaScript (ES6+)**: Consumo de API REST com Fetch API
- **Design Responsivo**: Mobile-first

## Executar Localmente

```bash
# Método 1: Python
python -m http.server 5173

# Método 2: Node.js (se npm estiver instalado)
npm start

# Método 3: Abrir diretamente no navegador
# Abrir frontend/public/index.html
```

Acesse em `http://localhost:5173` (ou a porta escolhida)

## Estrutura de Pastas

```
frontend/
├── public/
│   └── index.html        # Arquivo principal
├── src/
│   ├── js/
│   │   ├── api.js        # Cliente REST
│   │   └── app.js        # Controlador principal
│   └── css/
│       └── style.css     # Estilos
├── package.json
├── vercel.json           # Config Vercel
└── README.md
```

## Funcionalidades

- ✓ Visualizar tabela do campeonato
- ✓ Listar todos os times com estatísticas
- ✓ Registrar resultado de partidas
- ✓ Visualizar detalhes de times individuais
- ✓ Interface responsiva e intuitiva

## Endpoints da API

A aplicação consome os seguintes endpoints:

- `GET /api/teams/standings` - Tabela do campeonato
- `GET /api/teams/all` - Lista de times
- `GET /api/teams/{id}` - Detalhes de um time
- `POST /api/teams/match` - Registrar partida

## Deploy na Vercel

1. Fazer push para GitHub
2. Conectar repositório na Vercel
3. Configurar:
   - **Build Command**: `npm run build`
   - **Output Directory**: `public`
4. Deploy automático

## Variáveis de Ambiente

Criar arquivo `.env.local` na raiz:

```
VITE_API_URL=https://api-backend.railway.app
```

## Requisitos do Projeto Acadêmico

✓ **MVC - View**: O front-end implementa a camada de Visão do MVC
✓ **Separação Front/Back**: Aplicação isolada que consome apenas API REST
✓ **REST API**: Todas as requisições via fetch com HTTP methods
✓ **Responsivo**: CSS Grid e Flexbox para adaptação a dispositivos
✓ **Cloud-Ready**: Pronto para Vercel com vercel.json

## Autores

Desenvolvido como projeto acadêmico de Arquitetura de Software
