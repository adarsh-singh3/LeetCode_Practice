class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lefts = 0 
        rights = 0
        n = len(nums)
        for i in range(n):
            rights = total-lefts-nums[i]
            if(rights==lefts):
                return i
            lefts+=nums[i]
        return -1
        