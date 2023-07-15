import requests
import json
import spotify


CLIENT_ID = 'd5f82cabd7fb4d74a05d7d7ff9656542'

CLIENT_SECRET = 'a70ed1e0fe1e4bffbcf217330747f525'

AUTH_URL =  'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'

track_id = '6y0igZArWVi6Iz0rj35c1Y'

response = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

print(response.status_code)
print(response.json())
