class MyLinkedList(object):
    class Node:
        def __init__(self,data):
            self.val = data
            self.prev = None
            self.next = None
            

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self, index):
        if self.head is None: #If the list is empty we don't have something to return
            return -1
        
        node = self.head #Begin with the head
        for i in range(index):
            node = node.next #Iterate through the list
            if node is None: #Invalid index
                return -1

        return node.val #Return the current value
        
    def addAtHead(self, val):        
        node = MyLinkedList.Node(val) #Create the new node
        
        if self.size == 0: # Special case: empty linked list
            self.tail = node
            self.head = node
        else: 
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        self.size = self.size + 1 #if we have a new node the size increases

    def addAtTail(self, val):
        node = MyLinkedList.Node(val)
        
        if self.size == 0: # Special case: empty linked list
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size = self.size + 1
        

    def addAtIndex(self, index, val):
        if index == self.size:
            self.addAtTail(val)
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        if index > self.size:
            return
        
        node = self.head
        for i in range(index):
            node = node.next
            
        newNode = MyLinkedList.Node(val)
        
        newNode.next = node
        newNode.prev = node.prev
        
        node.prev.next = newNode
        node.prev = newNode
        
        self.size = self.size + 1
        
        
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size or self.size == 0:
            return
        
        #Special case: delete the head
        if index == 0:
            if self.size == 1:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

            self.size = self.size - 1
            return

        #Special case: delete the tail
        if index == self.size - 1:
            if self.size == 1:
                self.tail = None
                self.head = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

            self.size = self.size - 1
            return

        node = self.head
        for i in range(index):
            node = node.next
            
        node.next.prev = node.prev
        node.prev.next = node.next
        
        self.size = self.size - 1

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.val  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        output += " Head " + str(self.head.val)
        output += " Tail " + str(self.tail.val)

        return output



obj = MyLinkedList()

obj.addAtHead(24)
print(obj.get(1))
obj.addAtTail(18)
obj.deleteAtIndex(1)
print(obj.get(1))
obj.addAtTail(30)
print(obj.get(2))
obj.deleteAtIndex(1)
obj.addAtHead(3)
obj.addAtHead(3)
obj.addAtHead(33)
obj.addAtHead(97)
obj.addAtTail(43)
obj.addAtTail(12)
obj.addAtTail(10)
obj.deleteAtIndex(1)
obj.addAtIndex(1,56)
obj.addAtHead(30)
obj.addAtIndex(8,83)
obj.addAtTail(57)
obj.addAtHead(74)
print(obj.get(5))
obj.addAtHead(98)
obj.addAtTail(72)
obj.addAtHead(34)
obj.addAtHead(61)
print(obj.get(6))
obj.addAtHead(70)
obj.addAtHead(24)
obj.addAtTail(91)
obj.addAtHead(99)
obj.addAtTail(13)
obj.addAtTail(10)
obj.deleteAtIndex(17)
obj.addAtTail(84)
obj.deleteAtIndex(16)
obj.addAtHead(73)
obj.addAtTail(88)
obj.addAtIndex(4,19)
obj.addAtHead(59)
obj.addAtTail(41)
obj.addAtHead(57)
obj.deleteAtIndex(10)
obj.deleteAtIndex(18)
obj.addAtHead(2)
obj.addAtTail(12)
obj.addAtTail(25)
obj.addAtHead(1)
obj.addAtHead(77)
print(obj.get(1))
obj.deleteAtIndex(7)
obj.addAtHead(34)
obj.addAtTail(87)
obj.deleteAtIndex(13)
obj.addAtTail(4)
obj.addAtTail(12)
obj.addAtTail(11)
obj.addAtIndex(10,92)
obj.addAtIndex(21,55)
print(obj.get(11))
obj.addAtTail(38)
obj.addAtTail(31)
obj.addAtHead(45)
obj.addAtTail(4)
obj.addAtTail(21)
obj.addAtHead(38)
print(obj.get(4))
obj.addAtTail(88)
print(obj.get(12))
obj.deleteAtIndex(22)
obj.addAtHead(40)
obj.addAtHead(22)
obj.addAtHead(23)
obj.addAtIndex(13,96)
obj.addAtIndex(24,50)
obj.deleteAtIndex(8)
print(obj.get(14))
obj.addAtTail(25)
obj.addAtTail(53)
obj.addAtHead(42)
print(obj.get(6))
obj.addAtHead(58)
obj.addAtTail(55)
obj.addAtIndex(18,72)
obj.deleteAtIndex(13)
obj.addAtHead(30)
obj.addAtHead(97)
obj.addAtTail(59)
print(obj.get(47))
obj.deleteAtIndex(24)
obj.addAtHead(37)
obj.addAtTail(26)
obj.addAtTail(31)
obj.addAtHead(93)
obj.addAtHead(66)
obj.deleteAtIndex(11)
print(obj.get(43))
obj.addAtHead(70)
obj.addAtTail(36)
obj.addAtHead(31)
obj.addAtTail(28)


print(obj)