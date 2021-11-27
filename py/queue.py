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

print(findNumber([1,2,3,4,5,6,7,8,9,10],3))
print(findNumber([1,2,4,5,6,7,8,9,10,11],3))