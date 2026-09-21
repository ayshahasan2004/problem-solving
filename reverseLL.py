class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        if head is None or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node BEFORE left
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the nodes from left to right
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next