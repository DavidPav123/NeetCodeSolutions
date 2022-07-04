class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = dict()
        t_letters = dict()

        anagram = True

        for i in str(s):
            if i not in s_letters.keys():
                s_letters[i] = 1
            else:
                s_letters[i] = int(s_letters[i]) + 1

        for char in str(t):
            if char not in t_letters.keys():
                t_letters[char] = 1
            else:
                t_letters[char] = int(t_letters[char]) + 1

        if s_letters.keys() == t_letters.keys():
            for keys in s_letters:
                if s_letters[keys] != t_letters[keys]:
                    anagram = False
                    break
        else:
           anagram = False

        return anagram

        

        