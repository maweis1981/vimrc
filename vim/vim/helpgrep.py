"""Helpgrep given words in any order; empty input repeats last search."""

from vim import *
from string import join

def exists(var):
    return int(eval("exists('%s')" % var))

def helpgrep():
    command("call inputsave()")     # avoid problems with vim's typeahead mechanism
    pat = eval("input('HelpGrep> ')")
    command("call inputrestore()")
    if not pat:
        if exists("s:pat"): pat = eval("s:pat")
        else: return

    command("let s:pat='%s'" % pat)
    words = [".*%s.*" % w for w in pat.split()]
    command(":helpgrep %s" % join(words, "\&"))

if __name__ == "__main__":
    helpgrep()
