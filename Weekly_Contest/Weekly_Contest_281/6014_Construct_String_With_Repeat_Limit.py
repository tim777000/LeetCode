class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        sorted_s = sorted(s, reverse=True)
        sorted_s_dict = {}
        length_of_s = len(s)
        for index, c in enumerate(reversed(sorted_s)):
            if (c not in sorted_s_dict.keys()):
                sorted_s_dict[c] = (length_of_s-1) - index
        dup_counter = 0
        while_counter = 0
        isIllegal = False
        for index, c in enumerate(sorted_s):
            if (index == 0):
                previous_c = c
                dup_counter += 1
                continue
            if (c == previous_c):
                dup_counter += 1
            else:
                dup_counter = 1
            if (dup_counter > repeatLimit):
                if (sorted_s_dict[c] + 1 < length_of_s):
                    sorted_s[index], sorted_s[sorted_s_dict[c] + 1] = sorted_s[sorted_s_dict[c] + 1], sorted_s[index]
                    sorted_s_dict[c] += 1
                else:
                    isIllegal =True
                    break
            previous_c = sorted_s[index]
        index = index if isIllegal else index+1
        return "".join(sorted_s[:index])

