class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*(n+1)
        suffix = [1]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i]*nums[i]
        for i in reversed(range(n)):
            suffix[i] = suffix[i+1]*nums[i]
        
        return [pre[i]*suffix[i+1] for i in range(n)]

        