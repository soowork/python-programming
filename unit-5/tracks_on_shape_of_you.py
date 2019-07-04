import requests

response = requests.get("https://deezerdevs-deezer.p.rapidapi.com/search?q=ed+sheeran",
  headers={
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
    "X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade"
  }
)

artist_data = response.json()
tracks = artist_data['data']
print(tracks)

for track in tracks:
    if track['album']['title'] == 'Shape of You':
        album_id = track['album']['id']
        break

print('album id is',album_id)

response_data = requests.get("https://deezerdevs-deezer.p.rapidapi.com/album/"+str(album_id),
headers={
"X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
"X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade"
}).json()

print(response_data)

'''