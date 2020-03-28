from functools import wraps
import inspect


def dekorator(funkcja):
    @wraps(funkcja)
    def wrapper(*args, **kwargs):
        funkcja_args = inspect.signature(funkcja).bind(*args, **kwargs).arguments
        funkcja_args_str = ', '.join('{} = {!r}'.format(*item) for item in funkcja_args.items())
        print('-'*30)
        print('Func: {} | Args: {}'.format(funkcja.__qualname__, funkcja_args_str))
        print('-'*30)
        return funkcja(*args, **kwargs)
    return wrapper


@dekorator
def funkcja_a(n):
    return(n)


@dekorator
def funkcja_b(n):
    return n**n


def main():
    print(funkcja_a(8))
    print(funkcja_b(9))


if __name__ == '__main__':
    main()
