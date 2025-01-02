# Find the middle of the linked list with two pointers 
# Time: O(n), space: O(1)

def middleOfList(head):
    slow, fast = head, head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    return slow 

# Determine if the linked list contains a cycle 
# Time: O(n), space: O(1)

def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True 
    return False 

# Determine if the linked list contains a cycle 
# return the beginning of the cycle, otherwise return the null 

def cycleStart(head):
    slow, slow2, fast = head, head, head 

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow = fast:
            break 
        
        if not fast or fast.next:
            return None 

        while slow != slow2:
            slow = slow.next 
            slow2 = slow2.next
    
        return slow 

        
