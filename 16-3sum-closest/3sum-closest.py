class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        csum = nums[0]+nums[1]+nums[2]
        for i in range(n):
            j = i+1
            k = n-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if(abs(target-s)<abs(target-csum)):
                    csum = s
                if(target==s):
                    return s
                elif(s<target):
                    j+=1
                else:
                    k-=1
        return csum

                    
        