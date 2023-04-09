def BinarySearch(arr, StartingIndex, EndingIndex, Num):
    if EndingIndex >= StartingIndex:
        mid = StartingIndex + (EndingIndex - StartingIndex) // 2

        if arr[mid] == Num:
            return mid

        elif arr[mid] > Num:
            return BinarySearch(arr, StartingIndex, mid - 1, Num)

        else:
            return BinarySearch(arr, mid + 1, EndingIndex, Num)

    else:
        return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Number = int(input("Enter The Number\n"))
print("The Number ", Number, " Is Present At : ", BinarySearch(array, 0, len(array) - 1, Number))
