import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                                   client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                                   redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                                                   scope="user-library-read"))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(f"{idx + 1}. {track['artists'][0]['name']} – {track['name']}")

if __name__ == "__main__":
    main()