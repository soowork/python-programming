import requests
'''
response = requests.post("https://DeezerzakutynskyV1.p.rapidapi.com/getArtistAlbums",
  headers={
    "X-RapidAPI-Host": "DeezerzakutynskyV1.p.rapidapi.com",
    "X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  params={
    "artistId": "eninem"
  }
)
'''

# {'id': 13, 'name': 'Eminem', 'link': 'https://www.deezer.com/artist/13', 'share': 'https://www.deezer.com/artist/13?utm_source=deezer&utm_content=artist-13&utm_term=0_1561415089&utm_medium=web', 'picture': 'https://api.deezer.com/artist/13/image', 'picture_small': 'https://cdns-images.dzcdn.net/images/artist/0707267475580b1b82f4da20a1b295c6/56x56-000000-80-0-0.jpg', 'picture_medium': 'https://cdns-images.dzcdn.net/images/artist/0707267475580b1b82f4da20a1b295c6/250x250-000000-80-0-0.jpg', 'picture_big': 'https://cdns-images.dzcdn.net/images/artist/0707267475580b1b82f4da20a1b295c6/500x500-000000-80-0-0.jpg', 'picture_xl': 'https://cdns-images.dzcdn.net/images/artist/0707267475580b1b82f4da20a1b295c6/1000x1000-000000-80-0-0.jpg', 'nb_album': 65, 'nb_fan': 11955370, 'radio': True, 'tracklist': 'https://api.deezer.com/artist/13/top?limit=50', 'type': 'artist'}
# {'id': 13177249, 'name': 'Edsheeran', 'link': 'https://www.deezer.com/artist/13177249', 'share': 'https://www.deezer.com/artist/13177249?utm_source=deezer&utm_content=artist-13177249&utm_term=0_1561415140&utm_medium=web', 'picture': 'https://api.deezer.com/artist/13177249/image', 'picture_small': 'https://e-cdns-images.dzcdn.net/images/artist//56x56-000000-80-0-0.jpg', 'picture_medium': 'https://e-cdns-images.dzcdn.net/images/artist//250x250-000000-80-0-0.jpg', 'picture_big': 'https://e-cdns-images.dzcdn.net/images/artist//500x500-000000-80-0-0.jpg', 'picture_xl': 'https://e-cdns-images.dzcdn.net/images/artist//1000x1000-000000-80-0-0.jpg', 'nb_album': 0, 'nb_fan': 0, 'radio': False, 'tracklist': 'https://api.deezer.com/artist/13177249/top?limit=50', 'type': 'artist'}

response = requests.get("https://deezerdevs-deezer.p.rapidapi.com/search?q=ed+sheeran",
  headers={
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
    "X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade"
  }
)

ed_sheeran_data = response.json()

response = requests.get("https://deezerdevs-deezer.p.rapidapi.com/search?q=cardi+b",
  headers={
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
    "X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade"
  }
)

cardi_data = response.json()

response = requests.get("https://deezerdevs-deezer.p.rapidapi.com/search?q=eninem",
  headers={
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
    "X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade"
  }
)

eninem_data = response.json()
'''
print('Ed ========================')
print(ed_sheeran_data)
print('Cardi ========================')
print(cardi_data)
print('Eninem ========================')
print(eninem_data)

'''

ed_tracks = ed_sheeran_data['data']
#print(len(ed_tracks))

# how many albums
album_count = 0 
albums = {}   # empty dictionary
for track in ed_tracks:
    album_title = track['album']['title']
    if album_title in albums:
        # do not need to do anything
        pass
    else:
        albums[album_title] = 'present'     
        album_count += 1
    
#print('album count is',album_count)
#print('albums are',albums)


# most recent album
ed_albums = []
album_ids = []
for track in ed_tracks:
    ed_albums.append(track['album'])
    album_ids.append(track['album']['id'])

#print(ed_albums)
#print(album_ids)

# to find release date programmatically, get album IDs, make API calls with each ID and get release_date
eds_release_dates = []
for id_val in album_ids:
    response_data = requests.get("https://deezerdevs-deezer.p.rapidapi.com/album/"+str(id_val),
    headers={
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
    "X-RapidAPI-Key": "742017db4emsh75cfbd6592a303fp1d291bjsnabb9492f5ade"
    }).json()
    eds_release_dates.append(response_data['release_date'])

# set only allows unique values
print(set(eds_release_dates))

