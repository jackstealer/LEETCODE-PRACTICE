class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sa = list(range(n))
        rank = nums[:]
        k = 1
        while k < n:
            sa.sort(
                key=lambda i: (
                    rank[i],
                    rank[i + k] if i + k < n else -1
                )
            )
            new_rank = [0] * n
            for j in range(1, n):
                prev = sa[j - 1]
                curr = sa[j]
                prev_key = (
                    rank[prev],
                    rank[prev + k] if prev + k < n else -1
                )
                curr_key = (
                    rank[curr],
                    rank[curr + k] if curr + k < n else -1
                )
                new_rank[curr] = (
                    new_rank[prev] + (prev_key != curr_key)
                )
            rank = new_rank
            if rank[sa[-1]] == n - 1:
                break
            k *= 2
        pos = [0] * n
        for i in range(n):
            pos[sa[i]] = i
        lcp = [0] * n
        h = 0
        for i in range(n):
            r = pos[i]
            if r == 0:
                h = 0
                continue
            j = sa[r - 1]
            while (
                i + h < n
                and j + h < n
                and nums[i + h] == nums[j + h]
            ):
                h += 1
            lcp[r] = h
            if h > 0:
                h -= 1
        ans = n
        for r in range(n):
            left = lcp[r]
            right = 0
            if r + 1 < n:
                right = lcp[r + 1]
            max_lcp = max(left, right)
            required = max_lcp + 1
            start = sa[r]
            if required <= n - start:
                ans = min(ans, required)
        return ans
