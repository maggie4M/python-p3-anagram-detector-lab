# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        target_sorted = sorted(self.word)
        return [word for word in word_list if sorted(word) == target_sorted]