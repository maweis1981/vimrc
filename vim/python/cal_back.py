"""Back to current day in month view (from entries section)."""

from vim import *
from datetime import date


def search(pat, d=''):
    """Search for pattern. d='b' to search backwards, returns 0 if not found."""
    if d: d = ", '%s'" % d
    return int(eval("search('%s'%s)" % (pat, d)))

def back():
    """Jump to or make new entry."""
    if not current.line.startswith("==="):
        search("^===", 'b')

    ttup = strptime(current.line.strip("= "), "%a %B %d, %Y")
    # d = date(*ttup)
    search("^====== %s" % strftime("%B %Y", ttup), 'b')
    search("^====== %s" % strftime("%B %Y", ttup), 'b')

    day = ttup[2]

    for x in range(8):      # 8 not to stuck in a loop but cover 5 possible weeks
        search("-"*14)
        normal("j")
        # s = search(r"| \[\{0,1}[ ]\{0,1}%s\*\{0,1}" % str(day))
        s = search(r"| \(\[ \)\?%s\*\?" % str(day))
        if s: break
    search("\d")


if __name__ == '__main__':
    back()
