"""Fold python comments and strings."""
import re
from vim import *

def pydocfold():
    cur = 0
    b = current.buffer
    end = len(b)
    startfold = comment = False
    command("set foldmethod=manual")
    command("set fml=0")
    for cur in range(end):
        l = b[cur].strip()
        lst = l.startswith
        lend = l.endswith
        if comment and not lst("#"):
            # close comments fold
            command("%s,%sfold" % (startfold, cur))
            startfold = comment = False
            continue

        if startfold != False and lend('"""'):
            # close multiline fold
            command("%s,%sfold" % (startfold, cur+1))
            startfold = False
            continue

        if lst('"""') and not re.match('^""".*"""$', l) and startfold == False:
            # start multiline fold
            startfold = cur+1

        if not comment and lst("#"):
            # start comment fold
            comment = True
            startfold = cur+1

        # single line dosctrings
        if startfold == False:
            if lst('"') and lend('"') and not lend('"""'):
                # dbl quote docstring
                command("%sfold" % (cur+1))
            if (lst("'") and lend("'")) or (lst('"""') and lend('"""') and l != '"""'):
                # single quote or triple quote docstring
                command("%sfold" % (cur+1))

if __name__ == "__main__":
    pydocfold()
