def count_words(file):
    line_list = list()
    word_list = list()
    try:
        with open(file, 'r', encoding='UTF-8') as file:
            for line in file:
                line_list.append(line.split(' '))
        for line in line_list:
            for word in line:
                if word == '':
                    continue
                else:
                    word_list.append(word)
        print('Liczba wyrazów w pliku: {}'.format(len(word_list)))

    except FileNotFoundError:
        print('Plik o nazwie {} nie istnieje!'.format(file))


def main():
    file_to_count_words = 'plik.txt'
    count_words(file_to_count_words)


if __name__ == '__main__':
    main()
