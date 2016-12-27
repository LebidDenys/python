import string
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
