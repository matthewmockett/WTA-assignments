# author: Mleemock@uwo.ca
# Date: June 18, 2024
'''
Question 4 - Linked Lists
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. 
The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 
2s at the end of the linked list, and 1s in the mid of 0s and 2s.
'''
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def segregate(self, N, head):

        # Initlize a count list to keep track of the number of each 0, 1 and 2.
        count = [0, 0, 0]

        # Initalize a pointer to the head of the linked list.
        current = head

        # While loop that counts the number of 0s, 1s, 2s and adds them to the count list.
        while current:
            count[current.val] +=1
            current = current.next

        # Move the pointer back to the head so we can start filling in the linked list in the correct order.
        current = head

        # Use a nested loop starting with the for loop that will iterate through the 0s, 1 and 2's
        for i in range(3):

            # Each time an element is used, set the value to the current position in the linked list,
            # move to the next element and subtact one in the count.
            while count[i] > 0:
                current.val = i
                current = current.next
                count[i] -=1
        
        return head
    
# output for test case 1: 0 0 0 1 1 2 2 2
# output for test case 2: 0 0 0 1 1 1 1 1 2 2 2

def main():
    nodes = [ListNode(0), ListNode(1), ListNode(2), ListNode(0), ListNode(2), ListNode(0), ListNode(2), ListNode(1)] # test case 1
    #nodes = [ListNode(1), ListNode(1), ListNode(0), ListNode(1), ListNode(2), ListNode(0), ListNode(1), ListNode(2), ListNode(0), ListNode(2), ListNode(1)] # Test case 2
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    head = nodes[0]
    N = 8 

    solution = Solution()
    segregatedHead = solution.segregate(N, head)

    current = segregatedHead
    while current:
        print(current.val, end=" ")
        current = current.next

if __name__ == "__main__":
    main()

