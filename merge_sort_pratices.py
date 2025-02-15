def merge_sort(array: list[int], left: int, rigth: int) -> list[int]:
    if left >= rigth:
        return

    mid = int((left + rigth) / 2)
    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, rigth)
    sort(array, left, mid, rigth)


def sort(array: list[int], left: int, mid: int, right: int) -> list[int]:
    i = left
    j = mid + 1
    temp = []

    while i <= mid and j <= right:
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1

    while j <= right:
        temp.append(array[j])
        j += 1

    for k in range(len(temp)):
        array[left + k] = temp[k]


def main():
    un_sorted_array = [2, 2, 4, 4] + [2, 2, 2, 4, 4]

    merge_sort(un_sorted_array, 0, len(un_sorted_array) - 1)
    print(un_sorted_array)


main()
