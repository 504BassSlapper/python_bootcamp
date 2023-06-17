
# randomize this word (take it from a list of word)
word = "hangman"

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

list_index = []
counter = 0

def show_letters_left(listIndex):
    shown_word = len(word)* '_'
    list_to_print = list(shown_word)
    for i,letter in enumerate(word):
        for j in listIndex: 
            if i == j:
                list_to_print[j] = list(word)[j]
    
    print(f" {list_to_print}")

def check_choosen_letter(choosen_letter, list_index):
    flag = False
    for i, letter in enumerate(word): 
        if letter == choosen_letter:
            list_index.append(i)
            flag = True
    return flag
    
while counter < len(HANGMAN_PICS)-1:
    if len(list_index) == len(word):
       print(" You win congrats !")
       break
    show_letters_left(list_index)
    choosen_letter = input("choose a letter: ").lower()
    print(list_index)
    if check_choosen_letter(choosen_letter, list_index) == False:
       counter +=1  
       print(f"{HANGMAN_PICS[counter]}")
       if counter == len(HANGMAN_PICS): 
           print("game over : the word was: \n {word}, good luck for the next time")

        
    

