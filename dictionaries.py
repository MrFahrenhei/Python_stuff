#!/bin/python3

def new_line():
    print('\n')


new_line()

# Dictionaries
print("Dictionaries are keys and values:")
# list []
# ()
# {} Dictionaries

drinks = {"White Russians": 7, "old Fashion": 10, "lemon Drop": 8,
          "Buttery Nipple": 6}  # Drink is key, price is value
print(drinks)

#List and dictionaries
movies = ["When Harry Met Sally", "The Hangover",
          "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Bob", "Leah", "Jeff"]
combined = zip(movies, person)
movie_directionary = {key: value for key, value in combined}
print(movie_directionary)
