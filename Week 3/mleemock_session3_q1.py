# By mleemock@uwo.ca
# Date: June 24, 2024

# Question 1) - Sorting
# Given two arrays representing entry and exit times of guests at a party, find the time at which the maximum number of guests are present.
'''
Example:
Input:
entry = [1, 2, 9, 5, 5]
exit = [4, 5, 12, 9, 12]
Output:
5
Explanation:
The maximum number of guests (3) are present at time 5.
'''
class Solution:
    def numOfGuestsPresent(self, nums1, nums2):
        
        # Sort the entry and exit times into ascending order
        nums1.sort()
        nums2.sort()

        # initalize variables to keep track of num of guests and time with most guests
        maxGuests = 0
        timeOfMaxGuests = 0
        totalGuests = 0

        # initalize two pointers for entry and exit times
        entry = 0
        exit = 0

        # While loop to iterate through both lists which terminates when 
        while entry < len(nums1) and exit < len(nums2):
            if nums1[entry] <= nums2[exit]:
                totalGuests +=1
                if totalGuests > maxGuests:
                    maxGuests = totalGuests
                    timeOfMaxGuests = nums1[entry]
                entry +=1
            else:
                totalGuests -=1
                exit +=1
        
        # process any remaing entry times
        while entry < len(nums1):
            totalGuests += 1
            if totalGuests > maxGuests:
                maxGuests = totalGuests
                timeOfMaxGuests = nums1[entry]
            entry += 1

        # Process any remaining exit times
        while exit < len(nums2):
            totalGuests -= 1
            exit += 1

        return timeOfMaxGuests

# output test case 1) 9
# ouput test case 2) 3

# Testing
def main():
    solution = Solution()
    # Test case 1)
    nums1 = [1, 8, 9, 17, 5]
    nums2 = [16, 3, 12, 9, 20]
    '''
    #Test case 2)
    nums1 = [3, 8, 2, 9, 20]
    nums2 = [4, 12, 13, 1, 7]
    '''
    result = solution.numOfGuestsPresent(nums1, nums2)
    print(result)
    

if __name__ == "__main__":
    main()

        

