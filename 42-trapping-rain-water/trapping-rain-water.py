class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmx = 0
        rmx = 0
        trap = 0
        l = 0
        r = n-1
        while(l<r):
            if(height[l]<height[r]):
                lmx = max(lmx,height[l])
                trap +=lmx-height[l]
                l+=1
            else:
                rmx = max(rmx,height[r])
                trap += rmx-height[r]
                r-=1
        return trap


        