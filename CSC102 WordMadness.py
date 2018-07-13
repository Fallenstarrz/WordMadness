#####################################################################################################################
#                                                                                                                   #
# In this assignment you will write a Python program that counts vowels or consonants for a set of words,           #
#     and calculates the average number of vowels or consonants across the set of words.                            #
#                                                                                                                   #
# User interaction with the program should look like this:                                                          #
#                                                                                                                   #
# 1. Program Starts and asks the user whether they want to count vowels or consonants or quit.                      #
#       The input value is stored as a "mode". If user provides input other than "consonant"                        #
#       or "vowel" or "quit", program interprets this as an error and re-asks for input.                            #
# 2. Program asks for a word.                                                                                       #
# 3. Depending on mode, the number of consonants or vowels are calculated and reported to the user.                 #
# 4. Program asks if another word is available. If so, steps 2 through 4 are repeated, otherwise continue to step 5.#
# 5. Average vowels per word or average consonants per word are reported to the user.                               #
#                                                                                                                   #
# Be sure to use comments for both structure of the program and documentation of the code.                          #
# All code must completely be your own individual work product.                                                     #
# Post your Python program here.                                                                                    #
#                                                                                                                   #
#####################################################################################################################

#Tutor said: "Try not to use variables from main functions in other functions, because python 'sometimes' reads them strangely and can mess up your program"

def validMode(x):                                                                                   # This will validate your selection of mode
    while True:                                                                                     # This loop will continue forever, so we only break loop if function returns
        if(x == 'vowels'):                                                                          # If mode is vowels
            print('We are going to count vowels.')                                                  # Let user know they are going to count vowels
            return(x)                                                                               # Return the mode type
        elif(x == 'consonants'):                                                                    # If mode is consonants
            print('We are going to count consonants.')                                              # Let user know they are going to count consonants
            return(x)                                                                               # Return the mode type
        elif(x == 'quit'):                                                                          # If mode is quit
            return(x)                                                                               # Return the mode type
        else:                                                                                       # If mode isn't any of the above
            print('Error')                                                                          # Let user know there was an error while selecting mode
            x = input('Please select vowels, consonants, or quit.')                                 # Ask user to select a valid mode once again

def validWord(y):                                                                                   # This will validate your word selection. It will only take alphabetical characters.
    while True:                                                                                     # This loop will continue forever, so we only break if function returns
        for c in y:                                                                                 # This loop evaluates every letter in the string that is passed to it
            if y.isalpha():                                                                         # This checks every letter of the loop to be sure it is alphabetical
                return(y)                                                                           # This returns the word
            else:                                                                                   # If the word includes more than alphabetical characters, ask for another word
                y = input('Please select a word that doesnt use special characters or numbers.')
                

def vowelMode(z):                                                                                   # This will count vowels in your word
    vowel = ['a','e','i','o','u','y','A','E','I','O','U','Y']                                       # This creates a list containing all of the vowels in the alphabet
    vowelNum = 0                                                                                    # This variable is where we hold the number of vowels
    for ch in z:                                                                                    # This loop checks every character in the word passed into the function
        if ch in vowel:                                                                             # If the character being analyzed is in the list above
            vowelNum += 1                                                                           # Increase variable vowelNum by 1
            print(ch, 'is a vowel, making', vowelNum, 'in this word.')                              # Let user know what the character was a vowel and read the vowel count to them
        else:                                                                                       # If character was not a vowel
            print(ch, 'is not a vowel')                                                             # Let user know letter was not a vowel
    return(vowelNum)                                                                                # return the number of vowels in the word

def consonantMode(z):                                                                               # This will count consonants in your word
    consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z',\
                 'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']   # This is a list of consonants
    consonantNum = 0                                                                                # This variable is where we hold the number of consonants
    for ch in z:                                                                                    # This loop checks every character in the word passed into the function
        if ch in consonant:                                                                         # If the character being analyzed is in the list above
            consonantNum += 1                                                                       # Increase variable consonantNum by 1
            print(ch, 'is a consonant, making', consonantNum, 'in this word.')                      # let user know what the character was a consonant and read the consonant count to them
        else:                                                                                       # if character was not a consonant
            print(ch, 'is not a consonant')                                                         # let user know the letter was not a consonant
    return(consonantNum)                                                                            # return the number of consonants in the word
                                                                                                    
