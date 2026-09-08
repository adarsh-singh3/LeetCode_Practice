class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        csum = 0
        n = len(cardPoints)
        for i in range(k):
            csum+=cardPoints[i]
        l = k-1
        r = n-1
        mx = csum
        rsum = 0
        for i in range(k):
            csum-=cardPoints[l]
            rsum+=cardPoints[r]
            t = csum+rsum
            mx = max(t,mx)
            l-=1
            r-=1
        return mx
