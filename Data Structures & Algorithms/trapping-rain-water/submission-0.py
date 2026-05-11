class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxL = 0
        for i in range(len(height)):
            if i == 0:
                maxLeft.append(0)
            else:
                maxL = max(maxL, height[i-1])
                maxLeft.append(maxL)

        maxRight = []
        maxR = 0
        for i in range(len(height)-1,0, -1):
            if i == len(height)-1:
                maxRight.append(0)
            else:
                maxR = max(maxR, height[i+1])
                maxRight.append(maxR)
        maxRight.append(maxR)
        maxRight = maxRight[::-1]      

        minLR = []
        for i in range(len(height)):
            minLR.append(min(maxLeft[i], maxRight[i]))
        
        res = []
        for i in range(len(height)):
            if minLR[i] - height[i] < 0:
                res.append(0)
            else:
                res.append(minLR[i] - height[i])

        return sum(res)