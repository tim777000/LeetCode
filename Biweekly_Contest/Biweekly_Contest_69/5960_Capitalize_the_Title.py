class Solution:
    def capitalizeTitle(self, title: str) -> str:
        word_list = title.split(' ')
        answer_list = []
        for word in word_list:
            temp = word.lower()
            if len(temp) >= 3:
                temp = temp.capitalize()
            answer_list.append(temp)

        return ' '.join(answer_list)

