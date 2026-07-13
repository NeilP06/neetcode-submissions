class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Values needed to track intermediary row states, O(1) space
        lo_r, hi_r = 0, len(matrix) - 1

        # Perform binary search on the row's ranges to find the respective
        # row to search in, O(log m) work
        while lo_r <= hi_r:
            # Calculate row midpoint and find row range, O(1) work
            mid_r = lo_r + (hi_r - lo_r) // 2
            first_r, last_r = matrix[mid_r][0], matrix[mid_r][-1]

            # If the value is inside the row, perform binary search on that
            # row
            if first_r <= target and target <= last_r:
                # Values needed to track intermediary column states, O(1) work
                lo, hi = 0, len(matrix[0]) - 1

                # Perform binary search on the row to find the value, O(log n)
                # work (n represent # columns)
                while lo <= hi:
                    # Calculate column midpoint, O(1) work
                    mid = lo + (hi - lo) // 2

                    # Do the binary search casework, O(1) work
                    if matrix[mid_r][mid] == target:
                        return True
                    elif matrix[mid_r][mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1

                # We know that there doesn't exist the value in the matrix if
                # the target isnt contained in the range, so we can return
                # false early
                return False
            # Else if the value isn't inside the row, adjust the boundaries and
            # repeat the search 
            elif first_r > target:
                hi_r = mid_r - 1
            else:
                lo_r = mid_r + 1
            
        return False
        