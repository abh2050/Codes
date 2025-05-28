```python
'''
# Remove Duplicates from Sorted List
# Difficulty: Easy

# Problem Description:
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Examples:
# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
# Explanation: The first two nodes have value 1, so the first is kept and the second is removed. The last node has value 2 so it is kept as well.

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
# Explanation: The first two nodes have value 1, so the first is kept and the second is removed.
#              The second two nodes have value 3, so the first with 3 is kept and the second with 3 is removed.


# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Removes duplicate nodes from a sorted linked list.

        Args:
            head: The head of the linked list.

        Returns:
            The head of the modified linked list with duplicates removed.
        """
        if not head:
            return head

        current = head
        while current.next:  # Iterate until the last node
            if current.val == current.next.val:  # Duplicate found
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next node

        return head  # Return the modified list


# Time Complexity: O(n), where n is the number of nodes in the linked list, as we iterate through the list once.
# Space Complexity: O(1), as we use constant extra space.


# Test Cases
head1 = ListNode(1, ListNode(1, ListNode(2)))
result1 = Solution().deleteDuplicates(head1)
# Expected Output: [1,2]

head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
result2 = Solution().deleteDuplicates(head2)
# Expected Output: [1,2,3]

head3 = None  # Empty List
result3 = Solution().deleteDuplicates(head3)
# Expected Output: None


# Helper function to print linked list
def print_linked_list(head):
    if not head:
        print("[]")
        return
    
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

print_linked_list(result1)
print_linked_list(result2)
print_linked_list(result3)

```