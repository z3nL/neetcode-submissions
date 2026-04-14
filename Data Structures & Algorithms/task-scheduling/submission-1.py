class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Init time
        time = 0
        # Count frequency of each task
        tc = Counter(tasks)

        # Ready queue -> task with highest frequency remaining first
        ready = []
        for k, v in tc.items():
            heapq.heappush(ready, (-v, k))

        # Wait queue -> task with earliest last completion first 
        waiting = []

        while ready or waiting:
            # Shift pending tasks to ready queue
            while waiting and time - waiting[0][0] > n:
                at, count, label = heapq.heappop(waiting)
                heapq.heappush(ready, (count, label))

            # Complete first available task and add to wait queue if needed
            if ready:
                count, label = heapq.heappop(ready)
                count += 1
                if count < 0:
                    heapq.heappush(waiting, (time, count, label))

            time += 1
        
        return time


        