import media
import fresh_tomatoes
import requests


# fetch movies data from TMDB server, return a list of movies
def get_tmdb_movies():
    response = requests.get("https://api.themoviedb.org/3/discover/movie"
                            "?api_key=cb6f6a2667af1c852790468594b68e7e"
                            "&language=en-US"
                            "&sort_by=popularity.desc"
                            "&include_adult=false"
                            "&include_video=false&page=1"
                            "&primary_release_year=2017")
    if (response.status_code == 200):
        data = response.json()
        tmdb_movies = data["results"]
        return tmdb_movies
    else:
        print "movie api request failed!" + str(response.status_code)
        return []


# fetch vedio data from TMDB server, return the first YouTube URL string.
def get_videourl_by_movie(movie_id):
    videos_response = requests.get("https://api.themoviedb.org/3/movie/" +
                                   str(movie_id) + "/videos?"
                                   "api_key=cb6f6a2667af1c852790468594b68e7e"
                                   "&language=en-US")
    if (videos_response.status_code == 200):
        videos_data = videos_response.json()
        tmdb_video_data = videos_data["results"]
        for video in tmdb_video_data:
            video_url = ""
            if (video["site"] == "YouTube"):
                video_url = "https://www.youtube.com/watch?v=" + video["key"]
                break
        return video_url
    else:
        print "video api request failed!" + str(videos_response.status_code)
        return ""

movies = []
tmdb_movies = get_tmdb_movies()

# Make all the movies in individul media.Movie() class object,
# store in an Array, pass the array to fresh_tomatoes.
for movie in tmdb_movies:
    video_url = get_videourl_by_movie(movie["id"])
    temp_movie_object = media.Movie(movie["title"],
                                    movie["overview"],
                                    "https://image.tmdb.org/t/p/w185/" +
                                    movie["poster_path"],
                                    video_url)
    movies.append(temp_movie_object)

fresh_tomatoes.open_movies_page(movies)
