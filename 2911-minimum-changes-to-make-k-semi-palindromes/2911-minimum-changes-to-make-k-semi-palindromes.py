class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = float('inf')
                for d in range(1, length):
                    if length % d != 0:
                        continue
                    changes = 0
                    for offset in range(d):
                        left = i + offset
                        right = j - d + 1 + offset
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    best = min(best, changes)
                cost[i][j] = best
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for end in range(2, n + 1):
            for parts in range(1, k + 1):
                for cut in range(end - 1):
                    if dp[cut][parts - 1] == INF:
                        continue
                    current = (
                        dp[cut][parts - 1]
                        + cost[cut][end - 1]
                    )
                    dp[end][parts] = min(
                        dp[end][parts],
                        current
                    )
        return dp[n][k]
