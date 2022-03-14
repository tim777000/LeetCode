class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length_of_s = len(s)
        for i in range(length_of_s//2):
            s[i], s[length_of_s-1-i] = s[length_of_s-1-i], s[i]
        return