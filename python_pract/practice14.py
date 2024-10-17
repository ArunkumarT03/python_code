'''def summ(n):
    if n==0:
        return 0
    return n+summ(n-1)
print(summ(4))'''

''''def rec(num):
    if num==11:
        return
    print(num)
    rec(num+1)
num=1
rec(num)'''

'''s=input('enter:')
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
mx=max(d.values())
for k in d:
    if d[k]==mx:
        print(f'most reapeted string  {k}:{d[k]}')'''

'''L=[5,6,9,0,12,64]
max_l=0
for i in range(1,len(L)):
    if L[i]>max_l:
        max_l=L[i]
print(max_l)'''
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def mergeTwoLists(l1: ListNode, l2: ListNode):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next
def printList(head: ListNode):
    while head:
        print(head.value, end=' [] ')
        head = head.next
    #print('None')
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged_list = mergeTwoLists(l1, l2)

printList(merged_list)

