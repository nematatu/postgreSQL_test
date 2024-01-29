import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

client_id = 'a6bd17dc6fb74c3fba04930d83b6bc94' # App作成時のCliend ID
client_secret = 'f5f882869d3547f3a52216216981bed7' # App作成時のCliend Secret
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

music_id="6KDmk0EF3Qk7zJfDDtRoF2"
result=spotify.audio_features(music_id)
pprint.pprint(result)