"""Resize Vim window."""
from vim import *

sizes = [ # 59 / 66
         (20, 100),
         (35, 100),
         (54, 100),
         (59, 100),
         (59, 133),
         (59, 160),
         (59, 200),
         (59, 245),
]


def set(size):
    command("set lines=%s columns=%s" % size)

def resize():
    l = int(eval("&lines"))
    c = int(eval("&columns"))
    d = eval("a:dir")

    if d == '0':
        # make smaller
        sizes.reverse()
        for ln, col in sizes:
            if ln < l or col < c:
                set((ln, col))
                break
    else:
        # make larger
        for ln, col in sizes:
            if ln > l or col > c:
                set((ln, col))
                break


if __name__ == '__main__':
    resize()
