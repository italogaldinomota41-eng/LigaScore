"""
Settings Configuration
Define variáveis de ambiente e configurações da aplicação.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Configurações da aplicação"""
    
    # Servidor
    APP_NAME: str = "LigaScore - Brasileirão Série Z - A Liga dos Bagres (LigaScore)"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    
    # Banco de dados
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite:///./ligascore.db"
    )
    
    # CORS (para permitir requisições do front-end)
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8080",
        "https://ligascore-frontend.vercel.app",
        "*",  # Em produção, remover e especificar domínios
    ]

settings = Settings()
