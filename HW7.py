#Homework #7 - Dictionaries and Sets

song = {"Genre":"Country",
        "Artist":"Kelsea Ballerini",
        "Song":"half of my hometown",
        "DurationInSeconds":"236"}

for key in song:
    print("{0:s}: \"{1:s}\"".format(key.capitalize(), song[key]))


#Extra Credit

def guess(key, value):
    return key in song and song[key] == value


print("\n\nGuess:\n\n")
print("Is the title of this song \"half of my hometown\"?: {}".format(
    guess("title", "half of my hometown")))
print("Is the genre\"Country\"?: {}".format(
    guess("genre", "country")))