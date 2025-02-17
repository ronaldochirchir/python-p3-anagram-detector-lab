# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase for case-insensitive comparison

    def match(self, word_list):
        """Return a list of anagrams from the given word list."""
        anagrams = []
        for candidate in word_list:
            if self._is_anagram(candidate):
                anagrams.append(candidate)
        return anagrams

    def _is_anagram(self, candidate):
        """Check if the candidate is an anagram of the initialized word."""
        candidate_lower = candidate.lower()
        # Check if the candidate is not the same as the word and has the same sorted letters
        return candidate_lower != self.word and sorted(candidate_lower) == sorted(self.word)