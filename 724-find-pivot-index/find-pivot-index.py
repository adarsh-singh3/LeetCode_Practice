class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total= sum(nums)
        csum = 0
        rsum = 0
        for i in range(len(nums)):
            rsum = total-csum-nums[i]
            if(csum==rsum):
                return i
            csum+=nums[i]
        else:
            return -1

        