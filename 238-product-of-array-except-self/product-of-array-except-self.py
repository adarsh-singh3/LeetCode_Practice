class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = []
        n = len(nums)

        # for i in range(n):
        #     csum = 1
        #     for j in range(n):
        #         if i==j:
        #             continue
        #         csum = csum*nums[j]
        #     ans.append(csum)
        # return ans
        
        # pre = [1]*(n+1)
        # for i in range(n):
        #     pre[i+1] = pre[i]*nums[i]

        # suff = [1]*(n+1)
        # for i in reversed(range(n)):
        #     suff[i] = suff[i+1]*nums[i]
        
        # ans = []

        # for i in range(n):
        #     ans.append(pre[i]*suff[i+1])
        # return ans

        ans = [1]*(n)
        for  i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]
        suff = 1
        for i in reversed(range(n)):
            ans[i]*=suff
            suff*=nums[i]
        return ans


        

        