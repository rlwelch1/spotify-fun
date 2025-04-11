from typing import Any
from spotipy import Spotify

class Song:
    def __init__(self, song_uri: str, song_alias: str):
        self.song_uri: str = song_uri
        self.song_alias: str = song_alias
        
    def get_song_name(self, spotify_client: Spotify) -> str:
        """
        Returns the song name using the Spotify client.
        """
        track = spotify_client.track(self.song_uri)
        return track['name']

    # Track is a dictionary, documentation unclear on return type
    # https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.track
    def get_track(self, spotify_client: Spotify) -> (Any | None):
        """
        Returns the song name using the Spotify client.
        """
        track = spotify_client.track(self.song_uri)
        return track
    
    def get_album_art_url(self, spotify_client: Spotify) -> str:
        """
        Returns the album art URL using the Spotify client.
        """
        track = spotify_client.track(self.song_uri)
        return track['album']['images'][0]['url'] if track['album']['images'] else None
    
