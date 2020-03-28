from random import randint


def unique_elements(seq):
    buf = set()
    for el in seq:
        if el in buf:
            pass
        else:
            buf.add(el)
    seq.clear()
    for i in buf:
        seq.append(i)
    return(seq)


def main():
    lista = []
    for i in range(30):
        lista.append(randint(1, 20))
    print("[1] Zawartość listy pierwotnej: ")
    print(lista)
    print("[2] Zawartość listy po usunięiu duplikatów: ")
    print(unique_elements(lista))


if __name__ == '__main__':
    main()
