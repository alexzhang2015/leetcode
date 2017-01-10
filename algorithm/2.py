# -*- coding: utf-8 -*-
"""
2. Add Two Numbers
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        node = ListNode((l1.val + l2.val) % 10)
        node_pos = node
        carry = (l1.val + l2.val) / 10

        node1 = l1.next
        node2 = l2.next
        while node1 is not None or node2 is not None:
            if node1 is None:
                node_pos.next = ListNode((node2.val + carry)%10)
                carry = (node2.val + carry) / 10
                node2 = node2.next
                node_pos = node_pos.next

            elif node2 is None:
                node_pos.next = ListNode((node1.val + carry)%10)
                carry = (node1.val + carry) / 10
                node1 = node1.next
                node_pos = node_pos.next

            else:
                node_pos.next = ListNode((node1.val + node2.val + carry)%10)
                carry = (node1.val + node2.val + carry) / 10
                node1 = node1.next
                node2 = node2.next
                node_pos = node_pos.next

        # handle last carry
        if carry > 0:
            node_pos.next = ListNode(carry)

        return node


def main():
    # prepare test date
    node1 = ListNode(2)
    node1.next = ListNode(4)
    node1.next.next = ListNode(3)
    node2 = ListNode(5)
    node2.next = ListNode(6)
    node2.next.next = ListNode(6)

    # solution
    solution = Solution()
    node = solution.addTwoNumbers(node1, node2)
    while node is not None:
        print node.val
        node = node.next

if __name__ == "__main__":
    main()
