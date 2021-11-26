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
        node = MyLinkedList.Node(val) #1
        
        if self.size == 0: # Special case: empty linked list
            self.tail = node
            self.head = node
        else: 
            node.next = self.head #2
            self.head.prev = node #3
            self.head = node #4
        
        self.size = self.size + 1 #size increases when we add a new node to the list

    def addAtTail(self, val):
        node = MyLinkedList.Node(val) #1
        
        if self.size == 0: # Special case: empty linked list
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail #2
            self.tail.next = node #3
            self.tail = node #4

        self.size = self.size + 1 #size increases when we add a new node to the list
        

    def addAtIndex(self, index, val):
        if index == self.size: #Special case index = size: add to tail instead
            self.addAtTail(val)
            return
        
        if index == 0: #Special case index = 0: add to head instead
            self.addAtHead(val)
            return
        
        if index > self.size: #Special case index out of bounds: don't do anything
            return
        
        node = self.head #1
        for i in range(index):
            node = node.next
            
        newNode = MyLinkedList.Node(val) #2
        
        newNode.next = node #3
        newNode.prev = node.prev #4
        
        node.prev.next = newNode #5
        node.prev = newNode #6
        
        self.size = self.size + 1 #increment our size helper
        
        
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size or self.size == 0:
            return
        
        #Special case: delete the head
        if index == 0:
            if self.size == 1: #Special case: A single element in the list
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

            self.size = self.size - 1
            return

        #Special case: delete the tail
        if index == self.size - 1:
            if self.size == 1: #Special case: A single element in the list
                self.tail = None
                self.head = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

            self.size = self.size - 1
            return

        node = self.head
        for i in range(index): #1
            node = node.next
            
        node.next.prev = node.prev #2
        node.prev.next = node.next #3
        
        self.size = self.size - 1 #This time we decrement since we are deleting elements

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
        output = "MyLinkedList["
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



# obj = MyLinkedList()

# obj.addAtHead(24)
# print(obj.get(1))
# obj.addAtTail(18)
# obj.deleteAtIndex(1)
# print(obj.get(1))
# obj.addAtTail(30)
# print(obj.get(2))
# obj.deleteAtIndex(1)
# obj.addAtHead(3)
# obj.addAtHead(3)
# obj.addAtHead(33)
# obj.addAtHead(97)
# obj.addAtTail(43)
# obj.addAtTail(12)
# obj.addAtTail(10)
# obj.deleteAtIndex(1)
# obj.addAtIndex(1,56)
# obj.addAtHead(30)
# obj.addAtIndex(8,83)
# obj.addAtTail(57)
# obj.addAtHead(74)
# print(obj.get(5))
# obj.addAtHead(98)
# obj.addAtTail(72)
# obj.addAtHead(34)
# obj.addAtHead(61)
# print(obj.get(6))
# obj.addAtHead(70)
# obj.addAtHead(24)
# obj.addAtTail(91)
# obj.addAtHead(99)
# obj.addAtTail(13)
# obj.addAtTail(10)
# obj.deleteAtIndex(17)
# obj.addAtTail(84)
# obj.deleteAtIndex(16)
# obj.addAtHead(73)
# obj.addAtTail(88)
# obj.addAtIndex(4,19)
# obj.addAtHead(59)
# obj.addAtTail(41)
# obj.addAtHead(57)
# obj.deleteAtIndex(10)
# obj.deleteAtIndex(18)
# obj.addAtHead(2)
# obj.addAtTail(12)
# obj.addAtTail(25)
# obj.addAtHead(1)
# obj.addAtHead(77)
# print(obj.get(1))
# obj.deleteAtIndex(7)
# obj.addAtHead(34)
# obj.addAtTail(87)
# obj.deleteAtIndex(13)
# obj.addAtTail(4)
# obj.addAtTail(12)
# obj.addAtTail(11)
# obj.addAtIndex(10,92)
# obj.addAtIndex(21,55)
# print(obj.get(11))
# obj.addAtTail(38)
# obj.addAtTail(31)
# obj.addAtHead(45)
# obj.addAtTail(4)
# obj.addAtTail(21)
# obj.addAtHead(38)
# print(obj.get(4))
# obj.addAtTail(88)
# print(obj.get(12))
# obj.deleteAtIndex(22)
# obj.addAtHead(40)
# obj.addAtHead(22)
# obj.addAtHead(23)
# obj.addAtIndex(13,96)
# obj.addAtIndex(24,50)
# obj.deleteAtIndex(8)
# print(obj.get(14))
# obj.addAtTail(25)
# obj.addAtTail(53)
# obj.addAtHead(42)
# print(obj.get(6))
# obj.addAtHead(58)
# obj.addAtTail(55)
# obj.addAtIndex(18,72)
# obj.deleteAtIndex(13)
# obj.addAtHead(30)
# obj.addAtHead(97)
# obj.addAtTail(59)
# print(obj.get(47))
# obj.deleteAtIndex(24)
# obj.addAtHead(37)
# obj.addAtTail(26)
# obj.addAtTail(31)
# obj.addAtHead(93)
# obj.addAtHead(66)
# obj.deleteAtIndex(11)
# print(obj.get(43))
# obj.addAtHead(70)
# obj.addAtTail(36)
# obj.addAtHead(31)
# obj.addAtTail(28)

# print(obj)

"""
Expected result:
-1
-1
-1
3 
56
1 
61
1
92
19
34
21
12
MyLinkedList[31, 70, 66, 93, 37, 97, 30, 58, 42, 23, 22, 40, 38, 34, 77, 1, 57, 59, 73, 96, 70, 19, 92, 72, 61, 34, 98, 97, 3, 3, 50, 24, 43, 55, 72, 91, 13, 10, 84, 88, 41, 12, 25, 
87, 4, 12, 11, 38, 31, 4, 21, 88, 25, 53, 55, 59, 26, 31, 36, 28] Head 31 Tail 28
"""