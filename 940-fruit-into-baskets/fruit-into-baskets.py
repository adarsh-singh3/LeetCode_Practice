class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        l = r = mx = 0
        n = len(fruits)

        while(r<n):
            if(fruits[r] not in freq):
                freq[fruits[r]] = 1
            else:
                freq[fruits[r]]+=1
            if(len(freq)>2):
                while(len(freq)>2):
                    freq[fruits[l]]-=1
                    if(freq[fruits[l]]==0):
                        freq.pop(fruits[l])
                    l+=1
            mx = max(mx,r-l+1)
            r+=1
        return mx
        