import sorting
import time

def makelist(size):
    answer = []
    for i in range (size):
        answer.append(size - i)
    return (answer)

list100 - makelist(100)
list200 = makelist(200)
list400 = makelist(400)
list800 = makelist(800)
list1600 = makelist(1600)
lists = [list100, list200, list400, list800, list1600]

for alist in lists:
    length = len(alist)
    
    start = time.time()
    anything = sorting.bsort(alist)
    finish = time.time()
    btime = finish - start
    
    start = time.time()
    anything = sorting.ssort(alist)
    finish = time.time()
    stime = finish - start
    
    start = time.time()
    anything = sorting.msort(alist)
    finish = time.time()
    mtime = finish - start
    
    print ('''The list of length {0} took:
    {1} seconds to sort using a bubble sort,
    {2} seconds to sort usihng a Selection sort,
    and {3} seconds to sort using a Merge Sort
    
    '''.format(length, btime, stime, mtime))
