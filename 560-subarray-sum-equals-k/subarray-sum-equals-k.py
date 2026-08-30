class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        n = len(nums)
        csum = 0
        ans = 0
        for i in range(n):
            csum+=nums[i]
            if(csum-k in freq):
                ans+=freq.get(csum-k)
            freq[csum] = freq.get(csum,0)+1
        return ans

        