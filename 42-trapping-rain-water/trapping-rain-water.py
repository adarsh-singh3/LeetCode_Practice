class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trap = 0
        l = 0
        r = n-1
        leftmx = 0
        rightmx = 0
        while(l<r):
            if(height[l]<height[r]):
                # l+=1
                leftmx = max(leftmx,height[l])
                trap += leftmx-height[l]
                l+=1
            else:
                # r-=1
                rightmx = max(rightmx,height[r])
                trap+= rightmx-height[r]
                r-=1
        return trap
        