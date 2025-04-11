from audio_player.playback.song import Song


class URIManager:
    def __init__(self):
        self.uris = {} # map from song_name to uri
        self.song_alias_to_song = {} # map from track_name to Song object
        with open("audio_player/playback/song_name_to_url.txt", "r") as f:
            for line in f:
                song_alias, url = line.strip().split(" | ")
                uri = self.convert_url_to_uri(url)
                self.song_alias_to_song[song_alias] = Song(uri, song_alias)
                self.uri_to_song[uri] = self.song_alias_to_song[song_alias]

    def get_tracks(self, spotify_client):
        return [song.get_track(spotify_client) for song in self.song_alias_to_song.values()]  # list of tracks
    
    def get_song(self, uri):
        return self.uri_to_song[uri]

    def get_songs(self):
        return self.song_alias_to_song.values()

    def get_song_names(self, spotify_client):
        return [song.get_song_name(spotify_client) for song in self.song_alias_to_song.values()]  # list of song names
    
    def get_album_art_urls(self, spotify_client):
        return [song.get_album_art_url(spotify_client) for song in self.song_alias_to_song.values()] # list of album art urls

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