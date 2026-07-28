class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmx  = [0]*(n+1)
        rmx = [0]*(n+1)
        total = 0
        for i in range(n):
            lmx[i+1] = max(lmx[i],height[i])
        for i in reversed(range(n)):
            rmx[i] = max(rmx[i+1],height[i])
        for i in range(n):
            total+= min(lmx[i+1],rmx[i])-height[i]
        return total

        