class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        n = len(nums)
        zcount = 0
        mx = 0
        while(r<n):
            if(nums[r]==0):
                zcount+=1
            while(zcount>k):
                if(nums[l]==0):
                    zcount-=1
                l+=1
            mx = max(mx,r-l+1)
            r+=1
        return mx
        