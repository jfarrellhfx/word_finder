"""
Jack Farrell, 2020

Classes to support a basic "word finder" application
"""

class tests:
    """
    Functions to test if a word satisfies certain conditions.
    """


    @staticmethod
    def length(word, L):
        """
        Test if a word has length L

        :param word: string
        :param L: **string** (yep! string!)
        :return: bool
        """

        # check if we are dealing with a range or just an integer.  If so:
        if "-" in L:

            # split the string into two parts: left of the "-" and right of
            #it
            Lstrings = L.split("-")

            # turn the left and right (max and min) into integers
            Lmin, Lmax = int(Lstrings[0]), int(Lstrings[1])

            # if the length of the word is an integer between Lmin and Lmax
            # (inclusive):
            if len(word) in range(Lmin, Lmax + 1):
                return True
            else:
                return False
        # if not, we are just dealing with an integer.
        else:
            Lint = int(L)
            return len(word) == Lint

    @staticmethod
    def startswith(word, phrase):
        L = len(phrase)
        if len(word) < L:
            return False
        else:
            if word[:L] == phrase:
                return True
            else:
                return False

    @staticmethod
    def endswith(word, phrase):
        L = len(phrase)
        if len(word) < L:
            return False
        else:
            if word[-L:] == phrase:
                return True
            else:
                return False

    @staticmethod
    def contains(word, phrase):
        L = len(phrase)
        if len(word) < L:
            return False
        else:
            if phrase in word:
                return True
            else:
                return False

    @staticmethod
    def one_of_these_letters(word, letters, interval):
        contains = False

        if interval == "":
            for letter in letters:
                if letter in word:
                    contains = True


        elif "-" in interval:
            Lstrings = interval.split("-")
            Lmin, Lmax = int(Lstrings[0]), int(Lstrings[1])

            if Lmax < len(word):
                for letter in letters:
                    if letter in word[Lmin:Lmax]:
                        contains = True

        else:
            if len(word) > int(interval) - 1:
                for letter in letters:
                    if word[int(interval) - 1] == letter:
                        contains = True
        return contains

