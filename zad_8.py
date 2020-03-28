from functools import wraps


def licznik(funkcja, count=[0]):
    @wraps(funkcja)
    def increase_count(*args, **kwargs):
        count[0] += 1
        print('Wywołanie funkcji nr: {}'.format(count[0]))
        return funkcja(*args, **kwargs)
    return increase_count


@licznik
def funkcja_a(n):
    return(n)


def main():
    print(funkcja_a(8))
    print(funkcja_a(9))


if __name__ == '__main__':
    main()
