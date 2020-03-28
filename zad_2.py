def main():
    lista = list(range(20))
    lista_co_trzeci = lista[2::3]
    lista_odwrocona = lista[::-1]
    lista_co_drugi_od_konca = lista[len(lista)-2:1:-2]
    print('Lista: {}'.format(lista))
    print('A (co trzeci element): {}'.format(lista_co_trzeci))
    print('B (odwrócona lista): {}'.format(lista_odwrocona))
    print('C (co drugi od końca): {}'.format(lista_co_drugi_od_konca))


if __name__ == '__main__':
    main()
