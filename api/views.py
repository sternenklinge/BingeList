from django.shortcuts import render
import tmdbsimple as tmdb

tmdb.API_KEY = '300659883e7e07b8afd0aec7dbf8e802'
tmdb.REQUESTS_TIMEOUT = 10

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')

def search_results(request):
    query = request.GET.get('query')
    search = tmdb.Search()
    response = search.movie(query=query, language='de')
    movies = search.results
    response = search.tv(query=query, language='de')
    tv_shows = search.results
    return render(request, 'search_results.html', {'movies': movies, 'tv_shows': tv_shows})

def discover(request):
    discover = tmdb.Discover()
    response = discover.movie(language='de',sort_by='popularity.desc')
    movies = discover.results
    response = discover.tv(language='de',sort_by='popularity.desc')
    tv_shows = discover.results
    return render(request, 'discover.html', {'movies': movies, 'tv_shows': tv_shows})

def add_to_watchlist(request, movie_id):
    movie = tmdb.Movies(movie_id)
    movie_info = movie.info()
    watchlist_movie = Watchlist(
        title=movie_info['title'],
        release_date=movie_info['release_date'],
        overview=movie_info['overview'],
        poster_path=movie_info['poster_path'],
        )
    watchlist_movie.save()
    return redirect('watchlist.html')
