class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next 

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head 

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 

    def insertHead(self, val: int) -> None:
        curr = self.head 
        new_head = ListNode(val)
        new_head.next = curr.next
        curr.next = new_head
        if new_head.next == None:
            self.tail = new_head
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr.next:
            i += 1
            curr = curr.next
        if curr and curr.next:    
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False 

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values 
        
