class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank_row_lasers = [row.count("1") for row in bank]
        answer = 0
        length_of_bank_row_lasers = len(bank_row_lasers)
        for index, bank_row_laser in enumerate(bank_row_lasers):
            if (index == 0):
                pre_bank_row_laser = bank_row_laser
            elif (bank_row_laser == 0):
                continue
            else:
                answer += pre_bank_row_laser*bank_row_laser
                pre_bank_row_laser = bank_row_laser

        return answer
