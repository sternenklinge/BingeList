from django.shortcuts import render, redirect, HttpResponse
import tmdbsimple as tmdb
from .models import Watchlist

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

def add_to_watchlist(request, id):
    movie = tmdb.Movies(id)
    response = movie.info()
    Watchlist.objects.create(movie_id=id)
    return HttpResponse("Der Film wurde erfolgreich zur Watchlist hinzugefügt.")

def watchlist(request):
    watchlist = Watchlist.objects.all()
    movies = []
    for item in watchlist:
        movie = tmdb.Movies(item.movie_id)
        response = movie.info()
        movies.append(movie)
    return render(request, 'watchlist.html', {'movies': movies})

def delete_watchlist(request):
    watchlist = Watchlist.objects.all().delete()
    return HttpResponse('Alle Elemente aus der watchlist wurden entfernt')

def index(request):
    return render(request, 'index.html')
