import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
from pprint import pprint


CLIENT_ID = "<CLIENT-ID>"
CLIENT_SECRET = "<CLIENT-SECRET>"
REDIRECT_URL = "http://example.com"


DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{DATE}/")
response_webpage = response.text

soup = BeautifulSoup(response_webpage, "html.parser")
songs = soup.findAll(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

# for song in songs:
#     print(song.getText())


topify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        redirect_uri=REDIRECT_URL
    )
)

user_id = topify.current_user()["id"]
# print(user_id)
year = DATE.split("-")[0]

songs_uris = []
for _ in songs:
    song = _.getText()
    result = topify.search(q=f"track:{song} year:{year}", type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} does not exit in Spotify. Skipped!")

playlist = topify.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)

topify.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)