from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import tmdbsimple as tmdb
from .models import Watchlist

tmdb.API_KEY = '300659883e7e07b8afd0aec7dbf8e802'
tmdb.REQUESTS_TIMEOUT = 10

def home(request):
    return render(request, 'home.html')


def browse(request):
    discover = tmdb.Discover()
    response = discover.movie(language='de', sort_by='popularity.desc')
    movies = discover.results
    response = discover.tv(language='de', sort_by='popularity.desc')
    tv_shows = discover.results
    return render(request, 'browse.html', {'movies': movies, 'tv_shows': tv_shows})


def results(request):
    query = request.GET.get('query')
    referer_url = request.META.get('HTTP_REFERER')
    if query:
        search = tmdb.Search()
        response = search.movie(query=query, language='de')
        movies = search.results
        response = search.tv(query=query, language='de')
        tv_shows = search.results
        return render(request, 'newresults.html', {'movies': movies, 'tv_shows': tv_shows})
    else:
        if referer_url:
            return redirect(referer_url)
        else:
            return redirect('home')


def add_to_watchlist(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        Watchlist.objects.create(movie_id=movie_id)
        return redirect('browse')


def watchlist(request):
    watchlist = Watchlist.objects.all()
    movies = []
    for item in watchlist:
        movie = tmdb.Movies(item.movie_id)
        response = movie.info()
        movies.append(movie)
    return render(request, 'newwatchlist.html', {'movies': movies})


def delete_watchlist(request):
    watchlist = Watchlist.objects.all().delete()
    return HttpResponse('Alle Elemente aus der watchlist wurden entfernt')



