class Solution:
   def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_string = ''.join(char for char in s if char.isalnum())
        if new_string == new_string[::-1]:
            return True  
        else:
             return False
