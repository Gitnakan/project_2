import random

# Define the templates
template1 = "It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) ! "
template2 = "This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!! "
template3 = "Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!"

# Ask the user to choose a template
print("Choose a template:\n1. Hospital\n2. Camping\n3. Enchanted Castle")
choice = int(input("Enter the number of the template you want to use: "))

# Prompt the user for input based on the chosen template
if choice == 1:
    # Prompt the user to enter information
    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    mode_of_transportation = input("Enter a mode of transportation: ")
    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun = input("Enter a noun: ")
    color = input("Enter a color: ")
    part_of_the_body = input("Enter a part of the body: ")
    verb = input("Enter a verb: ")
    number2 = input("Enter another number: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    part_of_the_body2 = input("Enter another part of the body: ")
    verb2 = input("Enter another verb: ")
    noun4 = input("Enter another noun: ")
    adjective3 = input("Enter another adjective: ")
    silly_word = input("Enter a silly word: ")
# Print the story with the user's information
    print(f"It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. There are nurses here who have {color} {part_of_the_body}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_body2}. I heard that all doctors {verb2} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun}!")
elif choice == 2:
    # Prompt the user to enter information
    person_name = input("Enter a person's name: ")
    noun = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    verb2 = input("Enter a verb ending in 'ing': ")
    color = input("Enter a color: ")
    adverb = input("Enter an adverb ending in 'ly': ")
    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    color2 = input("Enter a color: ")
    animal2 = input("Enter an animal: ")
    number2 = input("Enter a number: ")
    silly_word = input("Enter a silly word: ")
    noun2 = input("Enter another noun: ")
# Print the story with the user's information
    print(f"This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective1} to {verb} in a tent. I am {adjective2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb2}. Then we will {adverb} hike through the forest for {number} {measure_of_time}. If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!")
elif choice == 3:
    person_name = input("Enter a proper noun (person's name): ")
    adj1 = input("Enter an adjective: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    place = input("Enter a place: ")
    adj2 = input("Enter an adjective: ")
    magical_creature_plural1 = input("Enter a plural noun for a magical creature: ")
    adj3 = input("Enter an adjective: ")
    magical_creature_plural2 = input("Enter another plural noun for a magical creature: ")
    room_in_a_house = input("Enter a room in a house: ")
    noun = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    noun_plural3 = input("Enter a plural noun: ")
    adj4 = input("Enter an adjective: ")
    noun_plural4 = input("Enter a plural noun: ")
    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    adj5 = input("Enter an adjective: ")
    noun5 = input("Enter a noun: ")
    silly_words = ['googly', 'silly', 'funny', 'wacky', 'zany', 'goofy', 'absurd']
    silly_word = random.choice(silly_words)
    print(f"Dear {person_name}, I am writing to you from a {adj1} castle in an enchanted forest. "
      f"I found myself here one day after going for a ride on a {color} {animal} in {place}. "
      f"There are {adj2} {magical_creature_plural1} and {adj3} {magical_creature_plural2} here! "
      f"In the {room_in_a_house} there is a pool full of {noun}. "
      f"I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adj4} {noun_plural4}. "
      f"It feels as though I have lived here for {number} {measure_of_time}. "
      f"I hope one day you can visit, although the only way to get here now is {verb_ing} on a "
      f"{adj5} {noun5}!! The most {silly_word} thing about this place is the enchanted forest!")
else:
    print("Invalid choice.")