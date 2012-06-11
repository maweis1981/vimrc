""" Add a new todo item. """
from vim import *
from time import *
from string import join

def newtodo():
    b = current.buffer

    # default line template or reuse one from sort(), to keep alignment
    fldtpl = " %-25s%-10s%-10s%-6s%-6s%-8s%s"
    if int(eval("exists('s:fldtpl')")):
        fldtpl = eval("s:fldtpl")

    # insert header and divider
    flds = tuple(eval("s:headers").split())
    if not b[0].startswith(' ' + flds[0]):
        b[0:0] = [fldtpl % flds, '-'*76]

    # insert new task with default values
    lnum = current.window.cursor[0] - 1
    if lnum < 2: lnum = 2
    start = asctime().split()[:3]
    flds = ("Task", '', '1', '1', '0', "No", join(start))
    b[lnum:lnum] = [fldtpl % flds]

    current.window.cursor = (lnum+1, 0)

if __name__ == '__main__':
    newtodo()
