import spotipy # Library we are using for spotify commands
import json #Used for printing user information step  
import random # for testing inputs with random variable 
from spotipy.oauth2 import SpotifyOAuth # for authentication and refresh token 
from dotenv import dotenv_values #To read Client ID, Redirect URI and Client Secret ID from .env file
import webbrowser # To open webbroswer 
import time # for time.sleep() adds pauses 
from pynput import keyboard # For the escape key 

config = dotenv_values(".env") # imports redirect url # client sectret ID # and Client ID

#Code for Authentication 
sp = spotipy.Spotify(# creates spotify client object through Spotipy 
    auth_manager=SpotifyOAuth(# We are using OAuth Authentication from Spotipy 
        client_id=config["SPOTIFY_CLIENT_ID"], # Fetching client Id from .env file 
        client_secret=config["SPOTIFY_CLIENT_SECRET"], # Fetching spotify Secret_Clinet_ID 
        redirect_uri=config["SPOTIFY_REDIRECT_URI"], # Fetching spotify_Redirect_URI from .env file
        scope="playlist-modify-private, user-modify-playback-state, user-read-playback-state, user-read-recently-played, user-read-private, user-read-email", # This defines the permisions the app uses
    ))

# Initialising the current user
try:
    current_user = sp.current_user()
    print("Authenticated as:", current_user["display_name"])
except Exception as e:
    print("Error:", e)
    exit()


# Defining function that checks if spotify player is active and returns T/F. The function also returns PlaybackState (which allows us to see if spotify is playing or paused when active). 
def PlayBackStatev2():
    PlayBackState= sp.current_playback()
    if PlayBackState is None:
        IsActive= False
    else:
        IsActive= True
    return IsActive, PlayBackState
        

#Priints the current user id (username) and prints where the token was saved
print(current_user["id"], "token saved in '.cache' file.")


#Prints a whole bunch of information about the user only here for checking authentication can remove later in refined product. 
print(json.dumps(current_user, sort_keys=True, indent=4)) 

#Code for the Escape Key 
def on_press(key):
        if key==keyboard.Key.esc:
            print('Have a nice Day! :)')
        return False 

# initialise is_paused
IsActive, PlayBackState=PlayBackStatev2()
if IsActive is True: # When spotify is inactive Playbackstate returns None
    if PlayBackState['is_playing']:
        is_paused=False
    else: 
        is_paused =True 
else: 
    is_paused=True

#initialising the variables 
iteh=0 # this is just for testing
DoubleBlink=False
LookLeft=False
LookRight=False

# The Player
with keyboard.Listener(on_press=on_press) as listener:  # Listening for the escape key to end the loop 
    while True:
        time.sleep(3) # Pauses the code for 3 seconds here because I was using random variable to test code. 
        x=4*random.random() # x is a random number between 0 and 4 
        if x<2:
            DoubleBlink=True
            iteh=iteh+1
            print('Blinkcheck')
            print('iteh:', iteh)
        elif 2<=x<3:
            LookRight=True
            print('Right Check')
        elif 3<=x<=4:
            LookLeft=True
            print('CheckLeft')
        if iteh>10: 
            print("Good Bye, Have a great day!") 
            break
        if  DoubleBlink is True and is_paused: 
            IsActive, _ =PlayBackStatev2() 
            if IsActive is True:
                sp.start_playback()
                DoubleBlink=False # Resests after each use otherwise Doublink will be True for next iteration
                is_paused=False  
                print('Playback resumed')
            else: #if no active spotify session find last played song and open spotify
                PlaybackHistory = sp.current_user_recently_played()
                LastPlayed=PlaybackHistory['items'][0]['track']['external_urls']['spotify']
                #LastPlayedUri=PlaybackHistory['items'][0]['context']
                #LastPlayedUri2=PlaybackHistory['items'][0]['track']['uri']
                webbrowser.open(LastPlayed)
                while not IsActive: 
                    print('bufferring')
                    time.sleep(5)
                #sp.pause_playback()
                #time.sleep(1)
                #sp.start_playback(uris=[LastPlayedUri2])
                is_paused = False
                print('Playback has begun')
                DoubleBlink=False
        elif DoubleBlink is True and not is_paused: 
            IsActive,PlayBackState=PlayBackStatev2()
            if IsActive is True:
                if PlayBackState['is_playing']:
                    sp.pause_playback()
                    is_paused = True
                    print('Playback paused.')
                    DoubleBlink=False
                else:
                    print('Player is already paused, check code if this appears')
                    is_paused=True
                    DoubleBlink=False
            else:  
                print('No active player found please play a song to pause, check code if this appears')
                is_paused=True
                DoubleBlink=False
        elif LookRight is True:
            try:
                sp.next_track()
                LookRight=False
                if is_paused is True:
                    print('Playback ressumed: Track skipped')
                else: 
                    print('Track skipped')
                is_paused=False
            except: 
                print('an error in lookRight logic has occured')
        elif LookLeft is True: 
            try:
                sp.previous_track()
                LookLeft=False
                if is_paused is True:
                    print('Playback ressumed: skipped backwards')
                else:
                    print('Skipped backwards')
                is_paused=False
            except: 
                print('an error with Lookleft has occured!!!!')
        else: 
            print("Please enter valid user-input.")
        if not listener.running:
            break  # Break the loop if the escape key was pressed

print('You have excaped the loop')
