import requests

response = requests.get("https://deezerdevs-deezer.p.rapidapi.com/search?q=eminem",
  headers={
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
    "X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade"
  }
)

eninem_data = response.json()
tracks = eninem_data['data']
#print(eninem_data)

for track in tracks:
    if track['album']['title'] == 'Curtain Call: The Hits':
        album_id = track['album']['id']
        break

print('album id is',album_id)
response_data = requests.get("https://deezerdevs-deezer.p.rapidapi.com/album/"+str(album_id),
headers={
"X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
"X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade"
}).json()

print('Curtain Call: The Hits was released on '+ response_data['release_date'])

