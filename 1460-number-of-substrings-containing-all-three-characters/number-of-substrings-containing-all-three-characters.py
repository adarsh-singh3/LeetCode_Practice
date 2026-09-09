class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # cnt = 0
        # n = len(s)
        # #brute force
        # for i in range(n):
        #     freq = {'a':0,'b':0,'c':0}
        #     for j in range(i,n):
        #         freq[s[j]] = freq.get(s[j],0)+1
        #         if(freq.get('a') > 0 and freq.get('b')>0 and freq.get('c')>0):
        #             cnt = cnt+1
        # return cnt

        # #better
        # mx = 0
        # n = len(s)
        # for i in range(n):
        #     freq = {'a':0,'b':0,'c':0}
        #     for j in range(i,n):
        #         freq[s[j]] = freq.get(s[j],0)+1
        #         if(freq.get('a') > 0 and freq.get('b')>0 and freq.get('c')>0):
        #             mx+=(n-j)
        #             break
        # return mx

        #optimal
        l = r = mx = 0
        n = len(s)
        freq = {}
        while(r<n):
            freq[s[r]] = freq.get(s[r],0)+1
            while(len(freq)==3):
                mx+=(n-r)
                freq[s[l]]-=1
                if(freq[s[l]]==0):
                    freq.pop(s[l])
                l+=1
            r+=1
        return mx


        