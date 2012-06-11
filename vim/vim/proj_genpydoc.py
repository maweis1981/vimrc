"""Generate docs file for all python files in a project or dir, depending on where cursor is."""
# vim: set fileencoding=utf-8 :

from vim import *
import os, sys, re
from os.path import expanduser
from inspect import *
from string import join
sys.path.append(expanduser("~/.vim/python/"))
import proj_openall

browser = "firefox"
outfn = "%s-out.html"
htmltpl = """<html><head><title>%s</title>
    <style type="text/css">
        h4 { color: #679; background: #f5f5f5; padding: 7px; border-top: 1px solid #ccc; }
        p { color: #666; display: inline; }
        #def { color: #76a; margin-bottom: 3px; }
        #main { width: 960px; border: 1px solid #aaa; margin: 30px; padding: 15px; }
        #cen { text-align: center; }
        h3 { text-align: center; color: #679; }
    </style>
    </head>
    <body> <h3>%s</h3>
    <div id="main">%s</div></body></html>
"""


def genpydoc():
    """Generate docs."""
    html = potl = False
    if int(eval("exists('a:1')")):
        if eval("a:1") == "html":
            html = True
        elif eval("a:1") == "potl":
            potl = True

    filelst = [f for f in proj_openall.filelist() if f.endswith(".py")]

    # get project or dir name
    pname = "Project"
    l = current.line
    if l.strip():
        if l.startswith("---"):
            pname = l.strip("- ").capitalize()
        else:
            l = l.strip(' '+os.sep)
            pname = l.split(os.sep)[-1].capitalize()

    out = []
    for fn in filelst:
        # import module
        path = expanduser(fn).split(sep)
        path, fname = join(path[:-1], sep), path[-1]
        sys.path.append(path)
        m = __import__(fname.split('.')[0])
        reload(m)   # if file was changed, it's not autoreloaded even if function is rerun
        memb = getmembers(m)

        # make a list of class / def names
        src = open(expanduser(fn)).read()
        lst = re.findall(r"\n\s*(class|def) ([a-zA-Z0-9_]+)(:|\()", src)
        lst = [x[1] for x in lst]

        # filename and docstring
        if html:
            out.extend( ["<h4>%s</h4>" % fname, ''] )
        elif potl:
            out.extend( ['· '+fn] )
        else:
            out.append('#'*78)
            out.extend( ['# '+fn, ''] )
        mdoc = getdoc(m).split('\n')

        if html:
            if len(mdoc) == 1: out.extend( ['<p>%s</p>' % mdoc[0],  "<br /><br />"] )
            else: out.extend(["<br/><p>"] + [join(mdoc, "<br/>")] + ["</p><br/>", "<br/><br/>"])
        elif potl:
            if len(mdoc) == 1:
                out.extend( [' '*4 + '"""%s"""' % mdoc[0]] )
            else:
                quote = [' '*4 + '"""']
                out.extend(quote + [' '*4 + ln for ln in mdoc] + quote)
        else:
            if len(mdoc) == 1: out.extend( ['"""%s"""' % mdoc[0],  ''] )
            else: out.extend( ['"""'] + mdoc + ['"""', ''] )

        # output each class and def and their docstrings
        last = None
        for item in lst:
            if hasattr(m, item):
                item = getattr(m, item)
                last = item
            else:
                item = getattr(last, item)

            cls_def = getsourcelines(item)[0][0]
            indent = cls_def.index(cls_def.lstrip())
            if html: indentsp = '&nbsp;'*indent
            else: indentsp = ' '*(indent+4)

            # does not support multiline defs but they are bad style?
            if html:
                out.append("%s<div id='def'>%s</div>" % (indentsp, cls_def))
                indentsp = '&nbsp;'*(indent+4)*2
            elif potl:
                out.append(' '*4 + '· ' + cls_def)
            else:
                out.append(cls_def)

            # output docstring with indentation
            idoc = getdoc(item)
            if idoc:
                idoc = idoc.split('\n')
                if html:
                    if len(idoc) == 1:
                        out.append('%s<p>%s</p><br />' % (indentsp, idoc[0]))
                    else:
                        idoc = [indentsp + l for l in idoc]
                        quote = ['%s<br />' % indentsp]
                        out.extend(quote +  ["<p>%s</p><br />" % join(idoc)] + quote)
                else:
                    if potl: indentsp += ' '*4
                    if len(idoc) == 1:
                        out.append('%s"""%s"""' % (indentsp, idoc[0]))
                    else:
                        idoc = [indentsp + l for l in idoc]
                        quote = ['%s"""' % indentsp]
                        out.extend(quote + idoc + quote)

            if html: out.append("<br />")
            elif not potl: out.append('')

        if potl:
            pass
        elif not html:
            out.extend(['', ''])

    if not out: return

    if html:
        fp = open(outfn % pname, 'w')
        fp.write(htmltpl % (pname, pname, join(out, '\n')))
        fp.close()
        os.system("%s %s" % (browser, outfn % pname))
    else:
        # go to main window area, create new buffer, write output, set filetype
        command("call NextWin()")
        command("new")
        current.buffer[:] = out
        command("normal gg")
        if potl:
            command("set ft=potl bt=nofile")
        else:
            command("set ft=python bt=nofile")


if __name__ == '__main__':
    genpydoc()
