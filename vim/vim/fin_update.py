"""Update totals for all columns."""

from vim import *
import re

def fin_update():
    b = current.buffer
    headers = re.split("\s\s+", b[0])
    ncols = len(headers) - 2
    maxlen = [len(h)+7 for h in headers[:-2]]

    initline = re.split("\s\s+", b[2])
    totals = [float(x) for x in initline[:ncols]]

    # loop through lines and add up totals
    lines = []
    for l in b[3:]:
        if l.startswith("-----"):
            break
        elif l.strip():
            flds = [fld.strip() for fld in re.split("\s\s+", l)]
            if len(flds) not in (ncols+2, ncols+1):
                print "Error: wrong number of fields in line: %s" % l
                return
            newflds = [0]*ncols
            for n, x in enumerate(flds[:ncols]):
                totals[n] += float(x)
                x = "%0.2f" % float(x)
                x = x.rstrip('0').rstrip('.')   # can't do both at the same time!!
                newflds[n] = x or '0'
            lines.append(newflds + flds[-2:])
        else:
            lines.append('')

    # make line template
    fldtpl = amtline_tpl = ''
    for x in maxlen:
        fldtpl += "%%-%ds" % x
        amtline_tpl += "%%-%ds" % x

    fldtpl += "%-16s%s"
    amtline_tpl += "%-16s%s"

    # make list of header, divider and rest of lines
    divlen = 78
    lst = ([fldtpl % tuple(headers), '-'*divlen] + [fldtpl % tuple(initline)])
    for l in lines:
        if l: l = amtline_tpl % tuple(l)

        lst.append(l)

    # make totals line and insert into buffer
    totals = amtline_tpl % tuple(totals + ['', ''])
    del b[:]
    b[0:0] = lst + ['-'*divlen, totals.strip()]
    command("normal G")
    # from time import sleep; sleep(1)
    command("normal zb")
    command("let s:fin_fldtpl='%s'" % fldtpl)


if __name__ == '__main__':
    fin_update()
