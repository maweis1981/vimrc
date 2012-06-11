"""
Searchcode plugin - search in code only, skipping strings and python-style comments

Notes:
 - Search is case insensitive
 - If you hit Enter at prompt, last search is repeated
 - Bug: won't skip some strings, e.g. if a few strings are mixed with code on one line,
   but should be good for docstrings and comments
"""

from vim import *
from re import *
import sys

multiline_dbl_quote = multiline_single_quote = False

def exists(var):
    return int(eval("exists('%s')" % var))

def main():
    # get pattern
    pat = None
    arglen = eval("a:0")                # length of arg list
    if arglen == "0":
        command("call inputsave()")     # avoid problems with vim's typeahead mechanism
        pat = eval("input('/')")
        command("call inputrestore()")
    if not pat:
        if exists("s:pat"):
            pat = eval("s:pat")
        else:
            return
    pat = pat.lower()
    command("let s:pat='%s'" % pat)

    # init vars
    w = current.window
    curline, col = w.cursor
    b = current.buffer
    end = len(b)

    if pat:
        found = iterate(curline, end, w, b, pat)
        if not found:
            found = iterate(0, curline, w, b, pat)
            if not found:
                print "pattern not found:", pat

def st_end_multi(l):
    "Line starts or ends multiline docstring."
    l = l.strip(); lst = l.startswith; lend = l.endswith
    if lst('"""') or lend('"""') or lst("'''") or lend("'''"):
        return True

def dblquotes(l):
    "Double quotes enclosed string."
    if l.find('"') != -1 and l.find('"') < l.find("'"):
        return True

def find(l, pat, quote, w):
    "Find pattern in line, excluding string."
    st, end = l.find(quote), l.rfind(quote)
    # print "st, end: ", st, end
    subl = l[st:end]
    i = subl.find(pat)
    if i != -1:
        if i > st:
            i += end-st
        w.cursor = (cur+1, i)
        return True

def iterate(fr, to, w, b, pat):
    ''' Iterate over lines, search for pattern.

        Handle these cases (and similarly for single quotes):
        """ docstring """
        """
        docstring
        """
        """ docstring
        ... """
        " docstring "

        This one's not handled yet:
        print """
        stuff
        """
    '''
    global multiline_dbl_quote, multiline_single_quote
    for cur in range(fr, to):
        l = b[cur].strip()
        lst = l.startswith
        lend = l.endswith

        # skip lines
        if match('^""".*"""$', l) or match("^'''.*'''$", l):
            continue
        elif lst('"""') and not multiline_dbl_quote:
            multiline_dbl_quote = True
            continue
        elif lst("'''") and not multiline_single_quote:
            multiline_single_quote = True
            continue
        elif multiline_dbl_quote and lend('"""'):
            multiline_dbl_quote = False
            # print "multiline_dbl_quote end"
            continue
        elif multiline_single_quote and lend("'''"):
            multiline_single_quote = False
            continue
        elif lst("#") or (lst('"') and lend('"')) or (lst("'") and lend("'")):
            continue
        elif multiline_dbl_quote or multiline_single_quote:
            continue

        # lines we can search
        l = b[cur].lower()
        if "#" in l:
            l = l.split("#")[0]
        elif "'''" in l or '"""' in l and not st_end_multi(l):
            pass
        elif '"' or "'" in l:
            if dblquotes(l): quote = '"'
            else: quote = "'"
            found = find(l, pat, quote, w)
            if found:
                return True
        i = l.find(pat)
        if i != -1:
            w.cursor = (cur+1, i)
            return True


if __name__ == "__main__":
    main()
