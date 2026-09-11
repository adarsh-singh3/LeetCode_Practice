class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #optimal
        # def sub(nums,goal):
        #     if(goal<0):
        #         return 0
        #     csum = msum = 0
        #     l = 0
        #     n = len(nums)
        #     for i in range(n):
        #         csum+=nums[i]
        #         # msum = goal-csum
        #         while(csum>goal):
        #             csum-=nums[l]
        #             l+=1
        #         msum+=(i-l+1)
        #     return msum
        # return sub(nums,goal)-sub(nums,goal-1)

        #better prefix sum + hashmap
        n = len(nums)
        freq = {0:1}
        ans = 0
        csum = 0
        for i in range(n):
            csum+=nums[i]
            if(csum-goal in freq):
                ans+=freq.get(csum-goal)
            freq[csum] = freq.get(csum,0)+1
        return ans


        