def quitMode(x,y,z,a): # It is important to note: x=numVowels, y=numConsonants, z=numWords, a=mode  # This will be if user ellects to quit the game, by not selecting a word or chosing quit as the option
    if z == 0:                                                                                      # If number of words = 0
        print('Thanks for playing!')                                                                # thank user for playing
        input('Press ENTER to close')                                                               # ask user to press enter to close
        return()                                                                                    # return nothing
    elif z != 0:                                                                                    # if number of words doesn't = 0
        if a == 'vowels':                                                                           # if mode = vowels
            print('We have found', x, 'vowels in the', z,'words you selected to evaluate')          # inform user of how many vowels we found and how many words we went through
            print('Average Vowels Per Word:', '{:,.2f}'.format(x/z))                                # inform user of the average number of vowels used per word
        elif a == 'consonants':                                                                     # if mode = consonants
            print('We have found', y, 'consonants in the', z,'words you selected to evaluate')      # inform user of how many consonants we found and how many words we went through
            print('Average Consonants Per Word:', '{:,.2f}'.format(y/z))                            # inform user of how many consonants appeared as an average in each word
    userSure = input('Are you sure you want to quit the program?')                                  # ask user if they are sure that they want to quit
    if userSure.casefold().startswith('y'):                                                         # if user is sure they want to quit
        print('Thanks for playing!')                                                                # thank them for playing
        input('Press ENTER to close')                                                               # and ask them to press enter to close the program
        return('no')                                                                                # return the string no to main function, so it closes the program
    else:                                                                                           # if user is not sure they want to leave the program
        return('yes')                                                                               # return the string yes to main function to restart the main loop

def main():                                                                                         # This is the main function
    numVowels = 0                                                                                   # numVowels is a variable and initally assigned 0
    numConsonants = 0                                                                               # numConsonants is a variable and initally assigned 0
    totalVowels = 0                                                                                 # PLACEHOLDER FOR POSSIBLE CHANGES LATER
    totalConsonants = 0                                                                             # PLACEHOLDER FOR POSSIBLE CHANGES LATER
    numWords = 0                                                                                    # numWords is a varriable and initially assigned 0
    anotherWord = 'y'                                                                               # anotherWord is a yes/no variable and initially assigned yes
    mode = input('Please select vowels, consonants, or quit: ')                                     # This variable lets the user choose the mode we will be playing in
    mode = validMode(mode)                                                                          # This calls the validMode function and passes mode as a variable
    while anotherWord.casefold().startswith('y'):                                                   # This loop will continue as long as the user wants to keep giving words
        if mode == 'vowels':                                                                        # If mode is vowels
            word = input('Please select a word: ')                                                  # get a word from the user
            word = validWord(word)                                                                  # pass the word into the validWord function
            numVowels += vowelMode(word)                                                            # numVowels goes up by the return from vowelMode
            numWords += 1                                                                           # numWords variable goes up by 1
            anotherWord = input('Would you like to select another word?')                           # ask user if they have another word they want to use and restart the loop
        elif mode == 'consonants':                                                                  # If mode is consonants
            word = input('Please select a word: ')                                                  # get a word from the user
            word = validWord(word)                                                                  # pass the word into the validWord function
            numConsonants += consonantMode(word)                                                    # numVowels goes up by the return from consonantMode
            numWords += 1                                                                           # numWords variable goes up by 1
            anotherWord = input('Would you like to select another word?')                           # ask user if they have another word they want to use and restart the loop
        elif mode == 'quit':                                                                        # If mode is quit
            quitMode(numVowels, numConsonants, numWords, mode)                                      # enter the quit function sending the variables numVowels, numConsonants and numWords
            break                                                                                   # break the loop
        if anotherWord.casefold().startswith('n'):                                                  # If the loop selected wasn't quit mode
            anotherWord = quitMode(numVowels, numConsonants, numWords, mode)                        # Jump into quit mode when user selects they do not want to pick another word,
                                                                                                    # If quit mode returns that the user is not ready to quit we will restart the main loop
                
main()                                                                                              # call the main function to start the program
