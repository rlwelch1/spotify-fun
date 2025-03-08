import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                                     client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                                     redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                                                     scope="user-library-read user-modify-playback-state user-read-playback-state",
                                                     cache_path=".cache"))

def generate_access_token(sp):
    """
    Generates an access token using the Spotify client.
    """
    token_info = sp.auth_manager.get_access_token()
    return token_info['access_token']

def print_tracks(sp):
    """
    Prints user's saved tracks. Test authentication worked.
    """
    sp.auth_manager.get_access_token()
    results = sp.current_user_saved_tracks(limit=50)
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(f"{idx + 1}. {track['artists'][0]['name']} – {track['name']}")



