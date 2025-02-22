def main():
    N = int(input())
    x, y = [int(x) for x in input().split()]

    answer = 4 - sum([(x == 1), (x == N), (y == 1), (y == N)])
    print(answer)


if __name__ == '__main__':
    main()