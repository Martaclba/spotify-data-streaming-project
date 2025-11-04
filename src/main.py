from dotenv import load_dotenv
load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scopes = [
    "user-library-read",
    "user-read-playback-state",
    "user-read-currently-playing",
]
scope = " ".join(scopes)



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


user_playlists = sp.current_user_playlists()
for playlist in user_playlists['items']:
    print(playlist, "\n")


