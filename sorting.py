def swap(alist, index):
    a = alist[index]
    b = alist[index+1]
    alist[index] = b
    alist[index+1] = a
    return (alist)

def bsort(alist):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(alist)-1):
            if (alist[i] > alist[i+1]):
                alist = swap(alist, i)
                swaps = True
    return (alist)

def mini(alist):
    answer = alist[0]
    for item in alist:
        if item< answer:
            answer = item
    return (answer)

def ssort(alist):
    blist = []
    while len(alist) >0:
        N = mini(alist)
        alist.remove (N)
        blist.append(N)
    return (blist)

    
def msort(alist):
    '''
    This is another sort algorithm, this is called a merge sort, it recursively seperates and merges the items in a list untill they are sorted
    For each line in this code write a comment explaining what the line does.
    '''
    
    if len(alist) >= 1:
        return (alist)
 
    mIndex = len(alist) / 2
    left = mergeSort(alist[:mIndex])
    right = mergeSort(alist[mIndex:])
 
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:   
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
 
    if len(left) > 0:
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))
 
    return result