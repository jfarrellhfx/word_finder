class tests:

    @staticmethod
    def length(word, L):
        if "-" in L:
            Lstrings = L.split("-")
            Lmin, Lmax = int(Lstrings[0]), int(Lstrings[1])

            if len(word) in range(Lmin, Lmax + 1):
                return True
            else:
                return False
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

