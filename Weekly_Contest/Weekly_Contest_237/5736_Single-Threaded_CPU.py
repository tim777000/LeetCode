class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasksLength = len(tasks)
        tasksIndex = [[i]+tasks[i] for i in range(0, tasksLength)]
        sortedTasksIndex = sorted(tasksIndex, key = lambda x: x[1])
        availableTasks = []
        processTasks = None
        iterator = 0
        timer = 0
        answer = []
        while len(answer) < tasksLength :
            if iterator < tasksLength:
                while iterator < tasksLength and sortedTasksIndex[iterator][1] <= timer:
                    heapq.heappush(availableTasks, [sortedTasksIndex[iterator][2], sortedTasksIndex[iterator][0]])
                    iterator += 1
            if processTasks == None and availableTasks == []:
                timer = sortedTasksIndex[iterator][1]
                continue
            if processTasks == None and availableTasks != []:
                temp = heapq.heappop(availableTasks)
                processTasks = temp
            if processTasks != None:
                timer += processTasks[0]
                answer.append(processTasks[1])
                processTasks = None
        return answer