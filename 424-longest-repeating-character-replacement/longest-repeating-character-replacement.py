class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #brute force
        # n = len(s)
        # ans = 0
        # for i in range(n):
        #     freq = {}
        #     mx = 0
        #     for j in range(i,n):
        #         freq[s[j]] = freq.get(s[j],0)+1
        #         mx = max(mx,freq[s[i]])
        #         change = (j-i+1)-mx
        #         if(change<=k):
        #             ans = max(j-i+1,ans)
        #         else:
        #             break
        # return ans

        #better
        # n = len(s)
        # l = r = mx = ans = 0
        # freq = {}
        # while(r<n):
        #     freq[s[r]] = freq.get(s[r],0)+1
        #     mx = max(mx,freq[s[r]])
        #     change = (r-l+1)-mx
        #     while(change>k):
        #         freq[s[l]]-=1
        #         if(freq[s[l]]==0):
        #             freq.pop(s[l])
        #         mx = 0
        #         for i in freq:
        #             mx = max(mx,freq.get(i))
        #         l+=1
        #         change = (r-l+1)-mx
        #     ans = max(ans,r-l+1)
        #     r+=1
        # return ans

        #optimal
        n = len(s)
        l = r = mx = ans = 0
        freq = {}
        while(r<n):
            freq[s[r]] = freq.get(s[r],0)+1
            mx = max(mx,freq[s[r]])
            change = (r-l+1)-mx
            if(change>k):
                freq[s[l]]-=1
                if(freq[s[l]]==0):
                    freq.pop(s[l])
                l+=1
                change = (r-l+1)-mx
            ans = max(ans,r-l+1)
            r+=1
        return ans

