import random
import hangman_art
from hangman_words import word_list
from os import system


stages_from_module = hangman_art.stages
lives=len(stages_from_module)
chosen_word = random.choice(word_list)
hint=random.choice(chosen_word)

print(hangman_art.logo,'\n')

print("you need to guess the following word by guessing a letter at a time.\nyou have a total of 7 lives and you lose a life everytime you guess a wrong letter.\nGood luck!!!\n")

display=[]
for i in range(len(chosen_word)):
    display += "_"

def letter_popup(L,temp,value = chosen_word):  
          
    for i in range(len(value)) :     

        if value[i] == L  :
            display[i] = value[i]
                        
        else:
            temp += 1   
    return temp
            
letter_popup(hint,0)

end_of_game = False

while not end_of_game :
    print(f"{' '.join(display)}")
    letter = input("\nguess a letter from a to z in lower case :  ")
    system('cls')
    temp=0

# to check the if the guessed letter is in the chosen word
    if letter in display:
            print("This letter has already been guessed, no life lost")
            temp=temp-1

    temp+=letter_popup(letter,temp)

# to print the hangman
    if temp == len(chosen_word):            #temp variable will become equal to the number of elements in display when no character matches the word.
        lives -= 1                          #to keep count of lives
        print(stages_from_module[lives])                                  
        print(f"Letter '{letter}' not found \n")
    print(f"lives left : {lives} \n")     

# to check if you won the game    
    if "_" not in display:
        end_of_game=True
        print(f"the word was '{chosen_word}'")
        print("you won!\n")

    elif(lives==0):
        end_of_game=True
        print("you lost!")
        print(f"the word was '{chosen_word}'")

    