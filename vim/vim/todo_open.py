"""Open todo window."""
from vim import *

def opentodo():
    sb = int(eval("&splitbelow"))
    command("set splitbelow")
    for b in buffers:
        if b.name and b.name.endswith(".todo"):
            bnr = eval("bufnr('%s')" % b.name)
            if int(eval("buflisted(%s)" % bnr)):
                command("split %s" % b.name)

                # resize window to show all active tasks only
                for n, l in enumerate(current.buffer):
                    if not l.strip():
                        n += 2
                        if n < 6: n = 6
                        command('exe "normal %d\\<c-w>_"' % n)
                        command("normal gg")
                        break
                break
    if not sb:
        command("set nosplitbelow")

if __name__ == '__main__':
    opentodo()
