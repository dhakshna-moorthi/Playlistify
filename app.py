from flask import Flask, render_template, request
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import numpy as np
import spotipy as spotipy
import pickle
import os

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

genre_predict = pickle.load(open('genre_classification.pkl', 'rb'))

playlist_predict = pickle.load(open('playlist_classification.pkl','rb'))

app = Flask(__name__)

def genre_song_features(track_uri, sp):
    features = sp.audio_features(track_uri)[0]
    features_list = np.array([features['energy'], features['acousticness'], features['danceability'], features['instrumentalness'],
                     features['loudness'], features['mode'], features['speechiness'], features['valence']
                    ])
    features_list = features_list.reshape(1, -1)
    return features_list

def playlist_song_features(track_uri, sp, genre):
    features = sp.audio_features(track_uri)[0]
    features_list = np.array([features['tempo'], features['danceability'], features['valence'], features['energy'],
                     features['tempo'], features['speechiness'], features['instrumentalness'], features['liveness'], genre
                    ])
    features_list = features_list.reshape(1, -1)
    return features_list


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    songName = request.form['songName']
    songURI = request.form['songURI']

    genre_features = genre_song_features(songURI, sp)
    genre = genre_predict.predict(genre_features)[0]
    print(genre_features)

    if(genre=='Electronic'):
        genre_coded=5
    elif(genre=='Jazz'):
        genre_coded=7
    elif(genre=='Alternative'):
        genre_coded=0
    elif(genre=='Country'):
        genre_coded=4
    elif(genre=='Rap'):
        genre_coded=8
    elif(genre=='Blues'):
        genre_coded=2
    elif(genre=='Classical'):
        genre_coded=3
    elif(genre=='Anime'):
        genre_coded=1
    elif(genre=='Rock'):
        genre_coded=9
    elif(genre=='Hip-Hop'):
        genre_coded=7

    playlist_features = playlist_song_features(songURI, sp, genre_coded)
    playlist = playlist_predict.predict(playlist_features)[0]
    print(playlist_features)

    if playlist == 14:
        playlist_name = 'Dance party'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXaXB8fQg7xif"
    elif playlist == 48:
        playlist_name = 'Phonk'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWWY64wDtewQt"
    elif playlist == 6:
        playlist_name = 'Beast Mode Dance'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXdURFimg6Blm"
    elif playlist == 36:
        playlist_name = 'Power Hour'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX32NsLKyzScr"
    elif playlist == 13:
        playlist_name = 'Dance Hits'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO"
    elif playlist == 12:
        playlist_name = 'Coffee Table Jazz'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWVqfgj8NZEp1"
    elif playlist == 29:
        playlist_name = 'Late Night Jazz'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX4wta20PHgwo"
    elif playlist == 28:
        playlist_name = 'Jazzy Romance'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWTbzY5gOVvKd"
    elif playlist == 26:
        playlist_name = 'Jazz in the Background'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWV7EzJMK2FUI"
    elif playlist == 41:
        playlist_name = 'Soft Jazz'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX949uWWpmTjT"
    elif playlist == 46:
        playlist_name = 'You & Me'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX6mvEU1S6INL"
    elif playlist == 1:
        playlist_name = 'ALT NOW'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWVqJMsgEN0F4"
    elif playlist == 47:
        playlist_name = 'anti pop'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWWqNV5cS50j6"
    elif playlist == 42:
        playlist_name = 'The New Alt'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX82GYcclJ3Ug"
    elif playlist == 2:
        playlist_name = 'Alternative 10s'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX873GaRGUmPl"
    elif playlist == 9:
        playlist_name = 'Chillin on a Dirty Road'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWTkxQvqMy4WW"
    elif playlist == 32:
        playlist_name = 'New Boots'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX8S0uQvJ4gaa"
    elif playlist == 43:
        playlist_name = 'Traditional country'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXaiEFNvQPZrM"
    elif playlist == 19:
        playlist_name = 'Energy Country Booster'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWXLSRKeL7KwM"
    elif playlist == 44:
        playlist_name = 'Wild country'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX5mB2C8gBeUM"
    elif playlist == 40:
        playlist_name = 'RapCaviar'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"
    elif playlist == 38:
        playlist_name = 'Rap Workout'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX76t638V6CA8"
    elif playlist == 16:
        playlist_name = 'Door Knockers'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX9iGsUcr0Bpa"
    elif playlist == 37:
        playlist_name = 'Pressure'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWZwCeILEyQAy"
    elif playlist == 39:
        playlist_name = 'Rap n Rool'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX89XXHpIgTCJ"
    elif playlist == 7:
        playlist_name = 'Blues Classics'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXd9rSDyQguIk"
    elif playlist == 30:
        playlist_name = 'Midnight Blues'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXcc6f6HRuPnq"
    elif playlist == 34:
        playlist_name = 'Nu-Blue'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXb3MZdETGqKB"
    elif playlist == 27:
        playlist_name = 'Jazz-Blues'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX9GSZDbrndTa"
    elif playlist == 10:
        playlist_name = 'Classic Blues Guitar'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWWhiW4fdIska"
    elif playlist == 11:
        playlist_name = 'Classical Essentials'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0"
    elif playlist == 8:
        playlist_name = 'Calming Classical'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWVFeEut75IAL"
    elif playlist == 15:
        playlist_name = 'Dark Academia Classical'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX17GkScaAekA"
    elif playlist == 20:
        playlist_name = 'Feel Good Classical'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX5Lm1ZiObdc3"
    elif playlist == 17:
        playlist_name = 'Dramatic Classical'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX2aCk0vzzaZQ"
    elif playlist == 4:
        playlist_name = 'Anime Now'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWT8aqnwgRt92"
    elif playlist == 31:
        playlist_name = 'My Hero Academia'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX9Uv7i7ODBAM"
    elif playlist == 18:
        playlist_name = 'EQUAL Anime'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXblYBkrEcpLK"
    elif playlist == 3:
        playlist_name = 'Anime Classical'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0CgRlkzaOFL"
    elif playlist == 5:
        playlist_name = 'Anime On Replay'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0hAXqBDwvwI"
    elif playlist == 35:
        playlist_name = 'Pop Rock'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXatFAWyNT5ad"
    elif playlist == 33:
        playlist_name = 'Noisy'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX98f0uoU1Pcs"
    elif playlist == 45:
        playlist_name = 'Women of Rock'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXd0ZFXhY0CRF"
    elif playlist == 22:
        playlist_name = 'Fresh Finds Rock'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX78toxP7mOaJ"
    elif playlist == 21:
        playlist_name = 'Feelin Myself'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX6GwdWRQMQpq"
    elif playlist == 25:
        playlist_name = 'Hip-Hop Frive'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWUFmyho2wkQU"
    elif playlist == 24:
        playlist_name = 'Hip-Hop Favourites'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX48TTZL62Yht"
    elif playlist == 23:
        playlist_name = 'Global Hip-Hop'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX2sQHbtx0sdt"
    elif playlist == 0:
        playlist_name = 'A1'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0sDai2F5jCQ"
    else:
        playlist_name = 'All New Rock'
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWZryfp6NSvtz"

    return render_template('result.html', genre = genre, songName = songName, playlist = playlist_name, image_url = genre+".jpeg", playlist_url = playlist_url)

if __name__ == '__main__':
    app.run(port=5000,debug=True)