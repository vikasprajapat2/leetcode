class Solution(object):
    def addTwoNumbers(self, l1, l2):
        cur=ListNode(0)
        dummy=cur
        carry=0
        while l1 or l2 or carry:
            sum=carry
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            # set value
            if sum<=9:
                cur.val=sum
                carry=0
            else:
                cur.val=sum%10
                carry=sum//10
            # creat new node
            if l1 or l2 or carry:
                cur.next=ListNode(0)
                cur=cur.next
        return dummy

        