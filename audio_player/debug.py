from pprint import pprint

def run_debug_script(apm):
    """
    Run the debug script for the Audio Playback Manager to experiment.
    """
    print("\n\n##############\nDebug Logs\n##############\n")

    # Print key : value pairs
    # print(apm.get_song_names_list())
    # print("\n\n")
    # print(apm.get_track_list()[0])
    # shuwa_track_dict = apm.get_track_list()[0]
    # print(type(shuwa_track_dict))
    # print(shuwa_track_dict['images'])
    # print(shuwa_track_dict.keys())
    # print("\n")
    # print(shuwa_track_dict['album']['images'][0]['url']) # get album art url

    # Print entire track dictionary
    # for key, value in shuwa_track_dict.items():
    #     print(f"{key} : {value}")

    # Print album art urls
    # for album_art_url in apm.get_album_art_url_list():
    #     print(album_art_url)
    

    for song in apm.get_songs():
        print(song.get_song_name(apm.spotify_client))
        # pprint(song.get_track(apm.spotify_client))
        print(song.get_album_art_url(apm.spotify_client))
        # break # break after one song for testing


    print("\n\n##############\nEnd Debug Logs\n##############\n")
    # End Debug Testing