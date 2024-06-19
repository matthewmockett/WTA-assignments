# Given a 2D array, print the elements of the array in a clockwise spiral from starting from top left.
class Solution:
    def clockwiseSpiral(self, nums1):

        # if the array/matrix is null or empty, return an empty list.
        if not nums1 or not nums1[0]:
            return []
        
        # Initialize a new results list to append the new format to.
        result = []
        
        # Initialize pointers
        top = 0 # top boundary of the matrix
        bottom = len(nums1) # number of rows
        left = 0 # left boundary of the matrix
        right = len(nums1[0]) # the length of the matrix + 1

        # Ensure we only traverse within the matrix
        while top < bottom and left < right:

            # Going to go from left to right (right is out of bounds but range function sorts that out - non-inclusive)
            for i in range(left, right):
                result.append(nums1[top][i])
            # shifts the top down by one
            top += 1

            # get every i in the right most column
            for i in range(top, bottom):
                result.append(nums1[i][right -1])
            # shifts the right to the left
            right -= 1

            if not (left < right and top < bottom):
                break

            # right to left in reverse order
            for i in range(right - 1, left - 1, -1):
                result.append(nums1[bottom - 1][i])
            bottom -=1

            # get i in the left most column
            for i in range(bottom - 1, top -1, -1):
                result.append(nums1[i][left])
            left +=1

        return result

# output for test case 1)

def main():

    solution = Solution()

    # Test case 1)
    nums1 = [
        [4, 2, 99, 4],
        [5, 6, 7, 68],
        [99, 10, 11, 12],
        [33, 34, 55, 16]
    ]

   # Test case 2)
   # nums1 = [
   #     [3, 4, 5, 1, 34, 3],
   #     [43, 4, 1, 3, 5, 7],
   #     [3, 1, 100, 99, 5, 8]
   # ]


    ans = solution.clockwiseSpiral(nums1)
    print(ans)  


if __name__ == "__main__":
    main()