def print_room(height, width):
    top_and_bottom = "*" + ("_" * width) + "*"
    inner_walls = "|" + ("." * width) + "|"
    print(top_and_bottom)
    for i in range(0, height):
        print(inner_walls)
    print(top_and_bottom)


def main():

    height = int(input("Give height: "))
    width = int(input("Give width: "))
    print_room(height, width)


if __name__ == '__main__':
    main()
