import random
def startwordle():
    word_list = word_list = [
        "word", "game", "play", "home", "love", "tree", "book", "time", "team", "door",
        "shop", "idea", "fire", "cake", "rock", "bird", "fish", "road", "park", "jump",
        "star", "moon", "baby", "city", "face", "song", "rain", "math", "foot", "hand",
        "girl", "boy", "ship", "pool", "hill", "film", "town", "text", "land", "kiss",
        "hope", "sand", "food", "life", "hate", "race", "path", "soul", "spin", "care",
        "drop", "open", "ride", "trip", "yard", "kick", "nose", "wave", "knee", "loud",
        "cool", "neck", "pick", "thin", "pale", "fear", "twin", "flag", "gasp", "read",
        "fuel", "harm", "dark", "curl", "pond", "root", "lazy", "melt", "sigh", "grey",
        "toss", "grab", "sink", "skip", "deck", "long", "shot", "soft", "weak", "wind",
        "fail", "lack", "feet", "rope", "rest", "belt", "vest", "rain", "rare", "rich",
        "wide", "tail", "mild", "snap", "swim", "bind"
    ]
    target_word = random.choice(word_list)
    max_attempts = 10

    def check_word(guess_word):
        if len(guess_word) != 4:
            return False
        correct_pos = sum([1 for i in range(4) if guess_word[i] == target_word[i]])
        correct_letters = len(set(guess_word) & set(target_word)) - correct_pos
        print("Correct position:", correct_pos)
        print("Correct letters:", correct_letters)
        return guess_word == target_word

    attempts = 0
    while attempts < max_attempts:
        print("Attempt", attempts + 1)
        guess = input("Enter a four-letter word: ").lower()   
        if check_word(guess):
            print("Congratulations! You guessed the word correctly.")
            break
        attempts += 1

    if attempts == max_attempts:
        print("You ran out of attempts. The word was", target_word)
