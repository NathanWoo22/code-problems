class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        pq = []
        countsByTask = defaultdict(int)

        for task in tasks:
            countsByTask[task] += 1
        
        pq = [[count, task] for task, count in countsByTask.items()]
        heapq.heapify_max(pq)
        counter = 0
        waitingTasks = deque()
        while pq or waitingTasks: 
            counter += 1
            if pq: 
                curTask = heapq.heappop_max(pq)
                curTask[0] -= 1
                if curTask[0] > 0:
                    curTask.append(counter + n)
                    waitingTasks.append(curTask)

            else: 
                counter = waitingTasks[0][2]

            if waitingTasks and waitingTasks[0][2] == counter:
                task = waitingTasks.popleft()
                heapq.heappush_max(pq, task[0:2])
            
                    
        return counter
        
        
