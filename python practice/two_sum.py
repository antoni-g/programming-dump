# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        
        it1 = l1
        it2 = l2
        ret = None     
        curr = None
        prev = None
        while not it1 == None and not it2 == None: 
            sum = it1.val + it2.val + carry
            print(sum)
            if sum == 10:
                carry = 1
                sum = 0
            elif sum > 10:
                carry = 1
                sum %= 10
            else:
                carry = 0
            print(sum)
            print(carry)
            new = ListNode(sum)
            if ret == None:
                ret = new
            if not prev == None:
                prev.next = new
            prev = new
            it1 = it1.next
            it2 = it2.next
        
        proc = None
        if not it1 == None:
            proc = it1
        elif not it2 == None:
            proc = it2
        elif not carry == 0:
            print(carry)
            prev.next = ListNode(carry)
            
        return ret

def construct_list(input):
    if len(input) > 0:
        head = ListNode(input[0])
        prev = head
        for i in range(1, len(input)):
            new = ListNode(input[i])
            prev.next = new
            prev = new
        return head

def print_list(head):
    ret = "<"
    curr = head    
    while not curr == None:
        ret+= str(head.val)        
        curr = curr.next
        if not curr == None:
            ret += ", "
    ret += ">"
    print(ret)



check = Solution()
l1 = [2,3,1]
l2 = [2,4,1]
print_list(check.addTwoNumbers(construct_list(l1),construct_list(l2)))

