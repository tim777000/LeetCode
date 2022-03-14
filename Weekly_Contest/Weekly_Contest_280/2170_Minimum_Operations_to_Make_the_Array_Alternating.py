class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd_dict = {}
        even_dict = {}
        for index, num in enumerate(nums):
            if (index%2 == 0):
                if (num in even_dict.keys()):
                    even_dict[num] += 1
                else:
                    even_dict[num] = 1
            else:
                if (num in odd_dict.keys()):
                    odd_dict[num] += 1
                else:
                    odd_dict[num] = 1
        length_of_nums = len(nums)
        answer = inf
        max_even = max(even_dict, key = even_dict.get)
        max_even_value = even_dict[max_even]
        max_odd = max(odd_dict, key = odd_dict.get) if odd_dict else None
        max_odd_value = odd_dict[max_odd] if odd_dict else 0
        del(even_dict[max_even])
        if max_odd != None:
            del(odd_dict[max_odd])
        sec_even = max(even_dict, key = even_dict.get) if even_dict else None
        sec_even_value = even_dict[sec_even] if even_dict else 0
        sec_odd = max(odd_dict, key = odd_dict.get) if odd_dict else None
        sec_odd_value = odd_dict[sec_odd] if odd_dict else 0

        if (max_even == max_odd):
            if (max_even_value + sec_odd_value) >= (sec_even_value + max_odd_value):
                answer = length_of_nums - max_even_value - sec_odd_value
            else:
                answer = length_of_nums - sec_even_value - max_odd_value
        else:
            answer = length_of_nums - max_even_value - max_odd_value

        return answer