import requests
movie_ids = [
    238,
    680,
    550,
    185,
    641,
    515042,
    152532,
    120467,
    872585,
    906126,
    840430
]

for ids in movie_ids:
    movie_ids_url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{ids}"
    response = requests.get(movie_ids_url)

    if response.status_code <= 400 :
        data = response.json()
        print(data["title"])
        print(data["overview"])
        print(data["vote_average"])
    elif response.status_code >= 500:
        print("Error while responsing")
    else:
        print("Server error")

