'''Add Two Numbers:

    Given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single
    digit. Add the two numbers and return it as a linked list.'''

class ListNode(object):
    '''Definition for singly-linked list.'''

    def __init__(self, x):
        '''simple list node'''
        self.val = x
        self.next = None

class Solution(object):
    '''May asusme the two numbers do not contain any leading zero, except the number
    0 itself'''

    def add_two_numbers(self, l1, l2):
        '''
        keywords input:
        type l1 - ListNode
        type l2 - ListNode
        return type - ListNode
        '''

        carry = 0
        head = ListNode(0)
        tail = head

        while l1 or l2:
            current_val = tail.val

            if l1:
                current_val += l1.val
                l1 = l1.next

            if l2:
                current_val += l2.val
                l2 = l2.next

            carry = current_val // 10
            tail.val = current_val % 10

            if carry == 1 or l1 or l2:
                tail.next = ListNode(carry)
                tail = tail.next
                carry = 0

        return head

def main():
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    result = Solution().add_two_numbers(a, b)
    while result:
        if result.next:
            print('{', result.val, '} -> ', end='')
        else:
            print('{', result.val, '}')
        result = result.next

main()
