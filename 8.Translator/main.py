german_lan = {
    "Hello": "Hallo",
    "Good morning": "Guten Morgen",
    "Good": "Gut",
    "Fast": "Schnell",
    "Slow": "Langsam",
} # This is a dictionary code I've creaded for english to german!

user_get = input("Enter a world in english and get it back in german: ").capitalize() # User request to enter an english word and is not case sensitive!

'''
This checks if the word is in the dictionary I've creaded
if it is will tell the user translation for that word in
german! Else can't find the word it will print out that 
word was not there!
'''
if german_lan.get(user_get):
    print("English word: " + user_get + " in german is: " + german_lan[user_get])
else:
    print(f"Word {user_get} is not in Dictionary!")