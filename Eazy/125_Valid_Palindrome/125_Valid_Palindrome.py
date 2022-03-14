class Solution:
    def isPalindrome(self, s: str) -> bool:
        target_string = ''.join(character.lower() for character in s if character.isalnum())
        print(target_string)
        length_of_target_string = len(target_string)
        for i in range(length_of_target_string//2):
            if target_string[i] != target_string[length_of_target_string-1-i]:
                return False
        return True