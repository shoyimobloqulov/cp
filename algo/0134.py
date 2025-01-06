def main():
    n, m = map(int, input().split())

    mat = []
    for _ in range(n):
        r = list(map(int, input().split()))
        mat.append(r)

    nr = list(map(int, input().split()))
    mat.append(nr)

    mat.sort(key=lambda x: x[0], reverse=True)

    for r in mat:
        print(' '.join(map(str, r)))

if __name__ == "__main__":
    main()
