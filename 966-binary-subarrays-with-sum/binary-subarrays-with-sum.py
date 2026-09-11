class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def sub(nums,goal):
            if(goal<0):
                return 0
            csum = msum = 0
            l = 0
            n = len(nums)
            for i in range(n):
                csum+=nums[i]
                # msum = goal-csum
                while(csum>goal):
                    csum-=nums[l]
                    l+=1
                msum+=(i-l+1)
            return msum
        return sub(nums,goal)-sub(nums,goal-1)

        