import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_spotify_client():
    # Load environment variables from .env file
    load_dotenv()

    # Validate environment variables were loaded successfully from .env file
    if not validate_env_variables():
        raise EnvironmentError("Error: Missing environment variables.")


    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                                                     client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                                                     redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
                                                     scope="user-library-read user-modify-playback-state user-read-playback-state",
                                                     cache_path=".cache"))

def validate_env_variables():
    """
    Validates that the required environment variables are loaded.
    """
    required_vars = ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise EnvironmentError(f"Error: Missing environment variables: {', '.join(missing_vars)}")
    return True

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



