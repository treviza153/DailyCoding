def maxList(num, arr):
    return [max(arr[i:num+i]) for i, _ in enumerate(arr)
            if i + num <= len(arr)]


if __name__ == '__main__':
    num = 5
    array = [10, 5, 2, 7, 8, 7]

    result = maxList(num, array)
    print(result)
