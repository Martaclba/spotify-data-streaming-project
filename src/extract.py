import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
load_dotenv()
import json

scopes = [
    "user-library-read",
    "user-read-playback-state",
    "user-read-currently-playing",
    "user-follow-read",
    "user-read-recently-played"
]
scope = " ".join(scopes)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))



def save_raw_data(data, filename):
    with open("data/raw/" + filename, "w") as f:
        json.dump(data, f, indent=2)


results = sp.current_user_saved_tracks()
save_raw_data(results, "saved_tracks.json")
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


user_playlists = sp.current_user_playlists()
for playlist in user_playlists['items']:
    print(playlist, "\n")


devices = sp.devices()
print("\n\nDevices", devices)

available_markets = sp.available_markets()
print("\n\nAvailable Markets", available_markets)


categories = sp.categories()
print("\n\nCategories\n", categories)


current_playback = sp.current_playback()
print("\n\nCurrent Playback\n", current_playback)


current_user = sp.current_user()
print("\n\nCurrent User\n", current_user)


current_user_followed_artists = sp.current_user_followed_artists()
print("\n\nCurrent User Followed Artists\n", current_user_followed_artists)



current_user_recently_played = sp.current_user_recently_played()
print("\n🎧 Músicas reproduzidas recentemente:")
for item in current_user_recently_played['items']:
    track = item['track']
    artist_name = track['artists'][0]['name']
    track_name = track['name']
    print(f"{artist_name} – {track_name}")

