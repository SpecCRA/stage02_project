# Things to change
# dictionaries for stuff, maybe
# global input variable
# while loop to for loop, maybe
# replace blank space with input answer
# create a function for the different levels

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
hard_q3 = "3. Is the sense of touch or the sense of pain transmitted faster? _____"
hard_q4 = "4. True or False, some alcohol is absorbed in the stomach."
hard_q5 = "5. _____ is a mutation where you have extra digits like fingers or toes."

# I thought it'd be a better idea to put variables into a list rather than long strings.
easy_q = [easy_q1, easy_q2, easy_q3, easy_q4, easy_q5]
med_q = [med_q1, med_q2, med_q3, med_q4, med_q5]
hard_q = [hard_q1, hard_q2, hard_q3, hard_q4, hard_q5]

# Right now, trying to figure out a nice way to allow input of both numbers and words for answers.
easy_ans = ["aorta", "mandible", "femur", "red blood cells", "dopamine"]
med_ans = ["three", "six", "twenty", "platelets", "ab"]
hard_ans = ["prefrontal cortex", "vena cava", "pain", "true", "polydactyly"]

# This will display the beginning with an opening message and level selection.
def opening_sequence():
    # starts with a prompt then directs towards a difficulty level after selection
    choose_difficulty = raw_input("Welcome! Please choose a difficulty to continue: easy, medium or hard. This quiz tests human physiology trivia. Your selection is: ")
    #just in case someone capitalizes something
    mod_selection = choose_difficulty.lower() 
    #print mod_selection  - This was just for me to check
    # directs program towards level selected
    if mod_selection == "easy":
        easy_level()
    if mod_selection == "medium":
        medium_level()
    if mod_selection == "hard":
        hard_level()
    #in case of typos or typing in something different
    else:
        print 'Select a difficulty from the choices.'
        return opening_sequence()

# ask_ques() is simply to display the question output and check the answer.
# A right answer prompts the next question. A wrong answer prompts to try again.
def ask_ques(ques_list, ans_list): 
    # this for loop didn't work at all. I tried to make it work with a for loop but couldn't do it.
    # I think I learned plenty about how for loops work by seeing... how they don't work.
#    queue = 0
#    for ques in ques_list[queue]:
#        print ques
#        ans_input = raw_input("Your answer:")
#        ans_input.lower()
#        if ans_input in ans_list:
#            print "Nice job!"
#            queue += 1
#        else:
#            print "Try again"
#            print ques
    # very strange to me, but a while loop worked much better for prompting and checking 
    count = 0
    while count < len(ques_list):
        print ques_list[count]
        ans_input = raw_input("Your answer: ")
        ans = ans_input.lower()
#        print ans - I initially didn't have it assigned to a variable, so I had to check.
        # the following sequence is to check answers. I tried to make a separate function, 
        # but the local ans_input variable didn't transfer over well
        if ans == ans_list[count]:
            print "Nice job!"
            count += 1
        else:
            print "Try again."

            
# I wanted to make a level selection per level to choose a different one but couldn't quite 
# quite figure that out without making a lot of redundant code
def level_selection():
    new_difficulty = raw_input("Select next level: easy, medium, hard, or end game. Enter choice here: ")
    mod_selection = new_difficulty.lower()
    if mod_selection == "easy":
        easy_level()
    elif mod_selection == "medium":
        medium_level()
    elif mod_selection == "hard":
        hard_level()
    else:
        if mod_selection == "end game":
            print "Thanks for playing! Game ending..."

# Each of the following simply is the output of the difficulty selected.
def easy_level():
    print "Easy selected. We'll start simple."
    ask_ques(easy_q, easy_ans)
    level_selection()

def medium_level():
    print "Medium selected. These may prove to be more trivial."
    ask_ques(med_q, med_ans)
    level_selection()
    
def hard_level():
    print "Hard selected. Good luck!"
    ask_ques(hard_q, hard_ans)
    level_selection()
    
opening_sequence()

# I know I have some redundant code with level selection. I didn't want them to display the same message though.
# I think the program is pretty concise besides that. 