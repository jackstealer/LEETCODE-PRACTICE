
import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        lower = []
        upper = []
        side = [0] * n
        deleted = set()

        ls = us = 0
        lsum = usum = 0

        def prune(heap):
            while heap and heap[0][1] in deleted:
                _, idx = heapq.heappop(heap)
                deleted.remove(idx)

        def balance():
            nonlocal ls, us, lsum, usum

            prune(lower)
            prune(upper)

            target = (ls + us + 1) // 2

            while ls > target:
                val, idx = heapq.heappop(lower)
                val = -val

                ls -= 1
                lsum -= val
                heapq.heappush(upper, (val, idx))
                side[idx] = 1
                us += 1
                usum += val
                prune(lower)

            while ls < target:
                prune(upper)
                val, idx = heapq.heappop(upper)

                us -= 1
                usum -= val
                heapq.heappush(lower, (-val, idx))
                side[idx] = 0
                ls += 1
                lsum += val
                prune(upper)

        def add(i):
            nonlocal ls, us, lsum, usum

            prune(lower)
            val = nums[i]

            if not lower or val <= -lower[0][0]:
                heapq.heappush(lower, (-val, i))
                side[i] = 0
                ls += 1
                lsum += val
            else:
                heapq.heappush(upper, (val, i))
                side[i] = 1
                us += 1
                usum += val

            balance()

        def remove(i):
            nonlocal ls, us, lsum, usum

            val = nums[i]

            if side[i] == 0:
                ls -= 1
                lsum -= val
            else:
                us -= 1
                usum -= val

            deleted.add(i)
            balance()

        # Calculate cost of every window of size x
        costs = []

        for i in range(x):
            add(i)

        for start in range(n - x + 1):
            if start > 0:
                remove(start - 1)
                add(start + x - 1)

            median = -lower[0][0]

            cost = (
                median * ls - lsum
                + usum - median * us
            )

            costs.append(cost)

        # Dynamic Programming
        INF = 10**30
        prev = [0] * (n + 1)

        for count in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Select a window of size x
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
