from tmdbv3api import TMDb

tmdb = TMDb()

tmdb.api_key = '3ccce087e61d6cabe327758d6d261b3c'

from tmdbv3api import Movie

movie = Movie()

search = movie.search('Harry Potter')

print(search[0].title)

"""for res in search:
    print(res.id)
    print(res.title)
    print(res.overview)
    print(res.poster_path)
    print(res.vote_average)"""
