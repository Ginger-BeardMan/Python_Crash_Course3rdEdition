# Using each action/function that was reviewed in Ch. 3 at least one time for lists. 

learned_languages = ['English', 'Celtic', 'Klingon', 'Chinese']

print(learned_languages)

print("I don't recognized all of these, let's update this list.")

learned_languages.pop(2)

print(learned_languages)

print("We're getting closer.")

del learned_languages[1]

print(learned_languages)

print("Almost.")

learned_languages.remove('Chinese')

print(learned_languages)

print("That's all that don't belong. Let's add some more that I have started learning.")

learned_languages.append('Japanese')

print(learned_languages)

learned_languages.insert(0, 'Norwegian')

print(learned_languages)

learned_languages.append('German')

print(learned_languages)

print("Let's mess around with the order of things. First, reverse order.")

learned_languages.reverse()

print(learned_languages)

print("Next, sorted order.")

print(sorted(learned_languages))

print("Lastly, let's put them in alphabetical order for good.")

learned_languages.sort()

print(learned_languages)