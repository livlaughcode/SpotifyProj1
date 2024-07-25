import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#secret

cliID = '17fa8a257753447eae1d70d4ee729295' #client ID was on spotify dash
secretID = '16edf4e41b504e5e89ef900697bfebba ' #secretID was aswell, need both in order to run 

client_credentials_manager = SpotifyClientCredentials(client_id= cliID, client_secret= secretID)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)



artist_name = []
track_name = []
popularity = []
track_id = []