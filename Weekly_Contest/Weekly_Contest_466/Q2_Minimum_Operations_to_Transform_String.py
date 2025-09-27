class Solution:
    def minOperations(self, s: str) -> int:
        min_c = None
        for i in s:
            if (i == 'a'):
                continue
            if (min_c == None):
                min_c = i
            if (ord(i) < ord(min_c)):
                min_c = i
        return ord('z') - ord(min_c) + 1 if min_c != None else 0