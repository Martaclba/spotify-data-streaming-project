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
    "user-read-recently-played",
    "user-top-read"
]
scope = " ".join(scopes)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=True))


def save_raw_data(data, filename):
    with open("data/raw/" + filename, "w") as f:
        json.dump(data, f, indent=2)



current_user_playlists = sp.current_user_playlists(limit=50)
for playlist in current_user_playlists['items']:
    print(playlist, "\n")
    playlist['extra_info'] = sp.playlist(playlist['id'])
    playlist['playlist_items'] = sp.playlist_items(playlist['id'])
    playlist['cover_images'] = sp.playlist_cover_image(playlist['id'])
save_raw_data(current_user_playlists, "current_user_playlists.json")


devices = sp.devices()
print("\n\nDevices", devices)
save_raw_data(devices, "devices.json")

available_markets = sp.available_markets()
print("\n\nAvailable Markets", available_markets)
save_raw_data(available_markets, "available_markets.json")


categories = sp.categories(limit=50)
# for category in categories['categories']['items']:
#     try:
#         category['playlists'] = sp.category_playlists(category['id'], country='PT')
#     except spotipy.exceptions.SpotifyException as e:
#         print(f"Cannot fetch playlists for category {category['name']} ({category['id']}): {e}")
#         category['playlists'] = None

save_raw_data(categories, "categories.json")

# category_playlists = sp.category_playlists(category_id='pop')
# print("\n\nCategory Playlists (Pop)\n", category_playlists)
# save_raw_data(category_playlists, "category_playlists_pop.json")


current_playback = sp.current_playback()
print("\n\nCurrent Playback\n", current_playback)
save_raw_data(current_playback, "current_playback.json")


current_user = sp.current_user()
print("\n\nCurrent User\n", current_user)
save_raw_data(current_user, "current_user.json")


# current_user_follow_playlist = sp.current_user_follow_playlist()
# print("\n\nCurrent User Followed Playlists\n", current_user_follow_playlist)
# save_raw_data(current_user_follow_playlist, "current_user_follow_playlist.json")


current_user_followed_artists = sp.current_user_followed_artists()
print("\n\nCurrent User Followed Artists\n", current_user_followed_artists)
save_raw_data(current_user_followed_artists, "current_user_followed_artists.json")

# current_user_following_artists = sp.current_user_following_artists()
# print("\n\nCurrent User Following Artists\n", current_user_following_artists)
# save_raw_data(current_user_following_artists, "current_user_following_artists.json")

# current_user_following_users = sp.current_user_following_users()
# print("\n\nCurrent User Following Users\n", current_user_following_users)
# save_raw_data(current_user_following_users, "current_user_following_users.json")


current_user_playing_track = sp.current_user_playing_track()
print("\n\nCurrent User Playing Track\n", current_user_playing_track)
save_raw_data(current_user_playing_track, "current_user_playing_track.json")


current_user_recently_played = sp.current_user_recently_played()
print("\n🎧 Músicas reproduzidas recentemente:")

for item in current_user_recently_played['items']:
    track = item['track']
    artist_name = track['artists'][0]['name']
    track_name = track['name']
    track_id = track['id']

    print(f"{artist_name} – {track_name} ({track_id})")

    # Fetch audio analysis safely
    try:
        track['audio_analysis'] = sp.audio_analysis(track_id)
    except spotipy.exceptions.SpotifyException as e:
        print(f"Cannot fetch audio analysis for {track_name} ({track_id}): {e}")
        track['audio_analysis'] = None

    # Fetch audio features safely
    try:
        track['audio_features'] = sp.audio_features([track_id])[0]  # note the list
    except spotipy.exceptions.SpotifyException as e:
        print(f"Cannot fetch audio features for {track_name} ({track_id}): {e}")
        track['audio_features'] = None

save_raw_data(current_user_recently_played, "current_user_recently_played.json")


current_user_saved_albums = sp.current_user_saved_albums(limit=50)
print("\n\nCurrent User Saved Albums\n", current_user_saved_albums)
save_raw_data(current_user_saved_albums, "current_user_saved_albums.json")


current_user_saved_tracks = sp.current_user_saved_tracks()
for idx, item in enumerate(current_user_saved_tracks['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
save_raw_data(current_user_saved_tracks, "current_user_saved_tracks.json")


current_user_top_artists = sp.current_user_top_artists()
for idx, artist in enumerate(current_user_top_artists['items']):
    print(idx, artist['name'])
save_raw_data(current_user_top_artists, "current_user_top_artists.json")


current_user_top_tracks = sp.current_user_top_tracks()
for idx, track in enumerate(current_user_top_tracks['items']):
    print(idx, track['name'])
save_raw_data(current_user_top_tracks, "current_user_top_tracks.json")


currently_playing = sp.currently_playing()
print("\n\nCurrently Playing\n", currently_playing)
save_raw_data(currently_playing, "currently_playing.json")


try:
    featured_playlists = sp.featured_playlists(country="PT")
except spotipy.exceptions.SpotifyException as e:
    print(f"Cannot fetch featured playlists: {e}")
    featured_playlists = None
save_raw_data(featured_playlists, "featured_playlists.json")


me = sp.me()
print("\n\nMe\n", me)
save_raw_data(me, "me.json")


new_releases = sp.new_releases(country="PT", limit=50)
print("\n\nNew Releases\n", new_releases)
save_raw_data(new_releases, "new_releases.json")



# next = sp.next()
# print("\n\nNext Saved Tracks\n", next)
# save_raw_data(next, "next_saved_tracks.json")






