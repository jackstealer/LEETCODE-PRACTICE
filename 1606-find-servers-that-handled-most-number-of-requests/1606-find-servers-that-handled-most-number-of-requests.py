import heapq
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        size = 1
        while size < k:
            size *= 2
        tree = [0] * (2 * size)
        for i in range(k):
            tree[size + i] = 1
        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]
        def update(pos, value):
            p = size + pos
            tree[p] = value
            p //= 2
            while p:
                tree[p] = tree[2 * p] + tree[2 * p + 1]
                p //= 2
        def find_first(node, left, right, start):
            if right < start or tree[node] == 0:
                return -1
            if left == right:
                return left
            mid = (left + right) // 2
            ans = find_first(node * 2, left, mid, start)
            if ans != -1:
                return ans
            return find_first(node * 2 + 1, mid + 1, right, start)
        busy = []
        count = [0] * k
        for i in range(len(arrival)):
            t = arrival[i]
            while busy and busy[0][0] <= t:
                end_time, server = heapq.heappop(busy)
                update(server, 1)
            start = i % k
            server = find_first(1, 0, size - 1, start)
            if server == -1:
                server = find_first(1, 0, size - 1, 0)
            if server == -1:
                continue
            update(server, 0)
            heapq.heappush(
                busy,
                (t + load[i], server)
            )
            count[server] += 1
        maximum = max(count)
        return [
            i for i in range(k)
            if count[i] == maximum
        ]