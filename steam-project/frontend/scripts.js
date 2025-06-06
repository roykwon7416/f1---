const apiBase = 'http://localhost:8000/api';

async function loadGenres() {
    const res = await fetch(`${apiBase}/top-games`);
    const games = await res.json();
    const genres = [...new Set(games.map(g => g.genre))].sort();
    const genreSelect = document.getElementById('genre');
    genres.forEach(g => {
        const opt = document.createElement('option'); opt.value = g; opt.textContent = g;
        genreSelect.appendChild(opt);
    });
}

async function loadGames() {
    const selected = Array.from(document.getElementById('genre').selectedOptions).map(o => o.value);
    const minTime = document.getElementById('minTime').value;
    const params = new URLSearchParams();
    selected.forEach(g => params.append('genres', g));
    params.set('min_time', minTime);
    const res = await fetch(`${apiBase}/games?${params}`);
    const games = await res.json();
    const tbody = document.querySelector('#gameList tbody');
    tbody.innerHTML = '';
    games.forEach(g => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${g.appid}</td><td>${g.name}</td><td>${g.genre}</td><td>${g.owners.toLocaleString()}</td><td>${g.players_2weeks.toLocaleString()}</td><td>${g.average_playtime.toLocaleString()}</td>`;
        tbody.appendChild(tr);
    });
}

document.getElementById('applyFilters').addEventListener('click', loadGames);
window.addEventListener('DOMContentLoaded', async () => { await loadGenres(); await loadGames(); });