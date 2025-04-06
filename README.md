# spotify-fun
For Fun - Spotify Custom Wrapper App
For Fun - Spotify Custom Wrapper App

Author: Ryan Welch
GitHub: @rlwelch1

# Getting Started
1. Download `poetry`
2. Clone the repository
3. 

# Features (planned)

## Get Simple Auth Working

1. Follow along with [Spotify Authentication](auth/implement_auth.txt) to 
2. set up dependency on `spotipy` library
3. set up main.py
4. make dummy Spotify API Call

## Work on Implementing Use Case


## Get User Feedback
Ask Sae and Sumi what they would do with an app like this

Figure out user needs



## SoundSwitch Lightshow Integration
Audio software called SoundSwitch that uses `.ssproj` (SoundSwitch Project) files to assign lighting configurations to buttons that are controllable by MIDI input.  There are ways to programmatically send midi input through a Python library (`mido`?).  It should be possible to map certain lighting timelines in the `.ssproj` file to a MIDI input that is labelled and programmatically triggered from a Python project.  Simultaneously, it is possible to trigger audio playback at a specified volume, timestamp, and potentially with a fade-in/fade-out.  There is also commonly background music playing before and after a performance song is played.  The app can pause playback (on YouTube, Spotify, SoundCloud, Apple Music, VLC, etc.), run the performance configuration - which comes down to playing the music and playing the lighting show at the same time, and then transition back to the default lighting schema and resume playback of the original background music source that was interrupted to play the performance.

### Experience
#### In one click:

##### -- Performance Begins --

- playback of background music stops
    - [optional] fade out
- playback of performance music begins
    - [optional] fade in
    - volume control setting for each song and for each microphone
    - saved mic volume levels, set to performance level
- lighting timeline for the song kicks off

##### -- Performance Concludes --

- playback of performance music stops
    - [optional] fade out
- playback of background music resumes playing
    - [optional] fade in
    - volume matched to what it was when paused initially
- lighting control timeline concludes
    - [optional] force stop lighting playback if desired
    - lighting returns to default café settings


### Technical Challenges
#### SoundSwitch MIDI Controller
Proof of concept trigger a timeline event on SoundSwitch via MIDI input.
##### 1. MIDI Controller
First input could be MIDI controller pad just to see how to map MIDI outputs inside SoundSwitch.
##### 2. Python library MIDI output
Second input, more technical, is having SoundSwitch trigger off of a Python MIDI output from a MIDI controller library.

