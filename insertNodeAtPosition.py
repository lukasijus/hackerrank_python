class SinglyLinkedListNode(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def insertNodeAtPosition(head, data, position):
    node = head
    if position == 0:
        newNode = SinglyLinkedListNode(data)
        newNode.next = head
        return newNode
    count = 1
    while count < position and node:
        count += 1
        node = node.next
    newNode = SinglyLinkedListNode(data)
    newNode.next = node.next
    node.next = newNode
    return head

def printLinkedList(head):
    node = head
    while node:
        print(node.data)
        node = node.next 

def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    if head:
        node.next = head
    return node

def deleteNode(head, position):
    current = head
    # next will point to None if there is 
    # not another item in the list
    if position == 0:
        head = head.next
    else:
    	# iterate to the right node
        for i in range(position-1):
            current = current.next
        # and alter the next pointer
        current.next = current.next.next
    return head
