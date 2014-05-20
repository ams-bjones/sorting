#Sorting

This ia a model set of answers for the sorting unit.  refer to http://ams-ict.github.io/GCSEcomputing/u2.html

## Introduction
Sorting is a common activity.  We often need to sort things in an order to make the output better for humans to read, or to process things in a given order.

##Algorithms used in this project
###Pseudocode for a swap


```
BEGIN
INPUT alist, index of item to swap
SET a to index'th item in list
SET b to (index+1)th item in list
SET (index)th item in list to b
SET (index +1 )th item in list to a
OUTPUT alist
END
```

Variables used | type | discussion
----|----|----
alist | a list of integers or floats| this list is the input, and it is also the out put once the swap has taken place.
index | integer |  this is the position of the item in the list to be swapped
a | Integer or float | This is a temporary variable which stores the first item to be swapped, at index in the list
b | Integer or float| This is a temporary variable which stores the second item to be swapped

###Pseudocode for bubble sort


```
BEGIN
INPUT alist
SET swaps to True
WHILE swaps is True:
    SET Swaps to False
    FOR item in alist:
        IF item > next item:
            Swap item and next item
            Set Swaps to True
OUTPUT alist
END
```
Variables used | type|discussion
----|----|----
alist | a list of integers or floats| This is the list that is to be sorted
swaps | Boolean | this is an internal varible which lets the while loop know when to stop iterating
item| Integer or float | this variable exists in the for loop - it is the item in alist that is being iterated.

### pseudocode for  finding the minimum (mini())
```
BEGIN
INPUT alist
SET answer to first item of list
FOR EACH number in alist:
    IF number < answer:
        set answer to number
OUTPUT answer
END
```

Variables used | type|discussion
----|----|----
alist | a list of integers or floats| This is the list that is to be sorted
answer | Integer or float | This is the answer that will be output.  It starts off as the first item in alist, and is compared with every other item to check if it is the lowest.
number | interger or flost from alist | This is the variable used in the iteration (for loop) which contains teh number being compared with the minimum

### pseudocode for Selection sort 
```
BEGIN
INPUT alist
set answer to [] (an empty list)
WHILE length of alist > 0:
    set N to minimum of alist (see previous code)
    remove N from alist
    append N to answer
OUTPUT answer
END
```
Variables used | type|discussion
----|----|----
alist | a list of integers or floats| This is the list that is to be sorted
answer | a list of integers or floats | This is the list that is to be output.  it is filled by extracting the minimum item in alist in order
N | integer or float | This is the temporary variable in the while loop (iteration) 


## Testing
###Swap Criteria
The swap function will be successful if
it accepts a list and an index as input
it returns the list with the indexed item swapped with its next item.


example input|Expected output
----|----
[4,3,2,1], 1 | [4,2,3,1]
[4,3,2,1], 0 | [3,4,2,1]
[1,2], 0 | [2,1]

### Finding the minimum
The minimum function will be succe4ssfull if it takes a list, and extracts the minimum from it.

example input|Expected output
----|----
[4,3,2,1] | 1
[4,3,2, 2] | 2
[1,2, -1] | -1


### Sorting criteria
For the swap functions the input should be an unsorted list, and the output should be a sorted list.
These tests apply equally to the bubble sort, selection sort, and merge sort, functions.

example input | Example output
----|----
[4,3,2,1] | [1,2,3,4]
[1,2,3,4] | [1,2,3,4]
[3,7,1] | [1,3,7]
[1.2, 3.6, 2.4] | [1.2, 2.4, 3.6]
