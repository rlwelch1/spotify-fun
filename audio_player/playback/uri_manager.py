class URIManager:
    def __init__(self):
        self.uris = {}
        with open("audio_player/playback/song_name_to_url.txt", "r") as f:
            for line in f:
                song_name, url = line.strip().split(" | ")
                self.uris[song_name] = self.convert_url_to_uri(url)
        
    def convert_url_to_uri(self, url: str) -> str:
        """Converts a Spotify URL to a URI."""
        spotify_track_header = "https://open.spotify.com/track/"
        if url.startswith(spotify_track_header): # URL is formatted as expected
            uri = url.replace(spotify_track_header, "spotify:track:")
            uri = uri.split("?si")[0]
        else: # URL is not formatted as a spotify track link
            raise ValueError(f"Invalid Spotify Track URL:\n{url}")
        return uri

    def set_uri(self, song_name, uri):
        self.uris[song_name] = uri

    def get_uri(self, song_name):
        result = self.uris.get(song_name, None)
        if result is None:
            raise ValueError(f"URI for {song_name} not found.")
        return result
    
    def __str__(self):
        return "\n".join(f'"{key}" : "{value}"' for key, value in self.uris.items())