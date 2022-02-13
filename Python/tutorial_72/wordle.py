words = []
with open("Python/tutorial_72/valid_wordle_answers.txt") as file:
    for line in file:
        words.append(line.strip())

def play_wordle(words : list) -> None:
    """Eliminate incorrect words"""
    while len(words) > 1:
        letters_in_word = []
        for position in range(5):
            letter = input("What letter did you put in position " + str(position+1) +"?: ").lower()
            color = input("What color is it (G,Y,B)?: ").lower() #green, yellow, or black
            if color != 'g' and color != 'y' and color != 'b':
                print("Invalid input")
                return
            words_to_remove = []
            for word in words:
                if color == 'g':
                    if word[position] != letter:
                        words_to_remove.append(word)
                        if letter not in letters_in_word:
                            letters_in_word.append(letter)
                elif color == 'y':
                    if letter not in word:
                        words_to_remove.append(word)
                    elif word[position] == letter:
                        words_to_remove.append(word)
                    if letter not in letters_in_word:
                        letters_in_word.append(letter)
                elif color == 'b':
                    if letter in word:
                        if letter not in letters_in_word:
                            words_to_remove.append(word)
                        elif words[position] == letter:
                            words_to_remove.append(word)
            for word in words_to_remove:
                words.remove(word)
        print(words)
        guess = input("Did you guess correctly (Y/N)?: ").lower()
        if guess == 'y':
            print("Congrats you won")
            return
play_wordle(words)