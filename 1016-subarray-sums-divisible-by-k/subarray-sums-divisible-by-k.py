class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        csum = c = 0
        n = len(nums)
        for i in range(n):
            csum+=nums[i]
            div = csum%k
            if(div in freq):
                c += freq.get(div)
            freq[div] = freq.get(div,0)+1
        return c

        #         freq = {0:1}
        # div = count = 0
        # for i in nums:
        #     div+=i
        #     res = div%k
        #     if(res in freq):
        #         count+=freq.get(res)
        #     freq[res] = freq.get(res,0)+1
        # print(freq)
        # return count
        