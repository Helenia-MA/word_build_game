"""
let me create a list of dicts of about 5 games where @ dict has the words for one game
steps:
1) generate a chunk of say 5 random letters
2) provide all the possible words that can be formed from some or all of the letters
3) for @ word, its length = points awarded
4) create a dict with the word as key and its points as value for ease in awarding points
5) if possible set timer for it and deduct say 0.5 points for @ 2 minutes spent by the player
"""
import random
import itertools

#importing word_list to enable word check for validation
with open("words_alpha.txt", "r") as file:
    word_list = [line.strip().lower() for line in file]

def main():
    name = input("PLAYER'S NAME: ")
    points = 0
    print(f"{name}, Welcome to the Spelling B🐝 game")
    word = generate_chunk()
    print(f"Use the letters given to form as many words as possible!! \nYour letters are .... {word}")
    bee_dict = possible_words(word)
    total_possible_points = sum([len(choice) for choice in bee_dict])
    trials = len(bee_dict) + 5

   #game
    print(f"maximum points you can earn is: {total_possible_points} \nYou have {trials} trials, to guess {len(bee_dict)} words")
    while trials > 1:
        guess = input("Enter possible word: ")
        guess = guess.lower()
        if guess in bee_dict:
            points += len(guess)
            bee_dict.remove(guess)
            print(f"wonderful: you have earned {len(guess)} points, TOTAL POINTS: {points}")
        else:
            print(f"Sorry, no such word exists. try again")
        trials -= 1
        print(f"TRIALS REM: {trials -1}, WORDS REM: {len(bee_dict)}, LETTERS: {word}")
   
    print(f"GAME OVER!! POINTS EARNED: {points}/{total_possible_points}")
    start = input("ready for another round? Yes / No? ")
    start = start.lower()
    if start == 'yes':
        return main()



def generate_chunk():
    letters = random.choices("abcdefghijklmnopqrstuvwxyz", k = 5)
    letters = ''.join(letters)
    vowels = 'aeiou'
    if any(vowel in letters for vowel in vowels):
        return letters
    else:
        return generate_chunk()

def possible_words(chunk):
    valid_words = []
    for i in range(2, len(chunk) + 1):  # at least 2-letter words
        for combo in itertools.permutations(chunk, i):
            word = ''.join(combo)
            if word in word_list:
                valid_words.append(word)
    return valid_words

main()
