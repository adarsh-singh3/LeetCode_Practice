class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        pre = [1]*(n+1)
        suff = [1]*(n+1)

        for i in range(n):
            pre[i+1] = pre[i]*nums[i]
        
        for i in reversed(range(n)):
            suff[i] = suff[i+1]*nums[i]
        return [pre[i]*suff[i+1] for i in range(n)]
        