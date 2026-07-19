class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 if len(nums1) <= len(nums2) else nums2
        B = nums1 if len(nums1) > len(nums2) else nums2
        half = (len(nums1) + len(nums2)) // 2
        res = 0.0

        lo_A, hi_A = 0, len(A)
        max_left, min_right = 0, 0

        while lo_A <= hi_A:
            mid_A = lo_A + (hi_A - lo_A) // 2
            mid_B = half - mid_A

            max_left = max(A[mid_A - 1], B[mid_B - 1])
            min_right = min(A[mid_A], B[mid_B]) if mid_A != len(A) else B[mid_B]

            if max_left > min_right:
                lo_A = mid_A + 1
            else:
                break
        
        mid = lo_A + (hi_A - lo_A) // 2
        if (len(nums1) + len(nums2)) % 2 == 1:
            res = float(nums1[mid])
            print("hi")
        else:
            res = (max_left + min_right) / 2


        return res