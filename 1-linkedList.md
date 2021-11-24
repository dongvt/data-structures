# Linked-List

## What is a linked list?
A linked list is a collection of data elements that are connected with pointers. There are two types of linked-lists: `single linked` and `double linked`. 

The main difference between a linked list and an Array is how they are store in memory. Arrays use contiguous memory w

### Single liked list
In the single linked list, the the elements (also called `nodes`) are connected in a linear way. A single node could be represented like the image bellow:

![Node single Linked-List](img/single-linked-list-node.jpg)

The first element (called `head`) point to the next node, and that next node point to the next and so on as represented in the image bellow:

![Single Linked Linked-List](img/single-linked-list.jpg)

The last node in the list will have the next pinter pointing to null

### Double liked list
In the double linked list the nodes have two pointers and a data value, the additional pointer in the double list points to the prev pointer. 
Here is a visual representation of a single node:

![Node double Linked-List](img/double-linked-list-node.jpg)

In adition, a double linked list have two aditional pointers, one pointing to the first node (Called the `Head`) an another pointing to the last node (Called the `Tail`). Here a visual representation of a complete double linked list:

![double Linked-List](img/double-linked-list.jpg)

## Designing our own linked list in python
There is not in build in class for a linked list on python however we can design a class to create a list which behaved like a liked list, in this tutorial we will work with a double linked list since this is the most complete example

We will create the next methods in our class to interact with our linked list (we will follow the [leetcode](https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/) sample):

* `get(index)`: Will get the value of the index<sup>th</sup> node in the linked list. If the index is invalid, return -1.
* `addAtHead(val)`: Will add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
* `addAtHead(val)` Will add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
* `addAtTail(val)` Will append a node of value `val` as the last element of the linked list.
* `addAtIndex(index, val)` Add a node of value `val` before the index<sup>th</sup> node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will *not be inserted*.


This is the template for linked list class (again, this is provided by [leetcode](https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/))

```
class MyLinkedList(object):

    def __init__(self):
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
```

First thing to do here, is to add a subclass for our nodes, here we write a constructor to create our default node:

```
class Node:
    def __init__(self,data):
        self.val = data
        self.prev = None
        self.next = None
```
We got the data and store into `val`, by default the previous and next pointers will be `None`

The constructor will have set our tail and head pointers to `None`, in adition we will set a `size` as helper for other functions

```
def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
```

For the `get` method we should begin by the head and iterate through the list `index` times, and then return the value of the current node. The `get` function would look like:

```
def get(self, index):
    if self.head is None: #If the list is empty we don't have something to return
        return -1
    
    node = self.head #Begin with the head
    for i in range(index):
        node = node.next #Iterate through the list
        if node is None: #Invalid index
            return -1

    return node.val #Return the current value
```
If this code is not perfectly clear, take a look to this image:

![get linked list](img/get-linked-list.gif)

For the `addToHead` function we need to follow this steps:
1. Create a new node
2. Set the next pointer from the new node to the current head
3. Set the prev pointer from the head to the new node
4. Assign the current head to the new pointer

Graphically the step by step would look like:
![get linked list](img/add-head-linked-list.gif)

In the code we have an special case, this is when adding the first node to our linked list. In this specific case we set both the tail and head to the same node. The add function would look like:
```
def addAtHead(self, val):        
    node = MyLinkedList.Node(val) #1
    
    if self.size == 0: # Special case: empty linked list
        self.tail = node
        self.head = node
    else: 
        node.next = self.head #2
        self.head.prev = node #3
        self.head = node #4
    
    self.size = self.size + 1 #if we have a new node the size increases
```

[Back to Welcome Page](README.md)
