
import random
def number_c (min_value, max_value, guess_value, random_number):
    """
    Generates a random number between min_value and max_value and checks guess_value.

    :parameter
    :param min_value (int): the minimum value to generate
    :param max_value (int): the maximum value to generate
    :param guess_value (int): the guess value of user input
    :param random_number (int): the random number generates a random number between min_value and max
    :return:
    """
    global correct
    correct = False
    if guess_value < min_value or guess_value > max_value:
        print("Invalid guess value range")
    elif guess_value < random_number:
        print("lower guess value")
    elif guess_value > random_number:
        print("upper guess value")
    else:
        print("correct guess")
        correct = True

min = int(input("enter the minimum value: "))
max = int(input("enter the maximum value: "))

i = 1
random_number = random.randint(min, max)
while i < 6:
    guess = int(input(f"Enter the guess value{i}: "))
    number_c(min, max, guess, random_number)
    if correct == True:
        break
    i += 1