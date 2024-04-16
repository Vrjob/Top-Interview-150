"""
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

""" Errado
def addTwoNumbers(self, l1, l2):
    l1.reverse()
    l2.reverse()
    newL1 = (''.join(str(x) for x in l1))
    newL2 = (''.join(str(x) for x in l2))

    addList = int(newL1) + int(newL2)
    res = [int(x) for x in str(addList)]

    return res


l1 = [2,4,3]
l2 = [5,6,4]

addTwoNumbers(0, l1, l2) """

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)
        result = num1 + num2
        return self.create_list(result)

    def get_number(self, l):
        number_str = ''
        while l:
            number_str += str(l.val)
            l = l.next
        return int(number_str[::-1])

    def create_list(self, number):
        head = ListNode(None)
        current = head
        for digit in str(number)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next
        return head.next
