def playlist():

    songs = [{'title': 'A Little Respect', 'genre': 'Pop', 'artist': 'Erasure', 'year': '1988', 'length': 3.32}, {'title': 'We Found Love', 'genre': 'Electro house', 'artist': 'Rihanna', 'year': '2011', 'length': 3.35}, {'title': 'Grace Kelly', 'genre': 'Pop', 'artist': 'Mika', 'year': '2006', 'length': 3.05}, {'title': 'Song for a Winters Night', 'genre': 'Folk', 'artist': 'Sarah McLachlan', 'year': '1996', 'length': 3.01}, {'title': 'Mirror in the Bathroom', 'genre': 'new wave', 'artist': 'The Beat', 'year': '1980', 'length': 3.10}, {'title': 'Love and Affection', 'genre': 'Folk', 'artist': 'Joan Armatrading', 'year': '1974', 'length': 4.28}, {'title': 'Love Runs Out', 'genre': 'Pop', 'artist': 'OneRepublic', 'year': '2014', 'length': 3.44}, {'title': 'Believe', 'genre': 'Dance-Pop', 'artist': 'Cher', 'year': '1998', 'length': 3.59}, {'title': 'When I Am Up', 'genre': 'Folk', 'artist': 'Great Big Sea', 'year': '1997', 'length': 3.24}, {'title': 'Feel It Still', 'genre': 'funk', 'artist': 'Portugal. The Man', 'year': '2017', 'length': 2.42}]

    #action = input("Choose the action you want to take\n 1. Print all the songs \n 2. Print all the artists in the list \n 3. Print the total play length of the playlist \n 4. Print the most popular genre \n")
    action = input("Choose the action you want to take\n 1. Print all the songs \n 2. Print all the artists in the list \n 3. Print the total play length of the playlist \n")

    playlist_length = 0.0

    if action == '1':
        for song in songs:
            print(song['title'])

    elif action == '2':
        for song in songs:
            print(song['artist'])

    elif action == '3':
        hours = 0 
        mn = 0 
        sec = 0 

        for song in songs:
            playlist_length += song['length']
        
        hours = int( playlist_length / 60 )
        mn = int(playlist_length % 60 )
        sec = ( playlist_length - ( hours * 60) - mn ) * 60 


        print('Playlist is ', playlist_length, ' minutes long.')
        print(f'Playlist is {hours} hours, {mn} minutes and {sec} seconds long.')

playlist()
    


'''
elif action == '4':
    genres = []
    index = -1 
    for song in songs:
        index += 1
        genres(index) = [song['genre'0playlist_length += song['length']

'''
