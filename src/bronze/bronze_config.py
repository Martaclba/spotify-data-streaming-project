BASE_PATH = "/Volumes/workspace/bronze/spotify_data/streaming_history"

INGESTION_CONFIG = [
    {
        "source": "streaming_history",
        "path": f"{BASE_PATH}/Streaming_History_Audio*.json",
        "format": "json",
        "table": "workspace.bronze.spotify_streaming_history_raw"
    },
    {
        "source": "api",
        "format": "api_call",
        "table": "workspace.bronze.spotify_api_recently_played_tracks_raw"
    }
]