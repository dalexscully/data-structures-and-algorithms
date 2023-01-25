def mergesort(lst):
    n = len(lst)

    if n > 1:
        mid = n//2
        left = lst[0:mid]
        right = lst[mid:]

        # sort the left side
        mergesort(left)
        # sort the right side
        mergesort(right)
        # merge the sorted left and right sides together
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


