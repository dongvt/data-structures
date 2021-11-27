# The big O notation

The big notation is the way computers scientist use to measure how algorithms performs based on the calculation performed on a given algorithm.

We cam measure how much time an algorithm could be (this is call __time complexity__). We also can measure how much extra memory an algorithm would use (this is called __space complexity__).

We will use the variable __n__ to represent the number of inputs. The result is based on how much space/time is needed based on the input. In this tutorial we will focus on time complexity since in most of the cases we have enough memory.

These are the most common cases:

* When a single computation is done (no mather how big is n) we call it *O(1)*
* When the algorithm makes as many computations as how big is n then we call it *O(n)*
* When the algorithm makes the computation n times twice we could call it *O(2n)* since the result here contains a __constant__ (the constant is 2) the result is still *O(n)*
* When the number of computations grows exponentially we can have a *O(n<sup>2</sup>)* or *O(2<sup>n</sup>)* depending on the growing ratio.
The best example of this is an inner for loop:
```python
def function(n)
    for i in range(n):
        for j in range(n):
            print("hello") 
```
* We can have a logarithmic performance. It means the number of inputs would not increment as fast as *O(log n)*. The best example on this is binary search look at this algorithm no find if a number exist in a sorted array:
```python
def findNumber(list,target):
    start = 0
    end = len(list) - 1
    while(start <= end):
        mid = (start + end) // 2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return False
```

Lastly, the next video will explain in less than two minutes

[![video](https://res.cloudinary.com/marcomontalbano/image/upload/v1637896264/video_to_markdown/images/youtube--g2o22C3CRfU-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=g2o22C3CRfU "Big O Notation in 100 seconds")

[Back to Welcome Page](0-welcome.md)