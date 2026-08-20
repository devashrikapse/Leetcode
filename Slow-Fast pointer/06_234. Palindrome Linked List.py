class Solution(object):
    def isPalindrome(self, head):

        # Find middle
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        current = slow

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare first half and reversed second half
        first = head
        second = prev

        while second is not None:

            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True