# import the random module
import random

# fetch a list of words from an online dictionary
import urllib.request, urllib.parse, urllib.error
def fetch_words_english():
    """Fetch a list of words from a URL.
    Returns a list of valid words.
    """
    url = urllib.request.urlopen("http://greenteapress.com/thinkpython/code/words.txt")
    text = url.read().decode()
    words = text.splitlines()
    return words

def fetch_words_german():
    url = urllib.request.urlopen("https://raw.githubusercontent.com/enz/german-wordlist/master/words")
    text = url.read().decode()
    words = text.splitlines()
    return words

# create a game where the user has to guess a word
def main():
    # Create an input asking the user which language he wants to play the game
    language = input("English / German : ")
    if language.lower() == "english":
        WORDS = fetch_words_english()

         # get a random word from the list
        word = random.choice(WORDS)
        # create a variable to use later to see if the user guessed the word
        correct = word
        # create a jumbled version of the word
        jumble =""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]
        # start the game
        print("Welcome to the Word Jumble game.")
        print("Unscramble the letters to make a word.")
        print("(Press the enter key at the prompt to quit.)")
        print("The jumble is:", jumble)
        # start the game loop
        guess = input("\nYour guess: ")
        while guess != correct and guess != "":
            print("Sorry, that's not it." + correct)
            guess = input("Your guess: ")
        if guess == correct:
            print("That's it! You guessed it!\n")
            print("Thanks for playing.")
    elif language.lower() == "german":
        WORDS = fetch_words_german()
         # get a random word from the list
        word = random.choice(WORDS)
        # create a variable to use later to see if the user guessed the word
        correct = word
        # create a jumbled version of the word
        jumble =""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]
        # start the game
        print("Willkommen beim Wort-Wirrwarr.")
        print("Bringe die Buchstaben in die richtige Reihenfolge und errate das Wort.")
        print("(Drücke bei der Eingabe irgendeine Taste, um das Spiel zu beenden.)")
        print("Das durcheinandergebrachte Wort ist:", jumble)
        # start the game loop
        guess = input("\nDeine Vermutung: ")
        while guess != correct and guess != "":
            print("Schade, das war leider nicht das richtige Wort." + correct)
            guess = input("Deine Vermutung: ")
        if guess == correct:
            print("Das ist es! Du hast das Wort erraten, herzlichen Glückwunsch!\n")
        print("Danke fürs Spielen.")
   

if __name__ == "__main__":
    main()