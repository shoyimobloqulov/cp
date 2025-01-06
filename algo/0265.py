def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    queries = list(map(int, data[n+2:]))

    from collections import Counter
    count = Counter(arr)

    result = sum(count[q] if q in count else 0 for q in queries)
    print(result)

if __name__ == "__main__":
    main()
