class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for factor, price in items)
        max_factor = max(factor for factor, price in items)
        freq = [0] * (max_factor + 1)
        for factor, price in items:
            freq[factor] += 1
        gain = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] == 0:
                continue
            count = 0
            for multiple in range(f, max_factor + 1, f):
                count += freq[multiple]
            gain[f] = count - 1
        items.sort(key=lambda x: x[1])
        ans = 0
        for factor, price in items:
            if price >= 2 * min_price:
                break
            if gain[factor] == 0:
                continue
            take = min(gain[factor], budget // price)
            ans += 2 * take
            budget -= take * price
            if take < gain[factor]:
                break
        ans += budget // min_price
        return ans
