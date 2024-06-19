# Given a 2D array, print the elements of the array in a clockwise spiral from starting from top left.
class Solution:
    def clockwiseSpiral(self, nums1):
        if not nums1 or not nums1[0]:
            return []
        
        result = []
        top = 0
        bottom = len(nums1) - 1
        left = 0
        right = len(nums1[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(nums1[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(nums1[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(nums1[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(nums1[i][left])
                left += 1

        return result


def main():

    solution = Solution()

    nums1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    ans = solution.clockwiseSpiral(nums1)
    print(ans)  #


if __name__ == "__main__":
    main()