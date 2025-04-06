import spotipy
from spotipy.oauth2 import SpotifyOAuth

def play_song(sp, uri):
    device_info.get_active_device(sp)
    if devices['devices']:
        device_id = devices['devices'][0]['id']
        sp.start_playback(device_id=device_id, uris=[uri])
    else:
        print("No active devices found")

# Example usage
# play_song("spotify:track:YOUR_SONG_URI")