BASE_PATH = "/Volumes/workspace/bronze/spotify_data/streaming_history"

INGESTION_CONFIG = [
    {
        "source": "streaming_history",
        "path": f"{BASE_PATH}/Streaming_History_Audio*.json",
        "format": "json",
        "table": "workspace.bronze.spotify_streaming_history_raw",
        "mode": "overwrite"
    },
    {
        "source": "api",
        "format": "api_call",
        "table": "workspace.bronze.spotify_recently_played_raw",
        "mode": "append"
    }
]

metadata_configs = {
    "track": {
        "table": "workspace.bronze.spotify_tracks_raw", 
        "chunk": 50,
        "api": "sp.tracks",
        "key": "tracks",
        "schema": "track_schema"
    },
    "artist": {
        "table": "workspace.bronze.spotify_artists_raw", 
        "chunk": 50,
        "api": "sp.artists",
        "key": "artists",
        "schema": "artist_schema"
    },
    "album": {
        "table": "workspace.bronze.spotify_albums_raw",
        "chunk": 20,
        "api": "sp.albums",
        "key": "albums",
        "schema": "album_schema"
    }
}
