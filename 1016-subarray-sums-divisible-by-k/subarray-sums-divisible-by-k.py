class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        csum = ans = 0
        for i in range(len(nums)):
            csum+= nums[i]
            cdiv = csum % k
            if(cdiv in freq):
                ans+=freq.get(cdiv)
            freq[cdiv] = freq.get(cdiv,0)+1
        return ans

        