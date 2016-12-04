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

# This will display the beginning with an opening message and level selection.
def opening_sequence():
    # starts with a prompt then directs towards a difficulty level after selection
    choose_difficulty = raw_input("Welcome! Please choose a difficulty to continue: easy, medium or hard. This quiz tests human physiology trivia. Your selection is: ")   
    #just in case someone capitalizes something
    mod_selection = choose_difficulty.lower() 
    if mod_selection == "easy" or mod_selection == "medium" or mod_selection == "hard":
        level(mod_selection)
    else:
        print 'Select a difficulty from the choices.'
        return opening_sequence()
    
# My logic behind the opening sequence is first to prompt for a difficulty while coding defensively
# against typos, other inputs, or different capitalizations.

# find_blank(list) returns the position of the blanks or blanks with a period.
# I looked up the index function. I don't think it was covered in the lectures.
# But then neither were dictionaries outside of the webcasts ಠ_ಠ
def find_blank(working_list):
    if "_____" in working_list:
        pos = working_list.index("_____")
    if "_____." in working_list:
        pos = working_list.index("_____.")
    return pos
       
# ask_ques() is simply to display the question, prompt an input, and check the answer with the answers list.
# A right answer prompts the next question and fills in the blank. A wrong answer prompts to try again.
def ask_ques(diff_selected): 
    count = 0
    num_of_ques = len(game_data[diff_selected]["ques"]) # the total number of questions per difficulty
    # I couldn't get the for loop to let the player try again on the same question 
    # if he or she entered the wrong answer, so I stuck with my while loop.
    # This is just because I could keep a count and restart the loop at certain counts.
#    for number in range(0, num_of_ques):
#        print game_data[diff_selected]["ques"][number]
#        ans_input = raw_input("Your answer: ")
#        ans = ans_input.lower()
#        if ans == game_data[diff_selected]["ans"][number]:
#            print "Nice job!"
#            continue
#        else:
#            print "Try again."
#            print game_data[diff_selected]["ques"][number] 
    while count < num_of_ques:
        ques_num = game_data[diff_selected]["ques"][count]
        ans_num = game_data[diff_selected]["ans"][count]
        # I thought it'd make a mess to call things deeply nested in dictionaries. 
        # So I assigned them to variables instead.
        print ques_num
        ans_input = raw_input("Your answer: ")
        ans = ans_input.lower()
        #print ans - I initially didn't have it assigned to a variable, so I had to check.
        # the following sequence is to check answers. I tried to make a separate function, 
        # but the local ans_input variable didn't transfer over well
        if ans == ans_num:
            print "Nice job!"
            ques_string = ques_num.split()
            ques_string[find_blank(ques_string)] = ans
            new_sent = " ".join(ques_string)
            print new_sent
            count += 1
        else:
            print "Try again."

# level_selection is a prompt for the next difficulty.
# The intention behind the else parts is so the program won't end in an error if user types in 
# something that isn't accepted within the function.
def level_selection():
    new_difficulty = raw_input("Select next level: easy, medium, hard, or end game. Enter choice here: ")
    mod_selection = new_difficulty.lower()
    # print mod_selection - checking stuff!
    if mod_selection in game_data.keys():
        # print "you did this right" 
        level(mod_selection)
    elif mod_selection == "end game":
        print "Thanks for playing! Game ending..."
    else:
        if mod_selection not in game_data.keys() or "end game":
            print "Please enter a valid choice."
            level_selection()
        
# level(diff) is just a function that operates each level with input being the difficulty
def level(diff):
    opener = game_data[diff]["opening_message"]
    print opener
    ask_ques(diff)
    level_selection()
     
opening_sequence()
# Finally done!
# Thanks for taking the time to go through my mess of code! I hope it was all legible.