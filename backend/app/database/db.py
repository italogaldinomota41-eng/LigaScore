"""
Database Configuration
Inicializa o banco SQLite e os dados mock iniciais.
"""
import sqlite3
from pathlib import Path
import os

DATABASE_URL = "sqlite:///./ligascore.db"
DB_PATH = Path(__file__).parent.parent.parent / "ligascore.db"

def get_db_connection():
    """Retorna uma conexão com o banco de dados SQLite"""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

def init_db():
    """
    Inicializa o banco de dados e cria a tabela de times
    com dados mock pré-carregados (Íbis, Sampaio Corrêa, etc.)
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Criar tabela teams
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            wins INTEGER DEFAULT 0,
            draws INTEGER DEFAULT 0,
            losses INTEGER DEFAULT 0,
            goals_for INTEGER DEFAULT 0,
            goals_against INTEGER DEFAULT 0
        )
    """)

    # Criar tabela matches para armazenar histórico de partidas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team1_id INTEGER NOT NULL,
            team2_id INTEGER NOT NULL,
            team1_goals INTEGER NOT NULL,
            team2_goals INTEGER NOT NULL,
            events TEXT,
            played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(team1_id) REFERENCES teams(id),
            FOREIGN KEY(team2_id) REFERENCES teams(id)
        )
    """)
    
    # Inserir 20 times oficiais da versão 2.0
    mock_teams = [
        ("Íbis", 0, 0, 0, 0, 0),
        ("Sampaio Corrêa", 0, 0, 0, 0, 0),
        ("Afogados da Ingazeira", 0, 0, 0, 0, 0),
        ("Sousa", 0, 0, 0, 0, 0),
        ("Globo FC", 0, 0, 0, 0, 0),
        ("4 de Julho", 0, 0, 0, 0, 0),
        ("Trem", 0, 0, 0, 0, 0),
        ("Tuna Luso", 0, 0, 0, 0, 0),
        ("Tocantinópolis", 0, 0, 0, 0, 0),
        ("Princesa do Solimões", 0, 0, 0, 0, 0),
        ("São Raimundo", 0, 0, 0, 0, 0),
        ("Real Noroeste", 0, 0, 0, 0, 0),
        ("Nova Venécia", 0, 0, 0, 0, 0),
        ("Ceilândia", 0, 0, 0, 0, 0),
        ("Nova Mutum", 0, 0, 0, 0, 0),
        ("Camboriú", 0, 0, 0, 0, 0),
        ("Campinense", 0, 0, 0, 0, 0),
        ("Maringá", 0, 0, 0, 0, 0),
        ("Altos", 0, 0, 0, 0, 0),
        ("Caucaia", 0, 0, 0, 0, 0),
    ]
    
    cursor.execute("SELECT COUNT(*) FROM teams")
    teams_count = cursor.fetchone()[0]

    if teams_count == 0:
        for name, wins, draws, losses, goals_for, goals_against in mock_teams:
            cursor.execute("""
                INSERT INTO teams (name, wins, draws, losses, goals_for, goals_against)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, wins, draws, losses, goals_for, goals_against))
    
    conn.commit()
    conn.close()

# Inicializar banco na importação
if not DB_PATH.exists():
    init_db()
