from audio_player.debug import run_debug_script
from audio_player.playback.audio_playback_manager import AudioPlaybackManager
import authentication.auth as auth

def main():
    # Startup
    spotify_client = auth.create_spotify_client()   # Instantiate Spotify client for session
    apm = AudioPlaybackManager(spotify_client)      # Audio Playback Manager

    # Color codes for terminal output
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    # DEBUG TESTING
    debug = True
    if debug:
        return run_debug_script(apm)

    print("Welcome to the OCP (One Click Performances) app!")
    print("Type 'exit' to quit.\n")
    while True:
        # Get user input
        usr_inp = input(f"{GREEN}ocp % {RESET}") # ocp: one click performances
        split_inp = usr_inp.split()
        first_token = usr_inp.split()[0]
        arg = usr_inp.split(first_token)[1].strip() if len(split_inp) > 1 else None

        # Exit program or attempt to execute command
        if usr_inp == 'exit' or usr_inp == 'quit':
            break
        else:
            apm.execute_command(first_token, arg)

if __name__ == "__main__":
    main()