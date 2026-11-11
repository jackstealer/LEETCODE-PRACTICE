class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        def f(k):
            return k * costBoth + max(0, need1 - k) * cost1 + max(0, need2 - k) * cost2
        return min(f(0), f(min(need1, need2)), f(max(need1, need2)))