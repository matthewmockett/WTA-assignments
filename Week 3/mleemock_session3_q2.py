# By mleemock@uwo.ca
# Date: June 24, 2024

# Question 2) - Binary Search
# Given the positions of houses and heaters on a horizontal line, 
# return the minimum radius required for the heaters to cover all the houses. The warm radius will be the same for all heaters.

def minRadius(houses, heaters):
    houses.sort()
    heaters.sort()

    # Binary search to find the left most heater
    def closestHeater(house):
        left = 0
        right = len(heaters) - 1
        while left < right:
            mid = (left + right) // 2
            if heaters[mid] < house:
                left = mid + 1
            else:
                right = mid
        return left

    maxRadius = 0

    for house in houses:
        # Find the position of the closest heater to the current house
        pos = closestHeater(house)
        # Calculate the distance from the current house to the heater at position 'pos'
        # If pos is within the bounds of the heaters array use heaters[pos] - house
        # Otherwise if pos is out of bounds, set dist1 to infinity
        dist1 = abs(heaters[pos] - house) if pos < len(heaters) else float('inf')
        dist2 = abs(heaters[pos - 1] - house) if pos > 0 else float('inf')

        # Find the minimum distance to a heater (either the one at 'pos' or pos - 1)
        minDistance = min(dist1, dist2)

        maxRadius = max(maxRadius, minDistance)

    return maxRadius

# Test case 1)
houses1 = [99, 8, 7]
heaters1 = [2]
print(minRadius(houses1, heaters1))  # Output: 97

# Test case 2)
houses2 = [5, 2, 9, 4]
heaters2 = [4, 8]
print(minRadius(houses2, heaters2))  # Output: 2