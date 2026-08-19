class Solution(object):
    def detectCycle(self, head):

        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Step 2: Find beginning of cycle
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None