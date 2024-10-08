# Implementation of Quickstart
def quickSort(arr: List[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr 

    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1

    arr[e] = arr[left]
    arr[left] = pivot

    quickSort(arr, s, left - 1)
    quickSort(arr, left + 1, e)

    return arr 
