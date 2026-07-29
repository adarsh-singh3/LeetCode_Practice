class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        pos = n-1
        ans = [0]*(n)
        while(l<=r):
            lsq = nums[l]**2
            rsq = nums[r]**2
            if(lsq>rsq):
                ans[pos] = lsq
                l+=1
            else:
                ans[pos] = rsq
                r-=1
            pos-=1
        return ans

        