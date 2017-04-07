import fresh_tomatoes
import urllib.request
import json

API_KEY = 'dd392b1622e38f86e3fb9b57d612901c'
BASE_URL = 'https://api.themoviedb.org/3/movie/popular?'
IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'
YOU_TUBE_URL = 'https://www.youtube.com/watch?v='


class Movie():
    def __init__(self, trailer_youtube_url,
                 storyline, title, poster_image_url):
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url


def get_trailer(movie_id):
    url = 'https://api.themoviedb.org/3/movie/%s/videos?api_key=%s' % (
        movie_id, API_KEY)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    return (data['results'][0]['key'])


def get_popular_movies():
    url = BASE_URL + 'api_key=' + API_KEY
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    movies = []
    for movie in data['results']:
        poster = IMAGE_BASE_URL + movie['poster_path']
        title = movie['original_title']
        storyline = movie['overview']
        trailer = YOU_TUBE_URL + get_trailer(movie['id'])
        movies.append(Movie(trailer, storyline, title, poster))
    if movies:
        return movies
    else:
        return None

movies = get_popular_movies()

fresh_tomatoes.open_movies_page(movies)
