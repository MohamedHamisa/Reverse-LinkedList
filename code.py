class Solution:
    def reverseList(self, head):
        current = head
        prev = None
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
