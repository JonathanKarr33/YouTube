#code was inspired from @Tech Tribe https://github.com/techtribeyt/Wordle
from words import get_wordle_guesses, get_wordle_answers
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import keyboard

def play(game_rows, browser, possible_guesses, possible_answers):
    # get the word list
    words = possible_guesses
    narrowed_down_list = possible_answers

    for guess_number in range(5):
        min_wordcount = 2e5 #less than 20 thousand words
        chosen_word = ""
        evaluation_to_wordlist_map = {}
        
        
        if guess_number != 0:
            words_to_consider = words
        else:
            words_to_consider = ["arise"]
    
        # see what word reduces the list the most
        for word_to_guess in words_to_consider:
            temp_eval_to_words_map = {}
            
            # evaluate with every possible answer
            for possible_answer in narrowed_down_list:
                evaluation = get_evaluation(possible_answer, word_to_guess)
                        
                # store word by evaluation tuple in a list
                if tuple(evaluation) not in temp_eval_to_words_map:
                    temp_eval_to_words_map[tuple(evaluation)] = [possible_answer]
                else:
                    temp_eval_to_words_map[tuple(evaluation)].append(possible_answer)
    
    
            # metric we are trying to minimize
            biggest_possible_remaining_wordcount = max([len(val) for val in temp_eval_to_words_map.values()])

            if biggest_possible_remaining_wordcount < min_wordcount:
                min_wordcount = biggest_possible_remaining_wordcount
                chosen_word = word_to_guess
                evaluation_to_wordlist_map = temp_eval_to_words_map
        enter_guess(chosen_word)
        time.sleep(1)
        answer_evaluation = get_wordle_evaluation(game_rows[guess_number], browser)
        if answer_evaluation in evaluation_to_wordlist_map:
            narrowed_down_list = evaluation_to_wordlist_map[answer_evaluation]
            
        if answer_evaluation == [2, 2, 2, 2, 2]: # 2 is correct location
            return [chosen_word]
        time.sleep(1)
        
        if len(narrowed_down_list) == 1:
            enter_guess(narrowed_down_list[0])
            return [chosen_word]
    return narrowed_down_list
            

def get_wordle_evaluation(game_row, browser):
    row = browser.execute_script('return arguments[0].shadowRoot', game_row)
    tiles = row.find_elements(By.CSS_SELECTOR, "game-tile")
    evaluation = []
    eval_to_int = {
        "correct": 2,
        "present": 1,
        "absent": 0
    }
    for tile in tiles:
        evaluation.append(eval_to_int[tile.get_attribute("evaluation")])
    return tuple(evaluation)   
    
def enter_guess(word):
    keyboard.write(word, delay=0.05)
    keyboard.press_and_release('enter')

def get_evaluation(answer, word):
    # 0 = nothing, 1 = yellow, 2 = green
    output = [0, 0, 0, 0, 0]
    
    # check for correct letter and placement
    for i in range(5):
        if word[i] == answer[i]:
            output[i] = 2
            answer = answer[:i] + ' ' + answer[i + 1:]
           
    # check for correct letter
    for i in range(5):
        char = word[i]
        if char in answer and output[i] == 0:
            output[i] = 1
            first_occurence = answer.find(char)
            answer = answer[:first_occurence] + ' ' + answer[first_occurence + 1:]
    return tuple(output)

def main():
    start_button = 'esc'

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.powerlanguage.co.uk/wordle/")
    keyboard.wait(start_button)

    game_app = browser.find_element(By.TAG_NAME, 'game-app')
    board = browser.execute_script("return arguments[0].shadowRoot.getElementById('board')", game_app)
    game_rows = board.find_elements(By.TAG_NAME, 'game-row')
        
    play(game_rows, browser, get_wordle_guesses(), get_wordle_answers())
    keyboard.wait(start_button)

if __name__ == "__main__":
    main()