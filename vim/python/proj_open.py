"""Open or run one file."""
from vim import *
from os.path import expanduser, join as pjoin
from os import sep

programs = {"py": "python", "sh": "bash", "html": "firefox"}


def openfile():
    name, b = current.line.strip(), current.buffer
    lnum = current.window.cursor[0]
    headpath = eval("expand('%:h')")

    # open a directory?
    if name and (name[0] in '~'+sep or name.endswith(sep)):
        if name[0] not in '~'+sep:
            # relative path
            name = pjoin(headpath, name)
        command("call NextWin()")
        command("e %s" % name)
        return

    # run file?
    run = False
    if int(eval("exists('a:1')")) and eval("a:1") == "run":
        run = True

    # search upwards for directory and open or run file
    while 1:
        if not lnum: return
        lnum -= 1
        l = b[lnum].strip()
        if l and (l[0] in '~'+sep or l.endswith(sep)):

            if l[0] not in '~'+sep:
                # relative path
                l = pjoin(headpath, l)

            ext = name.split('.')[-1]
            if ext in programs and run:
                command(":!%s %s" % (programs[ext], pjoin(l, name)))
            else:
                command(':call NextWin()')
                command(":e %s" % pjoin(l, name))
            return

if __name__ == '__main__':
    openfile()
