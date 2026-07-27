class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        mx = 0
        while(left<right):
            width = right-left
            h = min(height[right],height[left])
            carea = width * h
            mx = max(carea,mx)
            if(height[left]<height[right]):
                left+=1
            elif(height[right]<height[left]):
                right-=1
            else:
                right-=1
                left+=1
        return mx
        