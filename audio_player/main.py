import spotipy
import audio_player.playback.play_recent as play_recent
import authentication.auth as auth
from playback.play import play_song

def main():
    print("\n\nAuthenticating...")
    spotify_client = auth.create_spotify_client() # Instantiate Spotify client for session
    # play_recent.play_recent_liked_track(spotify_client, track_num=2)
    print("Welcome to the OCP (One Click Performances) app!")
    print("Type 'exit' to quit.")
    while True:
        usr_inp = input(" ocp % ") # ocp: one click performances
        if usr_inp == 'exit':
            break
        elif usr_inp == 'hello world':
            print("こんにちは、世界！")
        elif usr_inp == 'shuwa shuwa':
            play_song(spotify_client, "spotify:track:34xI77dFTR6pwrgIlwONwP?si=2e6f9ffd65704d31")
        else:
            print("Invalid command. Type 'exit' to quit.")

if __name__ == "__main__":
    main()