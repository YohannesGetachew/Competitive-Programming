class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middleNode(self, head: ListNode) -> ListNode:
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
