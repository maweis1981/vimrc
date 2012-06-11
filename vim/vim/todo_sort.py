"""
Sort todo item list. By default, sorting is by priority, to sort by a different header,
cursor should be positioned on the header and sort command activated.
"""

from vim import *
from time import *
import re, sys
from os.path import expanduser, join as pjoin
from string import join
from copy import deepcopy
sys.path.append(expanduser("~/scripts/"))

leftmargin = 1

class Sort:
    def cmp1(self, a, b):
        """Compare two items, used by sort, can compare numbers, alphanumeric or dates."""
        a, b = a[self.index], b[self.index]
        if self.index in (2,3,4):
            a, b = int(a), int(b)
        elif self.index == 6:
            try:
                a = strptime(a, "%a %b %d")
                b = strptime(b, "%a %b %d")
            except:
                pass
        return cmp(a, b)

    def sort(self):
        # find out what to sort by
        headers = tuple(eval("s:headers").split())
        self.index = 2                        # header to sort by
        cword = eval("expand('<cword>')")     # word under cursor
        pos = current.window.cursor
        b = current.buffer
        if cword in headers:
            self.index = headers.index(cword)

        # parse the task list
        tasks = []
        maxl1 = 4; maxl2 = 7    # task and project name max widths
        for l in b[2:]:
            if l.strip():
                flds = [fld.strip() for fld in re.split("\s\s+", l)]
                if len(flds) not in (6,7):
                    print "Error: wrong number of fields in line: %s" % l
                    return
                if len(flds) == 6: flds.insert(1, '')   # no project
                if len(flds[0]) > maxl1: maxl1 = len(flds[0])
                if len(flds[1]) > maxl2: maxl2 = len(flds[1])
                tasks.append(flds)
        maxl1 += 3; maxl2 += 2

        # separate Done, OnHold and sort the rest
        done = [t for t in tasks if t[4] == "100"]
        onhold = [t for t in tasks if t[5].lower() == "yes" and t[4] != "100"]
        tasks = [t for t in tasks if t[4] != "100" and t[5].lower() != "yes"]

        # sort in asc order; if was sorted, sort in desc order
        was_sorted = True
        for t in (done, onhold, tasks):
            original = deepcopy(t)
            t.sort(cmp=self.cmp1)
            if t != original: was_sorted = False

        if was_sorted:
            for t in (done, onhold, tasks):
                t.sort(cmp=self.cmp1, reverse=True)

        # make line template, insert headers, tasks, OnHold and Done
        divlen = maxl1 + maxl2 + 40 + leftmargin     # divider line
        del b[:]
        fldtpl = ' '* leftmargin + "%%-%ds%%-%ds" % (maxl1, maxl2) + "%-10s%-6s%-6s%-8s%s"
        b[0:0] = ([fldtpl % headers, '-'*divlen] +
                  [fldtpl % tuple(t) for t in tasks] + [''] +
                  [fldtpl % tuple(t) for t in onhold] + [''] +
                  [fldtpl % tuple(t) for t in done])

        # save line template to use when adding new tasks (to keep alignment)
        command("let s:fldtpl='%s'" % fldtpl)
        current.window.cursor = pos     # restore cursor


if __name__ == '__main__':
    Sort().sort()
