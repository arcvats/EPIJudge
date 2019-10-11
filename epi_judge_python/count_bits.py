from test_framework import generic_test


def count_bits(x):
    # TODO - you fill in here.
    counter = 0
    while x:
        counter += x & 1
        x >>= 1
    return counter


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
