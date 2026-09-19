class ListNode:
    def __init__(self, val: int = 0, next_node: "ListNode | None" = None):
        self.val = val
        self.next = next_node


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head is None or left == right:
            return head

        dummy = ListNode(next_node=head)
        before_reversed = dummy

        for _ in range(left - 1):
            before_reversed = before_reversed.next

        current = before_reversed.next
        for _ in range(right - left):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = before_reversed.next
            before_reversed.next = node_to_move

        return dummy.next
