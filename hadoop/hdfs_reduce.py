# coding = utf-8

import sys
from operator import itemgetter
from itertools import groupby


def read_mapper_output(file, sep="\t"):
    for line in file:
        yield line.rstrip().split(sep, 1)


def main():
    data = read_mapper_output(sys.stdin)

    for current_word, group in groupby(data, itemgetter(0)):
        total_count = sum(int(count) for current_word, count in group)

        print("%s%s%d" % (current_word, '\t', total_count))


if __name__ == '__main__':
    main()