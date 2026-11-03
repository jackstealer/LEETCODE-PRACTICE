class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        return len(nums) * maximum - sum(nums)
