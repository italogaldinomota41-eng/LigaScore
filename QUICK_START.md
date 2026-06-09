# ⚡ QUICK START GUIDE - FLASHSCORE

**Inicie a aplicação em menos de 5 minutos!**

---

## 🚀 PARTE 1: INICIAR BACK-END

### Terminal 1 (Back-end)

```bash
# 1. Navegar para pasta backend
cd /home/italo-mota/LigaScore/backend

# 2. Criar ambiente virtual
python3 -m venv venv

# 3. Ativar ambiente (Linux/Mac)
source venv/bin/activate

# OU se estiver no Windows:
# venv\Scripts\activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Executar servidor
python -m uvicorn app.main:app --reload --port 8000
```

**Esperado:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

✅ **Back-end pronto!**

---

## 🎨 PARTE 2: INICIAR FRONT-END

### Terminal 2 (Front-end)

```bash
# 1. Abrir nova aba/janela do terminal

# 2. Navegar para pasta frontend
cd /home/italo-mota/LigaScore/frontend

# 3. Executar servidor HTTP
python -m http.server 5173
```

**Esperado:**
```
Serving HTTP on 0.0.0.0 port 5173 (http://0.0.0.0:5173/) ...
```

✅ **Front-end pronto!**

---

## 🌐 PARTE 3: ACESSAR APLICAÇÃO

### Abra seu navegador:

| Link | Descrição |
|------|-----------|
| http://localhost:5173 | 🎨 **Interface web** (use esta!) |
| http://localhost:8000 | 📡 API REST (info técnica) |
| http://localhost:8000/docs | 📚 **Swagger UI** (testar endpoints) |
| http://localhost:8000/redoc | 📖 ReDoc (documentação alternativa) |

---

## 🧪 PARTE 4: TESTAR A APLICAÇÃO

### No Navegador (Recomendado)

1. Abra http://localhost:5173
2. Clique em "Tabela" → Veja standings
3. Clique em "Registrar Partida"
4. Selecione dois times
5. Digite gols (ex: Bayern 2 x 1 Tabajara)
6. Clique "Registrar Partida"
7. Volte para "Tabela" → Veja posições atualizadas!

### Via Terminal (CURL)

```bash
# Obter tabela
curl -X GET "http://localhost:8000/api/teams/standings" | python -m json.tool

# Registrar partida
curl -X POST "http://localhost:8000/api/teams/match" \
  -H "Content-Type: application/json" \
  -d '{"team1_id":3,"team2_id":5,"team1_goals":2,"team2_goals":1}'

# Obter detalhes de um time
curl -X GET "http://localhost:8000/api/teams/3" | python -m json.tool

# Health check
curl -X GET "http://localhost:8000/health" | python -m json.tool
```

### Via Swagger UI

1. Abra http://localhost:8000/docs
2. Encontre "POST /api/teams/match"
3. Clique "Try it out"
4. Preencha:
   ```json
   {
     "team1_id": 1,
     "team2_id": 2,
     "team1_goals": 3,
     "team2_goals": 1
   }
   ```
5. Clique "Execute"
6. Veja resposta em tempo real

---

## 📊 ESTRUTURA CRIADA

```
LigaScore/
├── backend/
│   ├── app/models/team.py              (Modelos)
│   ├── app/services/league_service.py  (Lógica)
│   ├── app/database/team_repository.py (Dados)
│   ├── app/routes/teams.py             (APIs)
│   ├── app/main.py                     (App)
│   ├── requirements.txt                (Dependências)
│   └── Procfile                        (Deploy)
│
└── frontend/
    ├── public/index.html               (UI)
    ├── src/js/api.js                   (Cliente REST)
    ├── src/js/app.js                   (Controller)
    └── src/css/style.css               (Estilos)
```

---

## 🎯 DADOS INICIAIS

**6 times fictícios já carregados:**

| Time | V | E | D | PTS | SG |
|------|---|---|---|-----|-----|
| Bayern de Belford Roxo | 6 | 1 | 3 | **19** | +10 |
| Tabajara FC | 5 | 3 | 2 | 18 | +7 |
| Sampaio Corrêa | 4 | 2 | 4 | 14 | +2 |
| Asa de Arapiraca | 3 | 2 | 5 | 11 | -4 |
| Íbis | 2 | 3 | 5 | 9 | -7 |
| Merden Bocard | 1 | 1 | 8 | 4 | -15 |

