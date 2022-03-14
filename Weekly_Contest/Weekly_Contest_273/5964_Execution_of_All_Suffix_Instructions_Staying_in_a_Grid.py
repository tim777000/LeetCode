class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        answer = []
        length_of_instruction = len(s)
        current_pos = None

        for index, instruction in enumerate(s):
            instruction_count = 0
            if (self.check_instruction(n, startPos, instruction)):
                instruction_count += 1
                current_pos = self.calculate_pos(startPos, instruction)
            elif (instruction_count == 0):
                answer.append(instruction_count)
                continue
            for temp_index in range(index+1, length_of_instruction):
                if ((current_pos != None) and self.check_instruction(n, current_pos, s[temp_index])):
                    instruction_count += 1
                    current_pos = self.calculate_pos(current_pos, s[temp_index])
                else:
                    break
            answer.append(instruction_count)
        return answer

    def check_instruction(self, n: int, current_pos: List[int], instruction: str) -> bool:
        if (instruction == "L" and current_pos[1]-1 < 0):
            return False
        elif (instruction == "R" and current_pos[1]+1 >= n):
            return False
        elif (instruction == "D" and current_pos[0]+1 >= n):
            return False
        elif (instruction == "U" and current_pos[0]-1 < 0):
            return False
        return True

    def calculate_pos(self, current_pos: List[int], instruction: str) -> List[int]:
        if (instruction == "L"):
            return [current_pos[0], current_pos[1]-1]
        elif (instruction == "R"):
            return [current_pos[0], current_pos[1]+1]
        elif (instruction == "D"):
            return [current_pos[0]+1, current_pos[1]]
        elif (instruction == "U"):
            return [current_pos[0]-1, current_pos[1]]



