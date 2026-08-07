# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):

        # Handle empty list
        if head is None:
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# -------------------------------
# Function to create linked list
# -------------------------------
def createLinkedList(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    nodes = [head]

    for value in arr[1:]:
        newNode = ListNode(value)
        current.next = newNode
        current = newNode
        nodes.append(newNode)

    return head, nodes


# -------------------------------
# Example Input
# -------------------------------

arr = [3, 2, 0, -4]
pos = 1          # Connect last node to node at index 1

head, nodes = createLinkedList(arr)

# Create cycle
if pos != -1:
    nodes[-1].next = nodes[pos]

# -------------------------------
# Test
# -------------------------------

sol = Solution()

print(sol.hasCycle(head))