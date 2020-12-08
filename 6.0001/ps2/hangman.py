# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return(all(x in letters_guessed for x in secret_word))
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    individual = [char for char in secret_word] 
    individual in letters_guessed
    boolelist=[i in letters_guessed for i in individual]   
    chars =[x if y==True else "_ " for x,y in zip(individual,boolelist)]
    stri =""
    return(stri.join(chars))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet=string.ascii_lowercase
    for i in letters_guessed :
        alphabet = alphabet.replace(i, '')
    return(alphabet)    
    


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    win = False
    lost = False
    letters_guessed=[]
    letters_available = get_available_letters(letters_guessed)
    wordlength = len(secret_word)
    print('Welcome to the game Hangman! I am thinking of a word that is', wordlength,'letters long.')
    print('------------')
    print('You have', guesses,' guesses left.')
    print('Available letters:',letters_available)
    print('Please guess a letter:')
    
   
   ##Game Loop##
    while win + lost == 0:
       recent_guess = str(input())
       remain = get_guessed_word(secret_word, letters_guessed)
       #lost = (guesses==0) or (warnings == 0)

       # if lost == True:
       #         print('you lose')
       
       if (recent_guess in letters_guessed) or (not str.isalpha(recent_guess)):
           warnings -=1
           lost = (guesses==0) or (warnings == 0)
           if warnings ==0:
               print('Sorry, you ran out of warnings. The word was',secret_word+'.')
           else:
               print('Oops! That is not a valid letter. You have', warnings ,'warnings left:',remain)
               # put if lost condition here
               print('------------')
               print('You have', guesses,' guesses left.')
               print('Available letters:',letters_available)
               print('Please guess a letter:')
       else:
           recent_guess = str.lower(recent_guess)
           letters_guessed.append(recent_guess)
           letters_available = get_available_letters(letters_guessed)
           remain = get_guessed_word(secret_word, letters_guessed)
           win = is_word_guessed(secret_word, letters_guessed)
           
           
            
           
           if win == True:
               score = guesses * wordlength
               print('Good guess:',remain)
               print('------------')
               print('Congratulations, you won!')
               print('Your total score for this game is:',score)
           
               
           else:
               if recent_guess in secret_word:
                    print('Good guess:',remain)
                    print('------------')
                    print('You have', guesses,' guesses left.')
                    print('Available letters:',letters_available)
                    print('Please guess a letter:')
               else:
                    guesses -=1
                    lost = (guesses==0) or (warnings == 0)
                    print('Oops! That letter is not in my word:',remain)
                    print('------------')
                    if guesses ==0:
                        print('Sorry, you ran out of guesses. The word was', secret_word+'.')
                    else:
                        print('You have', guesses,' guesses left.')
                        print('Available letters:',letters_available)
                        print('Please guess a letter:')
                   
            
      

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    mw = [char for char in my_word if char!=' ']  # use strip
    ow = [char for char in other_word if char!=' ']
    a = [y if x!='_' else '_' for x,y in zip(mw,ow)]
    b = [y for x,y in zip(mw,ow) if x=='_']
   
    # conditions
    con1 = len(mw) == len(ow)             # both words are same length
    con2 = a==mw                          # word is the same when replaced with blanks
    con3 = sum([x in mw for x in b]) == 0 # letter in blanks do not appear else where in the word
    
    return con1 and con2 and con3 



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pm = [y for x,y in zip([match_with_gaps(my_word,x) for x in wordlist],wordlist) if x ==True]
    return [x for x in [pm,'No matches found'] if x][0]




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    #Setup
    guesses = 6
    warnings = 3
    win = False
    lost = False
    letters_guessed=[]
    letters_available = get_available_letters(letters_guessed)
    wordlength = len(secret_word)
    print('Welcome to the game Hangman! I am thinking of a word that is', wordlength,'letters long.')
    print('------------')
    print('You have', guesses,' guesses left.')
    print('Available letters:',letters_available)
    print('Please guess a letter:')
    
    
    remain = get_guessed_word(secret_word, letters_guessed)
    
    
    #Game Loop
    while win + lost == 0:
        let = input()
        if let == '*':
            print('possible matches:')
            print(show_possible_matches(remain))
            print('------------')
            print('You have', guesses,' guesses left.')
            print('Available letters:',letters_available)
            print('Please guess a letter:')
            #hints
        else:
           recent_guess = str(let)
           remain = get_guessed_word(secret_word, letters_guessed)
           #lost = (guesses==0) or (warnings == 0)
    
           # if lost == True:
           #         print('you lose')
           
           if (recent_guess in letters_guessed) or (not str.isalpha(recent_guess)):
               warnings -=1
               lost = (guesses==0) or (warnings == 0)
               if warnings ==0:
                   print('Sorry, you ran out of warnings. The word was',secret_word+'.')
               else:
                   print('Oops! That is not a valid letter. You have', warnings ,'warnings left:',remain)
                   # put if lost condition here
                   print('------------')
                   print('You have', guesses,' guesses left.')
                   print('Available letters:',letters_available)
                   print('Please guess a letter:')
           else:
               recent_guess = str.lower(recent_guess)
               letters_guessed.append(recent_guess)
               letters_available = get_available_letters(letters_guessed)
               remain = get_guessed_word(secret_word, letters_guessed)
               win = is_word_guessed(secret_word, letters_guessed)
               
               
                
               
               if win == True:
                   score = guesses * wordlength
                   print('Good guess:',remain)
                   print('------------')
                   print('Congratulations, you won!')
                   print('Your total score for this game is:',score)
               
                   
               else:
                   if recent_guess in secret_word:
                        print('Good guess:',remain)
                        print('------------')
                        print('You have', guesses,' guesses left.')
                        print('Available letters:',letters_available)
                        print('Please guess a letter:')
                   else:
                        guesses -=1
                        lost = (guesses==0) or (warnings == 0)
                        print('Oops! That letter is not in my word:',remain)
                        print('------------')
                        if guesses ==0:
                            print('Sorry, you ran out of guesses. The word was', secret_word+'.')
                        else:
                            print('You have', guesses,' guesses left.')
                            print('Available letters:',letters_available)
                            print('Please guess a letter:')

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

