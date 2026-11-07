import heapq
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        busy = []
        ans = []
        time = 0
        for i, duration in enumerate(tasks):
            time = max(time, i)
            while busy and busy[0][0] <= time:
                free, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))
            if not available:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    free, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))
            weight, idx = heapq.heappop(available)
            ans.append(idx)
            heapq.heappush(
                busy,
                (time + duration, weight, idx)
            )
        return ans