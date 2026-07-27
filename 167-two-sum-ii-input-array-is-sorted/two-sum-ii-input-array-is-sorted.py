class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        csum = 0
        while(left<right):
            csum = numbers[left]+numbers[right]
            if(csum==target):
                return [left+1,right+1]
            elif(csum<target):
                left+=1
            else:
                right-=1
        return -1

        