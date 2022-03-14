class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance_of_house = [ -1 for house in colors ]
        number_of_house = len(colors)
        for house_index in range(0, number_of_house):
            for compare_house_index in range(0, number_of_house):
                if (colors[house_index] == colors[compare_house_index]):
                    continue
                distance = compare_house_index - house_index
                if (distance > max_distance_of_house[house_index]):
                    max_distance_of_house[house_index] = distance
        return mac(max_distance_of_house)
