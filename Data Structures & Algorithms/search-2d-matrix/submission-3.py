class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo_r, hi_r = 0, len(matrix) - 1

        while lo_r <= hi_r:
            mid_r = lo_r + (hi_r - lo_r) // 2

            first_r, last_r = matrix[mid_r][0], matrix[mid_r][-1]

            if first_r <= target and target <= last_r:
                lo, hi = 0, len(matrix[0]) - 1
                while lo <= hi:
                    mid = lo + (hi - lo) // 2

                    if matrix[mid_r][mid] == target:
                        return True
                    elif matrix[mid_r][mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1

                return False
            elif first_r > target:
                hi_r = mid_r - 1
            else:
                lo_r = mid_r + 1
            
        return False
        