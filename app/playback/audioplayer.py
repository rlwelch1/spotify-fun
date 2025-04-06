import spotipy
from spotipy.oauth2 import SpotifyOAuth

class AudioPlayer:
    def __init__(self, spotipy_client):
        """
        Initialize the AudioPlayer with a Spotipy client instance.
        """
        self.spotipy_client = spotipy_client

    def get_active_device(self):
        """
        Returns the ID of the active device.
        """
        devices = self.spotipy_client.devices()
        for device in devices['devices']:
            if device['is_active']:
                return device['id']
        return None

    def play_song(self, uri):
        """
        Plays a song on the active device using its URI.
        """
        device_id = self.get_active_device()
        if device_id:
            self.spotipy_client.start_playback(device_id=device_id, uris=[uri])
        else:
            print("No active devices found.")

    def play_recent_liked_track(self, track_num=1, user_inp=False):
        """
        Plays the most recently liked track on the active device.
        """
        if user_inp:
            track_num = int(input("Enter the number of the track you want to play: "))
        device_id = self.get_active_device()
        if not device_id:
            print("No active device found. Please open Spotify and start playing music on one of your devices.")
            return

        results = self.spotipy_client.current_user_saved_tracks(limit=track_num)
        if results['items']:
            track_idx = track_num - 1
            track_uri = results['items'][track_idx]['track']['uri']
            print(f"\nPlaying: {results['items'][track_idx]['track']['name']}\n")
            self.spotipy_client.start_playback(device_id=device_id, uris=[track_uri])
        else:
            print("No liked tracks found.")