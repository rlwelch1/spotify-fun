# import playback.device_info as di

# def play_recent_liked_track(sp, track_num=1, user_inp=False):
#     """
#     Plays the most recently liked track on the active device.
#     """
#     if user_inp:
#         track_num = int(input("Enter the number of the track you want to play: "))
#     device_id = di.get_active_device(sp)
#     if not device_id:
#         print("No active device found. Please open Spotify and start playing music on one of your devices.")
#         return

#     results = sp.current_user_saved_tracks(limit=track_num)
#     if results['items']:
#         track_idx = track_num - 1
#         track_uri = results['items'][track_idx]['track']['uri']
#         print(f"\nPlaying: {results['items'][track_idx]['track']['name']}\n")
#         sp.start_playback(device_id=device_id, uris=[track_uri])
#     else:
#         print("No liked tracks found.")