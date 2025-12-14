"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        h={}
        cur=head
        while cur:
            h[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            h[cur].next=h.get(cur.next)
            h[cur].random=h.get(cur.random)
            cur=cur.next
        return h[head]
        
        
