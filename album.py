def make_album(artist_name, album_title, song_number = None):
	
	if song_number:
		albums = {'Artist': artist_name, 'Album': album_title, 'Songs': song_number}
	else:
		albums = {'Artist': artist_name, 'Album': album_title}

	albums['Artist'] = artist_name
	albums['Album'] = album_title
	print(albums)

make_album('Metallica', 'Black Album')

make_album('Rush', '2112', song_number = 6)

make_album('Black Sabbath', 'Black Sabbath')