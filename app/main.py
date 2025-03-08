import spotipy
import app.playback.play_recent as play_recent
import authentication.auth as auth
import playback

def main():
    sp = auth.create_spotify_client() # Instantiate Spotify client for session
    play_recent.play_recent_liked_track(sp, track_num=2)

if __name__ == "__main__":
    main()