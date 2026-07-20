class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 if len(nums1) <= len(nums2) else nums2
        B = nums1 if len(nums1) > len(nums2) else nums2
        half = (len(nums1) + len(nums2)) // 2 if (len(nums1) + len(nums2)) % 2 == 0 else (len(nums1) + len(nums2)) // 2 + 1
        res = 0.0

        lo_A, hi_A = 1, len(A)
        max_left, min_right = 0, 0

        while lo_A <= hi_A:
            mid_A = lo_A + (hi_A - lo_A) // 2
            mid_B = half - mid_A

            max_left = max(A[mid_A - 1], B[mid_B - 1]) if mid_A != 0 else B[mid_B - 1]
            min_right = min(A[mid_A], B[mid_B]) if mid_A != len(A) else B[mid_B]

            print(mid_B,)

            print(mid_A, max_left, min_right)
            if max_left > min_right:
                lo_A = mid_A + 1
            else:
                break
        
        mid_A = lo_A + (hi_A - lo_A) // 2
        mid_B = half - mid_A
        print(mid_A, mid_B)
        if (len(nums1) + len(nums2)) % 2 == 1:
            max_right = max(A[mid_A], B[mid_B]) if mid_A != len(A) else B[mid_B]
            res = min(max_left, min_right)
        else:
            res = (max_left + min_right) / 2


        return res