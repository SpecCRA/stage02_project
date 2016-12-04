# 3 levels, easy, medium, hard
# 5 fill in the blank questions per level

easy_q1 = "1. The largest artery in the body is the _____" + "."
easy_q2 = "2. _____ is the official name of your jawbone."
easy_q3 = "3. The _____ is the biggest bone in the body."
easy_q4 = "4. _____ circulate oxygen to the body."
easy_q5 = "5. The neurotransmitter _____ is associated with happiness and crack."

med_q1 = "1. Your skin has _____ (enter a word) layers."
med_q2 = "2. The small intestine is an astonishing _____ (enter a word) meters long."
med_q3 = "3. Your brain uses _____ (enter a word) percentage of energy."
med_q4 = "4. When your body is injured, _____ are cells associated with blood clotting"
med_q5 = "5. Blood type _____ is the universal acceptor."

hard_q1 = "1. The _____ of the brain is responsible for motor function."
hard_q2 = "2. The largest vein in the body is called the _____" + "."
hard_q3 = "3. Is the sense of touch or the sense of pain transmitted faster? _____" + "."
hard_q4 = "4. True or False, some alcohol is absorbed in the stomach. _____"
hard_q5 = "5. _____ is a mutation where you have extra digits like fingers or toes."

# To simplify my methods to call game data, I included everything into dictionaries as suggested. 
# I did totally get lazy with typing everything again since my variables were already defined.
# I think this is still more organized than having the whole strings in dictionaries.
game_data = {
    "easy": {
        "opening_message": "Easy selected. We'll start simple.",
        "ques": [easy_q1, easy_q2, easy_q3, easy_q4, easy_q5],
        "ans": ["aorta", "mandible", "femur", "red blood cells", "dopamine"]
    },
    "medium": {
        "opening_message": "Medium selected. These may prove to be more trivial.",
        "ques": [med_q1, med_q2, med_q3, med_q4, med_q5],
        "ans": ["three", "six", "twenty", "platelets", "ab"]
    },
    "hard": {
        "opening_message": "Hard selected. Good luck!",
        "ques": [hard_q1, hard_q2, hard_q3, hard_q4, hard_q5],
        "ans": ["prefrontal cortex", "vena cava", "pain", "true", "polydactyly"]
    }
}

def level_selection():
    """
    level_selection() prompts the user to select the next difficulty or leave the program.
    """
    new_difficulty = raw_input("Enter choice here: ")
    mod_selection = new_difficulty.lower()
    if mod_selection in game_data.keys():
        level(mod_selection)
    elif mod_selection == "end game":
        print "Thanks for playing! Game ending..."
    else:
        if mod_selection not in game_data.keys() or "end game":
            print "Please enter a valid choice."
            level_selection()
    
def ask_ques(diff_selected): 
    """
    This function is used to ask and check quiz questions and answers, moving onto the next question if correct, and prompting the user to try again if wrong
    """
    count = 0
    num_of_ques = len(game_data[diff_selected]["ques"]) # the total number of questions per difficulty
    while count < num_of_ques:
        ques_num = game_data[diff_selected]["ques"][count]
        ans_num = game_data[diff_selected]["ans"][count]
        print ques_num
        ans_input = raw_input("Your answer: ")
        ans = ans_input.lower()
        if ans == ans_num:
            print "Nice job!"
            new_sent = ques_num.replace("_____", ans)
            print new_sent
            count += 1
        else:
            print "Try again."
        
def level(diff):
    """
    level(diff) is the function that runs each level difficulty.
    """
    opener = game_data[diff]["opening_message"]
    print opener
    ask_ques(diff)
    print "Select next level to continue: easy, medium, hard, or end game."
    level_selection()
  
print "Welcome! Please choose a difficulty to continue: easy, medium or hard. This quiz tests human physiology trivia."
level_selection()
# Finally done!
# Thanks for taking the time to go through my mess of code! I hope it was all legible.
