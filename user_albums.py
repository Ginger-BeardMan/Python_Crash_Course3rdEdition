def make_album():
	
	album = True

	albums = {}

	while album:
		artist_name = input("Please enter one of your favorite musician's names. ")
		album_title = input("What is your favorite album by them? ")
		song_number = input("If you know, how many songs were on that album? (Enter unkown if you aren't sure.) ")
			
		albums['Artist'] = artist_name
		albums['Album'] = album_title
		albums['Songs'] = song_number
		
		if song_number == 'unknown':
			song_number == None
			albums = {'Artist': artist_name.title(), 'Album': album_title.title()}
		else:
			albums = {'Artist': artist_name.title(), 'Album': album_title.title(), 'Songs': song_number}

		print(albums)

		all_done = input("Would you create another artist album? ")

		if all_done == 'no':
			album = False

make_album()