    # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):

        middle = head
        end = head

        while end is not None and end.next is not None:

            middle = middle.next
            end = end.next.next

        return middle


# -----------------------------
# Function to create Linked List
# -----------------------------
def createLinkedList(arr):

    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


# -----------------------------
# Function to print Linked List
# -----------------------------
def printLinkedList(head):

    while head is not None:
        print(head.val, end=" -> ")
        head = head.next

    print("None")


# -----------------------------
# Driver Code
# -----------------------------

arr = [1, 2, 3, 4, 5, 6]

head = createLinkedList(arr)

print("Original Linked List:")
printLinkedList(head)

sol = Solution()

middle = sol.middleNode(head)

print("\nMiddle Node onwards:")
printLinkedList(middle)