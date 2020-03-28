def generuj_fibonacciego(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def main():
    fibonacci = list(generuj_fibonacciego(10))
    print(fibonacci)


if __name__ == '__main__':
    main()
