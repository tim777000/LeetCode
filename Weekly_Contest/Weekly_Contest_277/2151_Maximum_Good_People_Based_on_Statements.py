class Solution:
    def generate_good_bad(self, number_of_people: int, people_list: List[bool], possibility_of_good_bad: List[List[bool]]):
        if (number_of_people == 0):
            possibility_of_good_bad.append(people_list)
        else:
            self.generate_good_bad(number_of_people-1, people_list + [True], possibility_of_good_bad)
            self.generate_good_bad(number_of_people-1, people_list + [False], possibility_of_good_bad)
        return

    def check_status(self, possibility: List[bool], statement: List[int]) -> bool:
        for person_index, index in enumerate(statement):
            if (possibility[person_index] == True and statement[person_index] == 0) or (possibility[person_index] == False and statement[person_index] == 1):
                return False
        return True

    def maximumGood(self, statements: List[List[int]]) -> int:
        number_of_people = len(statements)
        possibility_of_good_bad = []
        self.generate_good_bad(number_of_people, [], possibility_of_good_bad)
        answer = 0
        for possibility_index, possibility in enumerate(possibility_of_good_bad):
            flag = True
            for statement_index, statement in enumerate(statements):
                if (possibility[statement_index] != True):
                    continue
                if (self.check_status(possibility, statement) != True):
                    flag = False
                    break
            if (flag == True):
                answer = max(answer, possibility.count(True))

        return answer
