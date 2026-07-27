class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        n = len(nums)
        csum = c = 0
        for i in nums:
            csum+=i
            if(csum-k in freq):
                c+=freq.get(csum-k)
            freq[csum] = freq.get(csum,0)+1
        return c
            
