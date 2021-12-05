# Tree

A `tree` is a data structure designed to represent herarchical data

A tree is represented by a parent `node` which would link to other nodes. The main node which is used to get all other nodes is called the `root` of the tree. Each node the root link to is called a `child`.

One of the most common `tree` structure is called a `binary tree`. As its name implies, a binary tree us a tree were each node have two or less children. Here is an illustration.

![Binary tree](img/binary-tree-example-tree.jpg)

>__Note:__ In this tutorial, the examples will work just with binary trees. At the end we will solve a more complex problem to show an example of a different `tree` structure.

In this example the node which value 1 is the `root` of our tree, its childrean are nodes 2 and 3 which at the same time have their own children. That means we can have a `subtree` taking 2 or 3 as our root:

![sub tree](img/subtree-example-tree.jpg)

In this subtree nodes 4 and 5 are at the end of the tree. This nodes are called `leaf nodes`

## How do I "*explore*" a tree?
How can we get all the values in each node of the tree? Since each node is identical, we could potentially use an idential function on each node to get the value. What we do in `trees` is create a single function and then make it call itself. Function that call itself are called *recursive functoins*.

Lets see an exaple. First we would need to design our node:

```python
class TreeNode(object):
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None
```

Now that we have a node structure, lets create the our example `tree`
```python
#First level
root = TreeNode(1)
#Second level
root.left = TreeNode(2)
root.right = TreeNode(3)

#Third level
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
```

Now we can create our *recursive function*. When working with this type of functions we should __always__ have a `base case`. A base case is the instruction that will stop the iteration. With no base case our recursive function will fall in an infinite loop.

We just want to the data, so the we will stop the `recursive calls` when we don't have node availble (node is null):

```python
def printTree(root):
    if root is None:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)
```

>To test `printTree` just call it and using the tree created before as a parameter.
>```
>printTree(root)
>```

Now, the result is not perfectly ordered:
```
1
2
4
5
3
6
7
```
>### Quick overview of a stack
>This algorithm is the base for `depth first search` algorithm. The informaiton about this algorithm in [wikipedia](hhttps://en.wikipedia.org/wiki/Depth-first_search) says we need to use a `stack`. Indeed, we are using a hidden stack here. Which is a section of the memory where each recursion call is stored and then poped when a function ends. This is a long topic out of the scope of this tutorial. If you are curious check [this](https://www.geeksforgeeks.org/memory-layout-of-c-program/) out.

Continuing with our output the result is just a way we have to `traverse` the tree and the example above is called `preorder traversal`. It is simple to understand, we are just printing all the elements at the root then left of the tree and then the elements at the right, here in illustration:

![Preorder Traversal](img/preorder-traversal-tree.gif)

We can give priority to the left side (before the root), this is called `inorder traversal`.

```python
def inorderTraversal(root):
    if root is None:
        return
    
    inorderTraversal(root.left)
    print(root.val)
    inorderTraversal(root.right)
```
Here is an illustration:
![Preorder Traversal](img/inorder-traversal-tree.gif)

What if we want to begin from the leaft at the very left? This is called `Postorder traversal` the definition for postorder traversal is get the subtree at the left before, the subtree at the right and finally visit the root.

Take a look:
![Preorder Traversal](img/postorder-traversal-tree.gif)

how would you solve it? [here](py/tree-traversal.py) is a link to all the traversal solution discused in this tutorial.

In all the traversal methods we have not seen a result that actually returns the order in which we created the nodes (expected result like: `1,2,3,4,5,6,7`). This is possible but we don't use recursion, instead we use `levelorder traversal` or breadth first search as we did in the queue example.

This function would return `1,2,3,4,5,6,7`:
```python
from collections import deque
def levelorderTraversal(root):
    q = deque()

    q.append(root)

    while(len(q) > 0):
        node =  q.popleft()
        print(node.val)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
```
Note that there is not need of recursion.

__Time and Space complexity__ all the traversal funcitions discused here are *O(n)* where n is the number of nodes in the tree. However in order to traverse the tree we would need to store the entire tree somewhere else (wether the stack or a queue). Thus the space complexity would be *O(n)*.

## Solving problems



[Back to Welcome Page](0-welcome.md)
