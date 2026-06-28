class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Convert both arrays to sets to get unique elements
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Return the intersection of the two sets
        return list(set1 & set2)
