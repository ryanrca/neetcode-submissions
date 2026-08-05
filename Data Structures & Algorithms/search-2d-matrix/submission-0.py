class Solution:

    # returns the row the target lives in
    # index of item (greater or equal to target), that is less than next item
    def row_bin_search(self, int_list, target):
        low = 0
        high = len(int_list)-1

        while low <= high:
            mid = (low+high)//2

            if int_list[mid] == target:
                return mid
            if target < int_list[mid]:
                high = mid-1
            if target > int_list[mid]:
                low = mid+1
            
        if target < int_list[mid]:
            return mid-1
        return mid 

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = []
        for i in range(len(matrix)):
            first_col.append(matrix[i][0])

        row = self.row_bin_search(first_col, target)

        target_row = matrix[row]

        low = 0
        high = len(target_row)-1

        while low <= high:
            mid = (low+high)//2

            if target == target_row[mid]:
                return True
            if target < target_row[mid]:
                high = mid-1
            if target > target_row[mid]:
                low = mid+1

        return False
