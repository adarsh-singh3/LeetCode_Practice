class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zcount = 0
        n = len(nums)
        left = 0
        for i in range(n):
            if(nums[i]!=0):
                nums[i],nums[left] = nums[left],nums[i]
                left+=1
        return nums
            
        