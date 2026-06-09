"""
Main Application - FastAPI
Ponto de entrada da aplicação back-end.
Configura a aplicação, inicializa o banco de dados e registra as rotas.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.database.db import init_db
from app.routes.teams import router as teams_router

# Inicializar banco de dados
init_db()

# Criar aplicação FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API REST para gerenciamento de estatísticas de futebol",
)

# Configurar CORS (permite requisições do front-end)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(teams_router)

# ===== ROTAS GERAIS =====

@app.get("/")
def read_root():
    """
    GET /
    Rota raiz que retorna informações sobre a API.
    """
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "message": "Bem-vindo à API de Estatísticas de Futebol!",
        "endpoints": {
            "standings": "GET /api/teams/standings",
            "all_teams": "GET /api/teams/all",
            "team_details": "GET /api/teams/{team_id}",
            "record_match": "POST /api/teams/match",
            "health": "GET /api/teams/health/check",
            "docs": "GET /docs",
            "redoc": "GET /redoc",
        }
    }

@app.get("/health")
def health_check():
    """
    GET /health
    Endpoint de health check para monitoramento.
    """
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
    }

# ===== EXECUÇÃO =====
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
