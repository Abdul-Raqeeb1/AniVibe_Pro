import requests
from django.shortcuts import render, HttpResponse ,get_object_or_404
from .models import Show
from django.http import JsonResponse

TMDB_API_KEY = 'b70551e28f4fd7d27b9d3592e5a79e30'

def home_page(request):
    query = request.GET.get('q')
    
    if query:
        movies = Show.objects.filter(show_type='MOVIE', title__icontains=query).order_by('-rating')
        animes = Show.objects.filter(show_type='ANIME', title__icontains=query).order_by('-rating')
    else:
        movies = Show.objects.filter(show_type='MOVIE').order_by('-rating')
        animes = Show.objects.filter(show_type='ANIME').order_by('-rating')
    
    context = {
        'movies': movies,
        'animes': animes
    }
    return render(request, 'home.html', context)

def fetch_trending_data(request):
    # 1. Purana Data Saaf Karna
    Show.objects.all().delete()
    
    # 2. URLs
    movie_url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={TMDB_API_KEY}"
    anime_url = f"https://api.themoviedb.org/3/discover/tv?api_key={TMDB_API_KEY}&with_original_language=ja&with_genres=16&sort_by=popularity.desc"
    
    # 3. MOVIE DATA FETCH
    response_movies = requests.get(movie_url)
    if response_movies.status_code == 200:
        for item in response_movies.json().get('results', []):
            if item.get('poster_path'):
                Show.objects.create(
                    tmdb_id=item['id'],
                    title=item.get('title') or item.get('name'),
                    show_type='MOVIE',
                    poster_url=f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}",
                    rating=item.get('vote_average', 0.0),
                    release_date=item.get('release_date') or None,
                    description=item.get('overview') or ''
                    )

    # 4. ANIME DATA FETCH
    response_anime = requests.get(anime_url)
    if response_anime.status_code == 200:
        for item in response_anime.json().get('results', []):
            if item.get('poster_path'):
                Show.objects.create(
                    tmdb_id=item['id'] + 1000000, 
                    title=item.get('title') or item.get('name'),
                    show_type='ANIME',
                    poster_url=f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}",
                    rating=item.get('vote_average', 0.0),
                    release_date=item.get('first_air_date') or None,
                    description=item.get('overview') or ''
                )
    return HttpResponse("Masla Hal! Purana data delete ho gaya aur Fresh Movies/Anime save ho gaye hain!")


def search_suggestions(request):
    query = request.GET.get('q','')
    if query :
        shows = Show.objects.filter(title__icontains=query).values_list('title',flat=True)[:5]
        return JsonResponse({'suggestions' : list(shows)})
    return JsonResponse({'suggestions':[]})

def show_detail(request, id):
    # Database se movie nikalo jiski ID match kare
    show = get_object_or_404(Show, id=id)
    
    context = {
        'show': show
    }
    return render(request, 'catalog/detail.html', context)