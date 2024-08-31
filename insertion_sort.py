def main():
    print(insertion_sort([2, 3, 1, 65, 2, 1, 9, 7, 3, 4]))
    print(insertion_sort([2, 3]))
    print(insertion_sort([2]))
    print(insertion_sort([]))

    print(insertion_sort(
        [2, 3, 1, 65, 2, 1, 9, 7, 3, 4, -12, -12, 0, -121212]))


def insertion_sort(data):
    # If data is empty or data has only 1 element, it's already sorted
    if not data or len(data) == 1:
        return data
    for i in range(1, len(data)):
        key = data[i]
        for j in range(i - 1, -1, -1):
            if key < data[j]:
                break
            elif key > data[j]:
                data[j], data[j + 1] = key, data[j]
    return data


if __name__ == "__main__":
    main()
