class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        freq = {}
        mx = 0
        while(right<n):
            if(s[right] in freq and freq[s[right]]>=left):
                left = freq[s[right]]+1
            freq[s[right]] = right
            mx = max(mx,right-left+1)
            right+=1
        return mx




        