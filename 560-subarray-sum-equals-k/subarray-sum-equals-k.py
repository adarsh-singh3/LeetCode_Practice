class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        c = 0
        csum = 0
        n = len(nums)
        for i in range(n):
            csum+=nums[i]
            if(csum-k in freq):
                c+=freq.get(csum-k)
            freq[csum] = freq.get(csum,0)+1
        return c
        
        