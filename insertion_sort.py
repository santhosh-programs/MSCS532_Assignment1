def main():
    print(insertion_sort([2, 3, 1, 65, 2, 1, 9, 7, 3, 4]))


def insertion_sort(data):
    if not data or len(data) == 1:
        return data
    for i in range(1, len(data)):
        for j in range(i):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    return data


if __name__ == "__main__":
    main()
