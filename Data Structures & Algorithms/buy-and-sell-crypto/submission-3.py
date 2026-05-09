class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                val = prices[r] - prices[l]
                prof = max(prof, val)
            r += 1
        return prof