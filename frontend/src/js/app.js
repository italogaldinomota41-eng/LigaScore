/**
 * App v3 - Controlador Principal do Front-End
 * Tabela compacta, zonas coloridas por posicao e formulario de partida lado a lado.
 */

const navButtons = document.querySelectorAll('.nav-btn');
const views = document.querySelectorAll('.view');
const standingsTable = document.getElementById('standings-table');
const standingsBody = document.getElementById('standings-body');
const standingsLoading = document.getElementById('standings-loading');
const standingsError = document.getElementById('standings-error');
const matchForm = document.getElementById('match-form');
const team1Select = document.getElementById('team1');
const team2Select = document.getElementById('team2');
const matchMessage = document.getElementById('match-message');
const score1El = document.getElementById('score1');
const score2El = document.getElementById('score2');
const eventsEl = document.getElementById('events');
const modal = document.getElementById('team-modal');
const modalClose = modal ? modal.querySelector('.modal-close') : null;

document.addEventListener('DOMContentLoaded', () => {
  setupNavigation();
  setupScoreButtons();
  setupModal();
  loadStandings();
  loadTeamsForSelects();
});

function setupNavigation() {
  navButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const view = btn.dataset.view;

      navButtons.forEach((button) => button.classList.remove('active'));
      btn.classList.add('active');

      views.forEach((section) => section.classList.remove('active'));
      document.getElementById(`${view}-view`).classList.add('active');

      if (view === 'standings') {
        loadStandings();
      }
    });
  });
}

async function loadStandings() {
  standingsLoading.style.display = 'block';
  standingsTable.style.display = 'none';
  standingsError.style.display = 'none';

  try {
    const standings = await api.getStandings();

    if (!Array.isArray(standings)) {
      throw new Error('Resposta invalida da API.');
    }

    standingsBody.innerHTML = '';

    standings.forEach((team, index) => {
      const position = team.position || index + 1;
      const tr = document.createElement('tr');
      tr.classList.add(getClassificationClass(index));
      tr.tabIndex = 0;
      tr.title = `Abrir detalhes de ${team.name}`;

      tr.innerHTML = `
        <td class="position">${position}º</td>
        <td class="team-name">${team.name}</td>
        <td><strong>${team.points}</strong></td>
        <td>${team.games_played}</td>
        <td>${team.wins}</td>
        <td>${team.draws}</td>
        <td>${team.losses}</td>
        <td>${team.goals_for}</td>
        <td>${team.goals_against}</td>
        <td>${formatGoalDifference(team.goal_difference)}</td>
      `;

      tr.addEventListener('click', () => openTeamModal(team.id));
      tr.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          openTeamModal(team.id);
        }
      });

      standingsBody.appendChild(tr);
    });

    standingsLoading.style.display = 'none';
    standingsTable.style.display = 'table';
  } catch (err) {
    console.error(err);
    standingsLoading.style.display = 'none';
    standingsError.style.display = 'block';
    standingsError.textContent = 'Erro ao carregar a tabela de classificacao.';
  }
}

function getClassificationClass(index) {
  const position = index + 1;

  if (position >= 1 && position <= 4) return 'zone-libertadores';
  if (position >= 5 && position <= 6) return 'zone-pre-libertadores';
  if (position >= 7 && position <= 12) return 'zone-sul-bagricana';
  if (position >= 13 && position <= 16) return 'zone-ferias';
  return 'zone-z4';
}

function formatGoalDifference(goalDifference) {
  const value = Number(goalDifference) || 0;
  return `${value >= 0 ? '+' : ''}${value}`;
}

function setupModal() {
  if (!modal) return;

  if (modalClose) {
    modalClose.addEventListener('click', closeTeamModal);
  }

  const backdrop = modal.querySelector('.modal-backdrop');
  if (backdrop) {
    backdrop.addEventListener('click', closeTeamModal);
  }
}

function closeTeamModal() {
  modal.classList.add('hidden');
}

