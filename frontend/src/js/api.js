/**
 * API Handler
 * Módulo para fazer requisições REST à API do back-end
 */

// URL base da API (fixada para ambiente browser)
const API_URL = "http://localhost:8000";

/**
 * Classe APIClient
 * Encapsula toda lógica de comunicação com a API
 */
class APIClient {
    constructor(baseURL = API_URL) {
        this.baseURL = baseURL;
    }

    /**
     * Método genérico para fazer requisições
     */
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const defaultOptions = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        };

        const finalOptions = { ...defaultOptions, ...options };

        try {
            const response = await fetch(url, finalOptions);

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`API Error: ${endpoint}`, error);
            throw error;
        }
    }

    /**
     * GET /api/teams/standings
     * Obtém a tabela do campeonato
     */
    async getStandings() {
        return this.request('/api/teams/standings');
    }

    /**
     * GET /api/teams/all
     * Obtém lista de todos os times
     */
    async getAllTeams() {
        return this.request('/api/teams/all');
    }

    /**
     * GET /api/teams/{teamId}
     * Obtém detalhes de um time específico
     */
    async getTeamById(teamId) {
        return this.request(`/api/teams/${teamId}`);
    }

    /**
     * POST /api/teams/match
     * Registra resultado de uma partida
     */
    async recordMatch(team1Id, team2Id, team1Goals, team2Goals, events = null) {
        const body = {
            team1_id: team1Id,
            team2_id: team2Id,
            team1_goals: team1Goals,
            team2_goals: team2Goals,
        };
        if (events) body.events = events;

        return this.request('/api/teams/match', {
            method: 'POST',
            body: JSON.stringify(body),
        });
    }

    /**
     * GET /health
     * Verifica se a API está online
     */
    async healthCheck() {
        return this.request('/health');
    }
}

// Instância global do cliente API
const api = new APIClient();

// Exportar para uso nos módulos (se necessário)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { APIClient, api };
}
