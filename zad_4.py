def my_sort(seq, priority):
    flag = False

    def f(arg):
        nonlocal flag
        if arg in priority:
            flag = True
            return (1, arg)
        return (0, arg)
    seq.sort(key=f)
    return flag


def main():
    seq = [6, 2, 1, 5]
    print('Lista zawiera wartość z \
priorytetem: {}'.format(my_sort(seq, [1, 2])))
    print(seq)


if __name__ == '__main__':
    main()