async function openTeamModal(teamId) {
  try {
    const data = await api.getTeamById(teamId);
    const team = data.team;
    const matches = data.matches || [];

    document.getElementById('modal-team-name').textContent = `${team.name} (#${team.id})`;
    document.getElementById('modal-team-stats').innerHTML = `
      <p>Pontos: <strong>${team.points}</strong> | Jogos: ${team.games_played}</p>
      <p>Vitorias: ${team.wins} | Empates: ${team.draws} | Derrotas: ${team.losses}</p>
      <p>Gols pro: ${team.goals_for} | Gols contra: ${team.goals_against} | SG: ${formatGoalDifference(team.goal_difference)}</p>
    `;

    const list = document.getElementById('modal-team-matches');
    list.innerHTML = '';

    if (matches.length === 0) {
      list.innerHTML = '<li>Nenhuma partida registrada.</li>';
    }

    matches.forEach((match) => {
      const li = document.createElement('li');
      const events = match.events ? ` | ${match.events}` : '';
      li.textContent = `${match.played_at} | #${match.team1_id} ${match.team1_goals} x ${match.team2_goals} #${match.team2_id}${events}`;
      list.appendChild(li);
    });

    modal.classList.remove('hidden');
  } catch (err) {
    console.error(err);
    showMatchMessage('Erro ao carregar detalhes do time.', 'error');
  }
}

async function loadTeamsForSelects() {
  try {
    const teams = await api.getAllTeams();
    team1Select.innerHTML = '<option value="">Selecione um time...</option>';
    team2Select.innerHTML = '<option value="">Selecione um time...</option>';

    teams.forEach((team) => {
      const option1 = document.createElement('option');
      option1.value = team.id;
      option1.textContent = team.name;
      team1Select.appendChild(option1);

      const option2 = document.createElement('option');
      option2.value = team.id;
      option2.textContent = team.name;
      team2Select.appendChild(option2);
    });
  } catch (err) {
    console.error(err);
    showMatchMessage('Nao foi possivel carregar os times.', 'error');
  }
}

function setupScoreButtons() {
  document.querySelectorAll('.score-btn').forEach((button) => {
    button.addEventListener('click', () => {
      const scoreElement = button.dataset.for === '1' ? score1El : score2El;
      const currentScore = Number(scoreElement.textContent) || 0;
      const nextScore = button.classList.contains('inc')
        ? currentScore + 1
        : Math.max(0, currentScore - 1);

      scoreElement.textContent = String(nextScore);
    });
  });
}

matchForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const team1Id = Number(team1Select.value);
  const team2Id = Number(team2Select.value);
  const team1Goals = Number(score1El.textContent);
  const team2Goals = Number(score2El.textContent);
  const events = eventsEl.value.trim();

  if (!team1Id || !team2Id) {
    showMatchMessage('Selecione os dois times da partida.', 'error');
    return;
  }

  if (team1Id === team2Id) {
    showMatchMessage('Escolha times diferentes para registrar a partida.', 'error');
    return;
  }

  try {
    const response = await fetch(`${api.baseURL}/api/teams/match`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        team1_id: team1Id,
        team2_id: team2Id,
        team1_goals: team1Goals,
        team2_goals: team2Goals,
        events: events || null,
      }),
    });

    const result = await response.json().catch(() => ({}));

    if (!response.ok || result.success === false) {
      const detail = result.detail || result.message || 'Erro ao registrar partida.';
      throw new Error(detail);
    }

    showMatchMessage(result.message || 'Partida registrada com sucesso!', 'success');
    resetMatchForm();
    await loadStandings();

    navButtons.forEach((button) => button.classList.remove('active'));
    document.querySelector('[data-view="standings"]').classList.add('active');
    views.forEach((section) => section.classList.remove('active'));
    document.getElementById('standings-view').classList.add('active');
  } catch (err) {
    console.error(err);
    showMatchMessage(err.message || 'Erro ao registrar partida.', 'error');
  }
});

function resetMatchForm() {
  score1El.textContent = '0';
  score2El.textContent = '0';
  eventsEl.value = '';
  team1Select.value = '';
  team2Select.value = '';
}

function showMatchMessage(text, type) {
  matchMessage.textContent = text;
  matchMessage.className = `message ${type}`;
  matchMessage.style.display = 'block';

  setTimeout(() => {
    matchMessage.style.display = 'none';
  }, 4500);
}

async function checkAPIHealth() {
  try {
    await api.healthCheck();
  } catch (err) {
    console.warn('API offline', err);
  }
}

checkAPIHealth();
