# mleemock@uwo.ca
# June 24, 2024

# Q3 - sliding window
from collections import defaultdict


def numberOfSubarrays(nums, k):

    prefixSums = defaultdict(int)
    currSum = 0
    count = 0

    for num in nums:
        currSum += num
        
        # Check if the current cumulative sum is equal to k
        if currSum == k:
            count += 1
        
        # Check if there is a prefix sum that matches the condition
        if (currSum - k) in prefixSums:
            count += prefixSums[currSum - k]
        
        # Update the hashmap
        prefixSums[currSum] += 1

    return count

# Example 1
nums1 = [2, 0, 1, 1, 7, 9]
k1 = 8
print(numberOfSubarrays(nums1, k1))  # Output: 1

# Example 2
nums2 = [1, 0, 1, 0, 1]
k2 = 1
print(numberOfSubarrays(nums2, k2))  # Output: 8
