import art
from game_data import data
import random


def get_data():
    """
    This function will get a random index generated from the list of dictionaries called 'data'
    :return: it will return the dictionary with the random index allocated.
    """
    item_information = data[random.randint(0, len(data) - 1)]
    return item_information


def compare_options():
    """
    This function will compare the followers from the two random selected options and then, it will check if the user's
    guess is correct, if user is right: it will add +1 score, while user is right it will keep generating a new
    option plus the older one. When the user is wrong it will return the final score.
    """
    option_a = get_data()
    option_b = get_data()
    score = 0
    correct_option = True
    print(art.logo)
    while correct_option:
        if option_a != option_b:
            print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
            print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")
        else:
            option_b = get_data()
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choice == 'A':
            if option_a['follower_count'] > option_b['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
                option_a = option_b
                option_b = get_data()
                correct_option = True
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                correct_option = False
        else:
            if option_b['follower_count'] > option_a['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
                option_a = option_b
                option_b = get_data()
                correct_option = True
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                correct_option = False
