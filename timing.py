import sorting
import random
import time

def makelist(size):
    answer = []
    for i in range(size):
        n= random.randrange(7080000)
        answer.append(n)
    return(answer)

def profile(lists):
    for alist in lists:
        length = len(alist)
        start = time.time()
        something = sorting.bsort(alist)
        finish = time.time()
        btime = finish - start
        start = time.time()
        something = sorting.ssort(alist)
        finish = time.time()
        stime = finish - start
        start = time.time()
        something = sorting.msort(alist)
        finish = time.time()
        mtime = finish - start
        print("""The time taken to sort a list of length {0} is 
        {1} using the bubble sort algorithm, 
        {2} using the Selection sort algorithm, 
        and {3} using the merge sort algorithm""".format(length, btime, stime, mtime))

list100 = makelist(100)
list200 = makelist(200)
list400 = makelist(400)
list800 = makelist(800)
list1600 = makelist(1600)
lists = [list100, list200, list400, list800, list1600]
profile(lists)