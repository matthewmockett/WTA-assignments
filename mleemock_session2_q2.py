# Solution by mleemock@uwo.ca
# Date June 17, 2024
class Solution:
    def sortWave(self, nums1:list[int]):

        # Initialize a new list to store the final result in
        result = []

        # Initalize a left and right pointer that will be used to switch 
        l = 0
        r = 1

        # sort the list into ascending order
        nums1.sort()

        # use a while loop it iterate through the length of the list.
        while r < len(nums1):

            # if left is greater than right, don't swithch up the order and just append to result
            if nums1[l] > nums1[r]:
                result.append(nums1[l])
                result.append(nums1[r])
            
            # if right is greater than the left, switch up the order and append the right pointer and then the left pointer.
            else:
                result.append(nums1[r])
                result.append(nums1[l])

            # Increment by 2 so we don't go over the same number twice and get a new window between the left and right pointers.
            l+=2
            r+=2 
        
        # Once the while loop has been exited, if the length of the array was an odd number, 
        # there will still be a number leftover to be sorted which is why the left pointer is appended to the ans list.
        # and since we sorted the array at the start, it will always be the greatest number at the end of the array, thus can be just appended.
        if len(nums1) % 2 != 0:
            result.append(nums1[l])
        return result
    
# output Testcase 1: [1, 0, 15, 7, 99, 16, 123, 108, 532, 503, 1023]
# output Testcase 2: [15, 4, 43, 19, 56, 52, 999, 99, 1000]


  
def main():
    solution = Solution()
    
    # input 1)
    nums1 = [7, 16, 503, 1023, 532, 123, 99, 108, 15, 0, 1]
    # input 2)
    #nums2 = [4, 99, 999, 1000, 43, 56, 19, 15, 52]
    result = solution.sortWave(nums1)
    print(result)

if __name__ == "__main__":
    main()

# Explanation:
'''
For this algorithm, I used a 2 pointer approach to iterate through list. With the two pointers, I was able to compare the left pointer
to the right pointer and thus check which value is greater and then place them into the new array accordingly. Additionally, I used the sort
function at the beginning to sort the input into non-descending order to help later when iterating through the list. If the input contained an
odd amount of elements, I added a special if case to append the last element as the last element in the list will always be the greatest element
thanks to the sort function. The time complexity for this algorithm is O(nlogn) becuase of the sort function and then you need to iterate through the list
which is O(n) of time, but the sorting time dominates this. The space complexity is O(n) as it requires n additional space in the new list that
stores the wave list.
'''