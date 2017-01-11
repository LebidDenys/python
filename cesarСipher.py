import string
import random

class Cesar(object):

    def __init__(text, wordlist_filename):
        self.text = text
        self.wordlist_filename = wordlist_filename

    def loadWords(self.wordlist_filename):
        """
        Returns a list of valid words. Words are strings of lowercase letters.
        """
        print "Loading word list from file..."
        inFile = open(self.wordlist_filename, 'r')
        wordList = inFile.read().split()
        print "  ", len(wordList), "words loaded."
        return wordList

    def isWord(wordList, word):
        """
        Determines if word is a valid word.
        """

        word = word.lower()
        word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
        return word in wordList

    def randomWord(wordList):
        """
        Returns a random word.
        """
        return random.choice(wordList)

    def randomString(wordList, n):
        """
        Returns a string containing n random words from wordList
        """
        return " ".join([randomWord(wordList) for _ in range(n)])

    def randomScrambled(wordList, n):
        """
        Generates a test string by generating an n-word random string
        and encrypting it with a sequence of random shifts.

        wordList: list of words
        n: number of random words to generate and scamble
        returns: a scrambled string of n random words
        """
        s = randomString(wordList, n) + " "
        shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
        return self.applyShifts(s, shifts)[:-1]

    def getStoryString():
        return open("story.txt", "r").read()


    def buildCoder(shift):
        """
        Returns a dict that can apply a Caesar cipher to a letter.
        The cipher is defined by the shift value. Ignores non-letter characters
        like punctuation, numbers and spaces.
        """
        lowAlphabet = string.ascii_lowercase
        highAlphabet = string.ascii_uppercase

        dictinary = {}

        i = 0
        while len(dictinary) != len(highAlphabet):
            if i + shift >= len(highAlphabet):
                dictinary[highAlphabet[i]] = highAlphabet[i + shift - len(highAlphabet)]
            else:
                dictinary[highAlphabet[i]] = highAlphabet[i + shift]
            i += 1

        i = 0
        while len(dictinary) != len(lowAlphabet)*2:
            if i + shift >= len(lowAlphabet):
                dictinary[lowAlphabet[i]] = lowAlphabet[i + shift - len(lowAlphabet)]
            else:
                dictinary[lowAlphabet[i]] = lowAlphabet[i + shift]
            i += 1

        return dictinary

    def applyCoder(text, coder):
        """
        Applies the coder to the text. Returns the encoded text.
        returns: text after mapping coder chars to original text
        """
        newText = ''
        for letter in text:
            if letter not in coder:
                letter = letter
            else:
                letter = coder[letter]
            newText += letter
        return str(newText)

    def applyShift(text, shift):
        """
        Given a text, returns a new text Caesar shifted by the given shift
        offset.
        """
        return self.applyCoder(text, self.buildCoder(shift))

    def findBestShift(wordList):
        """
        Finds a shift key that can decrypt the encoded text.
        """
        bestShift = 0
        i = 0
        previousRealWordsNumber = 0
        shiftedText = ''
        self.text = text.replace(',', '')
        self.text = text.replace('.', '')
        self.text = text.replace('!', '')
        self.text = text.replace('?', '')


        while i < 26:
            realWordsNumber = 0
            shiftedText = self.applyShift(self.text, 26 - i)
            shiftedWords = shiftedText.split()

            for word in shiftedWords:
                if word in wordList:
                    realWordsNumber += 1

            if realWordsNumber > previousRealWordsNumber:
                bestShift = i
                previousRealWordsNumber = realWordsNumber
            i += 1
        return 26 - bestShift
