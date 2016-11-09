import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    for letter in lettersGuessed:
        if letter in secretWord:
            secretWord = secretWord.replace(letter, '')
        if secretWord == '':
            return True
    return False




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessingWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessingWord += letter
        else:
            guessingWord += '_ '
    return guessingWord




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, '')
    return alphabet


def hangman(secretWord):
    line = '------------'
    gueses = 8
    lettersGuessed = ''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'

    while 1:
        print line
        print 'You have ' + str(gueses) + ' guesses left.'
        print 'Aviable letters: ' + getAvailableLetters(lettersGuessed)
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed and letter in secretWord:
            print 'Oops, you have already guest that letter'
            letter = ''
        elif letter in lettersGuessed and letter not in secretWord:
            print 'Oops, you have already tried that letter'
            letter = ''
        lettersGuessed += letter
        if letter in secretWord:
            print 'Good guess! :' + getGuessedWord(secretWord, lettersGuessed)
        else:
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
            gueses -= 1
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
            break
        if gueses == 0:
            print 'Sorry, you ran out of guesses. The word was ' + secretWord
            break
    return

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
