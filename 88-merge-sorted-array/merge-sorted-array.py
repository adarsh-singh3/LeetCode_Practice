class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        ans = []
        while l < m and r < n:
            if nums1[l] < nums2[r]:
                ans.append(nums1[l]); l += 1
            else:
                ans.append(nums2[r]); r += 1
        while l < m:
            ans.append(nums1[l]); l += 1
        while r < n:
            ans.append(nums2[r]); r += 1
        for i in range(len(nums1)):
            nums1[i] = ans[i]
        return nums1



        