def get_wordle_guesses():
    words = []
    with open("Python/tutorial_73/valid_wordle_guesses.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words

def get_wordle_answers():
    words = []
    with open("Python/tutorial_73/valid_wordle_answers.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words