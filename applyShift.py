import string


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """

    def buildCoder(shift):
        """
        Shift: integer

        Takes shift and returns dictinary
        in wich key is original letter
        and value is shifted letter
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

        text: string
        coder: dict with mappings of characters to shifted characters
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

    return applyCoder(text, buildCoder(shift))

