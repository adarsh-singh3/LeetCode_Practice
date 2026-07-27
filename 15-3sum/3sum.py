class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            j = i+1
            k = n-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if(s==0):
                    ans.add((nums[i],nums[j],nums[k]))
                    k-=1
                    j+=1
                elif(s<0):
                    j+=1
                else:
                    k-=1
        return list(ans)

        