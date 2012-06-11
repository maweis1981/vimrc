"""
Sortable table, sort by headers, alphanumeric or numeric, automatically detect column data type.
"""

from vim import *
from time import *
import re, sys
from os.path import expanduser, join as pjoin
from string import join
sys.path.append(expanduser("~/scripts/"))

class Sort:
    def cmp1(self, a, b):
        """Compare two items, used by sort, can compare numbers or alphanumeric. Note: see
        todo_sort.py for an example of sorting by date."""
        a, b = a[self.index], b[self.index]
        if self.sortmode[self.index] == 0:
            a, b = float(a), float(b)

        elif self.sortmode[self.index] == 2:
            try:
                a = strptime(a, "%a %b %d")
                b = strptime(b, "%a %b %d")
            except:
                pass
        return cmp(a, b)

    def sort(self):
        pos = current.window.cursor
        b = current.buffer
        self.index = 0

        # find out what to sort by
        headers = [fld.strip() for fld in re.split("\s\s+", b[0])]
        ncols = len(headers)
        cword = eval("expand('<cword>')")     # word under cursor
        if cword in headers:
            self.index = headers.index(cword)

        # parse the data
        rows = []
        maxl = [2]*ncols
        self.sortmode = [0]*ncols
        skipped = []
        for l in b[2:]:
            if l.strip():
                flds = [fld.strip() for fld in re.split("\s\s+", l)]
                if len(flds) != ncols:
                    print "Wrong num. of columns, skipping line: %s" % l
                    skipped.append(l)
                    continue
                for n, fld in enumerate(flds):
                    if len(fld) > maxl[n]:
                        maxl[n] = len(fld)
                    if not (re.match("^[0-9.]+$", fld) and fld != '.'):
                        self.sortmode[n] = 1
                rows.append(flds)

        maxl = [x+3 for x in maxl]
        rows.sort(cmp=self.cmp1)

        # make line template, insert headers, rows
        fldtpl = ''
        total = 0
        for ml in maxl:
            total += ml
            fldtpl += "%%-%ds" % ml

        total -= 3
        r = [fldtpl % tuple(t) for t in rows]
        hr = fldtpl % tuple(headers)

        del b[:]
        out = [hr.strip(), '-'*total] + [r.strip() for r in r]
        if skipped: out += ['',''] + skipped
        b[0:0] = out

        current.window.cursor = pos     # restore cursor


if __name__ == '__main__':
    Sort().sort()
