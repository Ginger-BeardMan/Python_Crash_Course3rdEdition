def build_profile(first, last, **user_info):
	'''build a dictionary containing everything we know about a user'''
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('Fen', 'Kay', age='78', hobbie='drums', location='moon')

print(user_profile)