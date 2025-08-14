class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        result = []
        for candidate in candidates:
            if candidate.lower() != self.word.lower() and sorted(candidate.lower()) == sorted(self.word.lower()):
                result.append(candidate)
        return result
