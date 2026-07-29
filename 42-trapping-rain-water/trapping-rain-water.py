class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmx = [0]*(n+1)
        for i in range(n):
            lmx[i+1] = max(lmx[i],height[i])
        
        rmx = [0]*(n+1)
        for i in reversed(range(n)):
            rmx[i] = max(rmx[i+1],height[i])
        total = 0
        for i in range(n):
            total+= min(lmx[i+1],rmx[i])-height[i]
        return total

        