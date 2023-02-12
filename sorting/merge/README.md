# Blog Notes: Merge Sort
<hr>

## Author: Domaine Scully

# Merge Sort

Merge sort is an efficient sorting algorithm with a time complexity of O(nlogn). It achieves this efficiency through a “divide and conquer” approach of repeatedly splitting an array of unsorted numbers in half (usually recursively) down to a base case of one or two elements in each subarray. It sorts each of those subarrays. Finally, it merges all of these subarrays back together. The merge step can be performed in O(n) time, since all the subarrays are already sorted.

The merge step involves comparing two subarrays at a time, looking at the front element of each, and taking
whichever front element is smaller. This is guaranteed to be the smallest element in either array, since both arrays
are sorted. Repeating this process (and appending the full remaining subarray once one of the subarrays runs out of
values) reliably produces a combined sorted list of values in linear time.

Multiple merge steps of multiple subarrays yield a fully sorted array. Here is the code in Python (note that arrays in Python are called lists, so here the variable lst is used to represent the input array/list):

```
def mergesort(lst):
    n = len(lst)

    if n > 1:
        mid = n//2
        left = lst[0:mid]
        right = lst[mid:]

        mergesort(left)
        mergesort(right)
        merge(left, right, lst)

    return lst


def merge(left, right, lst):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1

        else:
            lst[k] = right[j]
            j += 1

        k += 1

    # Append remaining list elements when one list runs out
    if i == len(left):
        for idx in range(j, len(right)):
            lst[k] = right[idx]
            k += 1
    else:
        for idx in range(i, len(left)):
            lst[k] = left[idx]
            k += 1
```

There are two functions in this code: the `mergesort` function, which does the recursive splitting of the array into subarrays, and the `merge` helper function, which performs the merge step.

The most confusing part of this algorithm is understanding the order of the recursive calls. Here is an example that sheds light on how the recursive calls produces the desired order of splitting and merging.

Say we want to sort the following numbers: [8, 4, 23, 42, 16, 15]

Mergesort is called on this list, and since the length of the list is greater than one, values for the variables mid, left, and right are computed and stored. Their values are the following:

lst = [8, 4, 23, 42, 16, 15]\
mid = 3\
left = [8, 4, 23]\
right = [42, 16, 15]

After these variable assignments, the first recursive call is made to mergesort, and this time, just the left half
of the original list is passed in (stored in the variable left). To help
visualize the order of all
the recursive calls, since there will be many, here's a table that keeps track of the state of the call stack, as
well as the last line of
code executed by each function before its execution was paused. This way it's clear where the function should resume
once it again reaches the top of the call stack.

|Call Stack| Last Execution|
|:---:|:---:|
|mergesort([8, 4, 23])|
|mergesort([8, 4, 23, 42, 16, 15])| mergesort(left)

The call at the bottom of the stack is now paused, and the function at the top of the stack executes. Variable
assignments are made, and then another recursive call is made to mergesort, again passing in just the left half of
the current list. This pattern continues until the base case is reached, which is a list of length 1. This will finally
allow the function at the top of the call stack to resume execution and move on to the call to mergesort(right).

|Call Stack| Last Execution|
|:---:|:---:|
|mergesort([8]) |
|mergesort([8, 4, 23])| mergesort(left)
|mergesort([8, 4, 23, 42, 16, 15])| mergesort(left)

Here the top function on the call stack is just one element, so its call to mergesort(left) returns without
executing the `if` statement, and this call is removed from the top of the stack. The new function at the top of the
stack can resume execution and calls meregesort(right), which spawns more recursive calls as follows.

|            Call Stack             | Last Execution|
|:---------------------------------:|:---:|
| mergesort([4])
|        mergesort([4, 23])         |mergesort(left)
|       mergesort([8, 4, 23])       | mergesort(right)
| mergesort([8, 4, 23, 42, 16, 15]) | mergesort(left)

Note that each time a new call to mergesort is made, the execution must again make a call to mergesort(left). Once
the base case is reached, the algorithm backtracks and calls mergesort(right).

|            Call Stack             | Last Execution|
|:---------------------------------:|:---:|
| mergesort([23])
|        mergesort([4, 23])         |mergesort(right)
|       mergesort([8, 4, 23])       | mergesort(right)
| mergesort([8, 4, 23, 42, 16, 15]) | mergesort(left)

Finally, the call to mergesort([4, 23]) has exhausted all mergesort(left) and mergesort(right) calls that it can
make. This function resumes and executes merge() on the function's values for left, right, and lst (recall that this
is the order of arguments to any merge() call).

|            Call Stack             | Last Execution|
|:---------------------------------:|:---:|
| merge([4], [23], [4, 23])
|        mergesort([4, 23])         |merge()
|       mergesort([8, 4, 23])       | mergesort(right)
| mergesort([8, 4, 23, 42, 16, 15]) | mergesort(left)

The merge function sorts the two values that it's given. In this case, the values happened to already be in sorted
order. The top function calls return, and mergesort([8, 4, 23]) makes its merge call.

|            Call Stack             | Last Execution|
|:---------------------------------:|:---:|
|  merge([8], [4, 23], [8, 4, 23])  |
|       mergesort([8, 4, 23])       | merge()
| mergesort([8, 4, 23, 42, 16, 15]) | mergesort(left)

At the conclusion of this call, the first half of the list is sorted. The recursion unwinds back to the original
list, and the whole process repeats on the right half as follows:

|            Call Stack             | Last Execution|
|:---------------------------------:|:---:|
|          mergesort([42])          |
|      mergesort([42, 16, 15])      | mergesort(left)
| mergesort([8, 4, 23, 42, 16, 15]) | mergesort(right)

|            Call Stack             | Last Execution|
|:---------------------------------:|:---:|
| mergesort([16])   |
|        mergesort([16, 15])        | mergesort(left)
|      mergesort([42, 16, 15])      | mergesort(right)
| mergesort([8, 4, 23, 42, 16, 15]) | mergesort(right)

|            Call Stack             | Last Execution|
|:---------------------------------:|:---:|
|          mergesort([15])          |
|        mergesort([16, 15])        | mergesort(right)
|      mergesort([42, 16, 15])      | mergesort(right)
| mergesort([8, 4, 23, 42, 16, 15]) | mergesort(right)

|            Call Stack             | Last Execution|
|:---------------------------------:|:---:|
|    merge([16], [15], [16, 15])    |
|        mergesort([16, 15])        | merge()
|      mergesort([42, 16, 15])      | mergesort(right)
| mergesort([8, 4, 23, 42, 16, 15]) | mergesort(right)

|             Call Stack              | Last Execution|
|:-----------------------------------:|:---:|
| merge([42], [15, 16], [42, 16, 15]) |
|       mergesort([42, 16, 15])       | merge()
|  mergesort([8, 4, 23, 42, 16, 15])  | mergesort(right)

After the top calls return, both halves are sorted, and the final merge call integrates them into the full sorted list:

|              Call Stack               | Last Execution|
|:-------------------------------------:|:---:|
| mergesort([4, 8, 23], [15, 16, 42], [8, 4, 23, 42, 16, 15]) | merge()
|   mergesort([8, 4, 23, 42, 16, 15])   | merge()

The final output is: [4, 8, 15, 16, 23, 42]

Try it for yourself and see! And for insights into the order of the recursive calls, merge steps, and variable values,
you can always
include the following print statements at the beginning of the merge function:

```
print(f'left: {left}')
print(f'right: {right}')
print(f'lst: {lst}')
```
This will reveal what’s going on under the hood :)

