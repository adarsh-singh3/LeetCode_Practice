class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        csum = 0
        mx = 0
        for i in gain:
            csum+=i
            mx = max(csum,mx)
        return mx

        