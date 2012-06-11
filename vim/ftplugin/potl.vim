function! PotlCloseFold()
    let closed = foldclosed('.') > 0
    if (!closed)
        normal zc
    endif
    return closed
endfunction


function! PotlPromote(dir)
    set lz
    let closed = PotlCloseFold()
    if a:dir == 1
        normal >>
    else
        normal <<
    endif
    if (!closed)
        normal zo
    endif
    set nolz
endfunction



function! NewHeader()
python <<
from vim import *
from time import sleep
def new_header():
    lnum = current.window.cursor[0]
    command("call search('·', 'b')")
    lnum2, ind = current.window.cursor
    if lnum2 != lnum:
        command("exe 'normal \\<c-o>'")     # jump back to original line
    else:
        command("normal j")
    b = current.buffer
    b[lnum:lnum] = [' '*ind + '·']          # add new line with indent and bullet
    current.window.cursor = (lnum+1, 0)

new_header()
.
endfunction


function! PotlHelp()
    " Help listing
    echo " New                   ".g:mapleader."n\n"
    echo " Foldlevel             ".g:mapleader."z<N>\n"
    echo " Promote section       ".g:mapleader.">\n"
    echo " Demote section        ".g:mapleader."<\n"
    echo " Close one fold level  -\n"
    echo " Open one fold level   =\n"

    echo " Help                  ".g:mapleader."h\n"
endfu


" Make a more outline-friendly fold view.
function! PotlFoldText()
    let l = getline(v:foldstart)
    let line = substitute(l, '^[ ]*', '', '')
    let prefix = repeat(' ', (strlen(l) - strlen(line)))
    return prefix . line
endfunction


function! PotlFoldLevel(n)
    let l = getline(a:n)
    if (l == '') | return '=' | endif

    let level = matchend(l, '^[ ]*') / 4

    " Recognize header lines, which start with optional spaces and a '·'
    if (l =~ '^[ ]*·')
        return '>' . (level + 1)
    else
        return '='
    endif
endfunction