---

## 🔌 ENDPOINTS DISPONÍVEIS

```
GET    /api/teams/standings      Tabela ordenada
GET    /api/teams/all            Todos os times
GET    /api/teams/{id}           Detalhes de 1 time
POST   /api/teams/match          Registrar partida
GET    /health                   Health check
```

---

## 🛑 PARAR A APLICAÇÃO

```bash
# Terminal 1 (Back-end)
CTRL + C

# Terminal 2 (Front-end)
CTRL + C

# Desativar ambiente virtual
deactivate
```

---

## ❌ TROUBLESHOOTING

### Porta 5173 já em uso
```bash
# Usar porta diferente
python -m http.server 8888

# Acessar em http://localhost:8888
```

### Porta 8000 já em uso
```bash
# Usar porta diferente
python -m uvicorn app.main:app --reload --port 8001
```

### Módulos não encontrados
```bash
# Verificar ambiente ativado
which python  # Deve estar em venv/

# Reinstalar dependências
pip install -r requirements.txt --force-reinstall
```

### SQLite não encontrado
```bash
# Banco será criado automaticamente na primeira execução
# Se não funcionar, criar manualmente:
rm -f ligascore.db
python -c "from app.database.db import init_db; init_db()"
```

---

## 📝 EXEMPLO DE FLUXO COMPLETO

```bash
# 1. Back-end rodando em terminal 1
# (você já iniciou acima)

# 2. Front-end rodando em terminal 2
# (você já iniciou acima)

# 3. Abrir navegador
firefox http://localhost:5173

# 4. Ver tabela atual
# (Clique em "Tabela" no menu)

# 5. Registrar uma partida
# Clique "Registrar Partida"
# Selecione "Bayern de Belford Roxo"
# Digite "3" gols
# Selecione "Íbis"
# Digite "0" gols
# Clique "Registrar Partida"

# 6. Ver tabela atualizada
# Volta em "Tabela"
# Bayern agora tem 22 pontos (6V+1 = 7V)
# Tabela re-ordenada automaticamente
```

---

## 📚 DOCUMENTAÇÃO IMPORTANTE

| Arquivo | Para |
|---------|------|
| `README.md` | Visão geral |
| `ARQUITETURA_JUSTIFICATIVA.md` | **Sua apresentação** ⭐ |
| `backend/README.md` | Detalhes técnicos back-end |
| `frontend/README.md` | Detalhes técnicos front-end |
| `API_REFERENCE.md` | Exemplos de requisições |
| `ESTRUTURA_PASTAS.md` | Arquitetura visual |

---

## ✨ CARACTERÍSTICAS

✅ MVC Pattern  
✅ Arquitetura em Camadas  
✅ REST API Completa  
✅ Dados Mock Pré-carregados  
✅ Interface Responsiva  
✅ Pronto para Cloud (Railway + Vercel)  
✅ Documentação Automática (Swagger UI)  

---

## 🎓 PARA SUA DEFESA

1. **Copie este trecho** (em `ARQUITETURA_JUSTIFICATIVA.md`):
   ```
   3 parágrafos sobre MVC e Camadas
   ```

2. **Execute a aplicação** (este guia)

3. **Mostre funcionando**:
   - Tabela do campeonato
   - Registrar partida
   - Tabela atualizada

4. **Aponte as camadas**:
   - Models → Services → Repository → Routes

5. **Conclua**:
   - "Este é um projeto de produção com padrões reais"

---

## 🚀 DEPLOYMENT (Opcional)

### Railway (Back-end)
```bash
git push railway main
```

### Vercel (Front-end)
- Conectar GitHub
- Adicionar env: `VITE_API_URL=<railway-url>`
- Deploy automático

---

## 📞 DÚVIDAS?

- **Swagger UI**: http://localhost:8000/docs (testador interativo)
- **Backend README**: `/backend/README.md`
- **Frontend README**: `/frontend/README.md`
- **API Reference**: `API_REFERENCE.md`

---

**⏱️ Tempo total: ~5 minutos para ter aplicação rodando**

**Boa sorte na defesa! 🎓**
