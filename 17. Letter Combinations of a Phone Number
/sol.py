from typing import List

class Solution:
    phone_map = { 
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def __init__(self):
        self.result = []

    def create_word(self, s: str, c: str):
        if len(c) == len(s):
            self.result.append(c)
            return

        for letter in self.phone_map[s[len(c)]]:
            self.create_word(s, c + letter)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.result = []  
        self.create_word(digits, '')
        return self.result
