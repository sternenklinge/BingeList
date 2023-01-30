import tmdbsimple as tmdb

# api_key = '300659883e7e07b8afd0aec7dbf8e802'
tmdb.API_KEY = '300659883e7e07b8afd0aec7dbf8e802'
tmdb.REQUESTS_TIMEOUT = 10

#request to get info about movie
tmdb_id = 603
movie = tmdb.Movies(tmdb_id)
response = movie.info()
print (movie.title)

def search_movies_and_tv(query):
    search = tmdb.Search()
    response = search.movie(query=query, language="de")
    movies = search.results
    response = search.tv(query=query, language="de")
    tv_shows = search.results
    return movies, tv_shows

movies, tv_shows = search_movies_and_t("Harry Potter Stein der Weisen")
print(movies)
print(tv_shows)
