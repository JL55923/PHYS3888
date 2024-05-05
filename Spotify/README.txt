If you want to use the code with your own spotify account 
1) Download all the files in this folder save them so they are all located in the same folder
2) Go to spotify https://developer.spotify.com/documentation/web-api
    - Create a developer account 
    - Once you have created a developer account you can create an app 
3) Create an app 
    - Go to your developer Dashboard and create and app 
    - Name it something random
    - Fill in a Redirect URI do something like http://localhost:8080/callback
    - select Web API and Web Playback SDK 
4) Client ID and Client Secret ID 
    - Once you have created your app go to the settings of the app and retrieved the Clinet ID and the Clinet Secret ID and your Redirect URI 
    - Paste these into the .env file I have left it blank where you need to paste you don't need quotation marks 
5) Running the App 
    - Make sure you have installed all the requirments and that the .env file is in the same folder as spotifyV3.py 
    - Run SpotifyV3.py 
        - your webbrowser should open and you should be redirected to a spotify log in 
        - if you are already logged in you will be redirected to a page asking you to accept the apps permisions click accept 
        - After you accept the token should be saved in the same foulder as the spotifyV3.py file
6) BEWARE
    -  right now the skip pause and play controls are just controlled by a random variable x which refreshes every 3 seconds 
    -   USE THE ESCAPE KEY TO END THE LOOP
    - I have codded it with the random variable as I wanted to try get it into a form where it was accepting inputs that are similar 
    to what the classifier outputs
7) More Notes 
    - If you dont have spotify premium some functions might not work 
    - Atm it seems spotify don't let you have more than 25 users of one app when it is in developer mode and I havent found a way to automate adding a user to the app. 
    you can give other users permissions to use the app MANUALLY through the developer dashboard I tested it with another spotify account.
    I am unsure if there is a way to automate this without requesting permission from spotify to upgrade the app from developer mode. 
    - If you dont have a spotify account I create a dummy one I can lend you guys. Spotify also offer a 2month free trial so you could create one 
    using that but you will have to remember to cancel the subscription before they charge you in 2 months.
    - Mac users might not need to do the config = dotenv_values(".env") I think you can just use a source command although I am unsure

