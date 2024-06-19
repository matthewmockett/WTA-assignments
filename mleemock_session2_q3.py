# author: mleemock@uwo.ca
# date: June 19, 2024

class Solution:
    def managerReport(self, dict):

       # initializes an empty dictionary to map managers to their direct employees. 
        managerToEmployees = {}

        # iterates over each key (employee) value (manager) pair
        for employee, manager in dict.items():
            # checks if manager is already a key.
            if manager not in managerToEmployees:
                # if manager is not a key, initializes key with empty list
                managerToEmployees[manager] = []
            if employee != manager:  # Skip ceo reporting to themselves
                managerToEmployees[manager].append(employee)
        
        # initializes empty dictionary which will store the number of employees under each manager
        result = {}
    
        # recursive function to count the number of employees under each manager
        def countEmployees(manager):
            if manager not in managerToEmployees:
                result[manager] = 0
                return 0
            
            if manager in result:
                return result[manager]
            
            count = 0
            for employee in managerToEmployees[manager]:
                count += 1 + countEmployees(employee)
            
            result[manager] = count
            return count
        
        for employee in dict:
            if employee not in result:
                countEmployees(employee)
        
        return result

# output for test case 1) {'B': 0, 'A': 1, 'C': 0, 'D': 1, 'E': 2, 'F': 5}

def main():

    # test case 1:
    #dict =  {
   # "A": "F",
   # "B": "A",
   # "C": "D",
    #"D": "E",
    #"E": "F",
   # "F": "F"
#}
    # test case 2:
    dict =  {
    "A": "F",
    "B": "F",
    "C": "F",
    "D": "F",
    "E": "F",
    "F": "F"
}

    solution = Solution()
    result = solution.managerReport(dict)
    print(result)

if __name__ == "__main__":
    main()