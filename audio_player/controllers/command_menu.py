class CommandMenu:
    def __init__(self, apm):
        self.apm = apm
        self.command_menu = {
            'hello-world':
                lambda x : print("こんにちは、世界！"),
            'pause':
                lambda x: self.apm.spotify_client.pause_playback(),
            'play': # attempt to play a song
                lambda x: self.apm.play_song(x),
            'song-list':
                lambda x: self.apm.show_song_list(),
            'rr': # rickroll
                lambda x: self.apm.play_song_by_uri("spotify:track:4PTG3Z6ehGkBFwjybzWkR8")
        }

    def execute_command(self, command, arg):
        if command in self.command_menu:
            func_to_execute = self.command_menu[command]
            func_to_execute(arg) # pass the argument to the function
        else:
            raise ValueError(f"Command '{command}' not found in command menu.")
        