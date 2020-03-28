def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if(number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


def main():
    lista = list(range(2, 100))
    print('\nWyszukiwanie liczb pierwszych')
    print('\nA (Za pomocą map, filter- mój pomysł (odwołanie do funkcji)): ')
    print(list(map(
            lambda arg: arg,
            filter(lambda arg: is_prime(arg), lista)
        )))
    print('\nA (cwana wersja ze stackoverflow (tak chciałem to zrobić początkowo, ale nie mogłem zrobić pętli)):')
    print(list(map(
            lambda arg: arg,
            filter(lambda x: all(x % y != 0 for y in range(2, x)), lista)
        )))
    print('\nB (za pomocą list comprehension):')
    print([x for x in lista if all(x % y != 0 for y in range(2, x))])


if __name__ == '__main__':
    main()
