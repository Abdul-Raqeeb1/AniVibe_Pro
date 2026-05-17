document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('toggle-btn');
    const siteLogo = document.getElementById('site-logo');
    const heroTitle = document.getElementById('hero-title');
    const searchInput = document.getElementById('search-input');
    const body = document.body;
    
    // NEW SELECTOR FOR 3D IMAGE POSTER
    const floatingPoster = document.getElementById('floating-poster');

    // DUMMY POSTER URLS FOR TESTING
    const ANIME_POSTER_URL = "/static/image/2.jpeg"
    const MOVIE_POSTER_URL = "/static/image/3.jpg"; // Spider-Verse

    let isMovieMode = false;

    toggleBtn.addEventListener('click', () => {
        isMovieMode = !isMovieMode;
        
        if (isMovieMode) {
            // SWITCHING TO MOVIE MODE
            body.classList.add('movie-mode');
            toggleBtn.innerText = "Switch to Anime";
            siteLogo.innerText = "CINEVIBE";
            heroTitle.innerHTML = 'Discover Top <span style="color: var(--accent-color);">Movies</span>';
            searchInput.placeholder = "Search for Movies...";
            
            // 🔥 NEW: Dynamically swap the image source to Movie Poster
            floatingPoster.src = MOVIE_POSTER_URL;
            floatingPoster.alt = "Spider-Man Poster";

        } else {
            // SWITCHING BACK TO ANIME MODE
            body.classList.remove('movie-mode');
            toggleBtn.innerText = "Switch to Movies";
            siteLogo.innerText = "ANIVIBE";
            heroTitle.innerHTML = 'Discover Top <span style="color: var(--accent-color);">Anime</span>';
            searchInput.placeholder = "Search for Anime...";
            
            // 🔥 NEW: Dynamically swap back to Anime Poster
            floatingPoster.src = ANIME_POSTER_URL;
            floatingPoster.alt = "Jujutsu Kaisen Poster";
        }
    });
});