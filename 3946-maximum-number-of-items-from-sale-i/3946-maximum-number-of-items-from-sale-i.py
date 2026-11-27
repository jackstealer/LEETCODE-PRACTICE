
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Find the cheapest item
        min_price = min(price for factor, price in items)

        # 0/1 Knapsack DP
        # dp[b] = maximum benefit using exactly b money
        dp = [float('-inf')] * (budget + 1)
        dp[0] = 0

        # Process each item type
        for factor, price in items:

            # Calculate the first-purchase benefit
            cnt = 0

            for other_factor, other_price in items:
                if other_factor % factor == 0:
                    cnt += 1

            # 0/1 Knapsack: traverse backwards
            for b in range(budget, price - 1, -1):

                if dp[b - price] != float('-inf'):

                    dp[b] = max(
                        dp[b],
                        dp[b - price] + cnt
                    )

        # Phase 2: Spend remaining budget on cheapest item
        ans = 0

        for spent in range(budget + 1):

            if dp[spent] != float('-inf'):

                remaining = budget - spent

                extra_items = remaining // min_price

                total = dp[spent] + extra_items

                ans = max(ans, total)

        return ans
