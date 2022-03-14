class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_list = [0]*101
        even_list = [0]*101
        length_of_nums_list = len(nums)
        for index, num in enumerate(nums):
            if (index%2 == 0):
                even_list[num] += 1
            else:
                odd_list[num] += 1

        even_sort = []
        for i in range(101):
            if (even_list[i] != 0):
                even_sort.extend([i]*even_list[i])

        odd_sort = []
        for i in range(100, 0, -1):
            if (odd_list[i] != 0):
                odd_sort.extend([i]*odd_list[i])

        counter = 0
        answer = []
        length_of_even = len(even_sort)
        even_counter = 0
        length_of_odd = len(odd_sort)
        odd_counter = 0
        while(counter < length_of_nums_list):
            if (counter%2 == 0 and even_counter < length_of_even):
                answer.append(even_sort[even_counter])
                even_counter += 1
            elif (counter%2 == 1 and odd_counter < length_of_odd):
                answer.append(odd_sort[odd_counter])
                odd_counter += 1
            counter += 1

        return answer