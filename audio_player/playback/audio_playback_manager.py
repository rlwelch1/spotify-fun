from spotipy.oauth2 import SpotifyOAuth
import socket
from audio_player.controllers.command_menu import CommandMenu
from audio_player.playback.uri_manager import URIManager

class AudioPlaybackManager:
    def __init__(self, spotify_client):
        """
        Initialize the AudioPlaybackManager with a Spotify client instance.
        """
        self.spotify_client = spotify_client
        self.uri_manager = URIManager()
        self.device_id = self.get_device()
        self.command_menu = CommandMenu(self)

    def execute_command(self, command, arg):
        """
        Executes a command from the command menu.
        """
        try:
            self.command_menu.execute_command(command, arg)
        except ValueError as e:
            print(e)

    def get_device(self):
        """
        Returns the ID of either the active device or the current macbook.
        """
        active_device = self.get_active_device()
        current_mac = self.get_current_macbook()
        device_id = active_device if not current_mac else current_mac
        if not device_id:
            raise RuntimeError("No active devices found.")
        return device_id

    def get_active_device(self):
        """
        Returns the ID of the active device.
        """
        devices = self.spotify_client.devices()
        for device in devices['devices']:
            if device['is_active']:
                return device['id']
        return None
    
    def choose_device(self):
        """
        Fetches the list of devices and prompts the user to select one during app setup.
        """
        pass # TODO: Implement and move device logic to separate class

    def get_current_macbook(self):
        """
        Returns the ID of the MacBook device runing the app.
        """
        # Get the hostname (device name) of the current device
        device_name = socket.gethostname()
        # print(f"The device name is: {device_name}")

        devices = self.spotify_client.devices()
        for device in devices['devices']:
            # print(device['name'])
            # print(device['id'])
            ryan_mac_name = "Ryan's MacBook Air"
            if device['name'] == ryan_mac_name:
                print("found it\n\n\n")
                return device['id']
        return None

    def play_song(self, name):
        """
        Plays a song on the active device using its name.
        """
        try:
            uri = self.uri_manager.get_uri(name)
            self.play_song_by_uri(uri)
        except ValueError as e:
            print(f"An error occurred while trying to play the song: {e}")
    
    def pause_song(self):
        """
        Pauses the currently playing song on the active device.
        """
        if self.device_id:
            self.spotify_client.pause_playback(device_id=self.device_id)
        else:
            print("No active devices found.")

    def play_song_by_uri(self, uri):
        """
        Plays a song on the current device using the song's URI.
        """
        if self.device_id:
            self.spotify_client.start_playback(device_id=self.device_id, uris=[uri])
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

        results = self.spotify_client.current_user_saved_tracks(limit=track_num)
        if results['items']:
            track_idx = track_num - 1
            track_uri = results['items'][track_idx]['track']['uri']
            print(f"\nPlaying: {results['items'][track_idx]['track']['name']}\n")
            self.spotify_client.start_playback(device_id=device_id, uris=[track_uri])
        else:
            print("No liked tracks found.")
    
    def show_song_list(self):
        print(self.uri_manager)