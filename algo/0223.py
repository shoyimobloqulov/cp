def is_ap(arr):
    if len(arr) < 2:
        return True

    d = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != d:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

if is_ap(a):
    print("yes")
else:
    print("no")
