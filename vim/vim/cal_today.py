"""Mark today and clear mark from previous highlight."""

from vim import *
from time import *
from datetime import date


def search(pat, d=''):
    """Search for pattern. d='b' to search backwards, returns 0 if not found."""
    if d: d = ", '%s'" % d
    return int(eval("search('%s'%s)" % (pat, d)))

def normal(cmd):
    command("normal " + cmd)

def today():
    t = date.today()
    month = strftime("%B %Y", t.timetuple())
    command("normal gg")

    # remove old hl
    # need to match: "| [ 12 ]" OR "| [ 12*]"
    # pseudo-pattern: | [ \d{1,2} *{1,2} [ ]{1,2}]
    s = search("| \[ \d\{1,2}\*\{0,1}[ ]\{0,1}\]")
    if s:
        normal("2lxxf]r a  ")  # cmd: 2l xx f] r<space> a<space><space>
        normal("gg")

    # add new hl
    search(month)
    day = t.timetuple()[2]
    for x in range(8):
        search("-"*14)
        normal("j")
        s = search(r"| %s\*\{0,1} " % str(day))
        if s: break

    # some plugin (autoclose?) does not allow closing [] with R cmd

    mv = 4
    if day > 10: mv = 5

    normal("2li  ")             # cmd: 2l i<space><space>
    normal("hr[%dlr]lxxb" % mv)     # cmd: h r[ 5l r] l xx b

if __name__ == '__main__':
    today()
