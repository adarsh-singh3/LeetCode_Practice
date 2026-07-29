class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i]^arr[i]
        ans = []
        for i in queries:
            l = i[0]
            r = i[1]
            ans.append(pre[r+1]^pre[l])
        return ans

        