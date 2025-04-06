from audio_player.playback.audio_playback_manager import AudioPlaybackManager
import authentication.auth as auth

def main():
    # Startup
    spotify_client = auth.create_spotify_client()   # Instantiate Spotify client for session
    apm = AudioPlaybackManager(spotify_client)      # Audio Playback Manager

    print("Welcome to the OCP (One Click Performances) app!")
    print("Type 'exit' to quit.\n")
    while True:
        # Get user input
        usr_inp = input("ocp % ") # ocp: one click performances
        split_inp = usr_inp.split()
        first_token = usr_inp.split()[0]
        arg = usr_inp.split(first_token)[1].strip() if len(split_inp) > 1 else None

        if usr_inp == 'exit':
            break
        else:
            apm.execute_command(first_token, arg)

if __name__ == "__main__":
    main()