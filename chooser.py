from random import choice
from animeAPI import AnimeAPI

# #create list of animes
# animes = [['naruto','action', 'series', 'long'], ['haikyuu', 'sports', 'friendship', 'series'], ['mushishi', 'music', 'romance', 'series']]

# #input mood
# print('what mood are you in?')
# mood = input()

# #loop through and find a matching mood
# for item in animes:
#     if item[1] == mood:
#         print(mood + ' anime: ' + item[0])

data_fields = {1: "rating", 2: "episodes", 3: "status"}


def get_valid_input():
    try:
        user_input = int(input(
            "Would you like more information, such as rating(1), episode(2), status(3)? \n"))
        if user_input in data_fields:
            return user_input
        else:
            return get_valid_input()
    except:
        return get_valid_input()


print("Welcome to anime randomizer!")
user_input = input("Would you like a random anime to watch? \n")
while user_input == 'yes':
    randomizer = AnimeAPI()
    randomizer.get_random_anime()
    randomizer.print_data()
    user_input = get_valid_input()
    # print(randomizer.data["data"][data_fields[user_input]])
    user_input = input("Would you like another random anime to watch? \n")

print("Awesome. Have a nice day!")
