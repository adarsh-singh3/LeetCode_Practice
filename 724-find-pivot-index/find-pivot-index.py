class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_s = right_s = 0 
        total = sum(nums)
        for i in range(len(nums)):
            right_s = total-left_s-nums[i]
            if(right_s==left_s):
                return i
            left_s+=nums[i]
        return -1
        