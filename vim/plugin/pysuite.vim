" PySuite - collection of Vim plugins written in Python
" version: 0.3.0
"
" functions:
 " DoAlignCode(...) - Align equal signs or comments in code
 " Resize(dir)      - Resize vim main window, see .py for size list
 " DoSort()         - sortable table
 " SortableHelp()   - sortable table help
 " HelpGrep()       - helpgrep given words in any order
 " Pdocfold()       - fold docstrings and comments
 " PyStripDoc()     - copy buffer with stripped docstrings and comments
 " SearchCode()     - Search in code only, skipping strings and python-style comments
"

if exists("g:pysuite_loaded")
    finish
endif

let g:pysuite_loaded = 1
let g:pysuite_tabbar = 1    " set when using pysuite with tabbar; used in proj_open.py


command! -nargs=? AlignCode call DoAlignCode(<q-args>)
nnoremap <Leader>hg :call HelpGrep()<cr>
nnoremap <Leader>df :call Pdocfold()<cr>
nnoremap <Leader>sd :call PyStripDoc()<cr>
nnoremap \f :call SearchCode()<cr>
nnoremap <Leader>n :call SearchCode(1)<cr>

:au BufNewFile,BufRead,BufEnter *.ts nnoremap <buffer> <cr> :call DoSort()<CR>
:au BufNewFile,BufRead,BufEnter *.ts nnoremap <buffer> ? :call SortableHelp()<CR>

" Tip: these are much handier with ctrl-key mapping
nnoremap <Leader>- :call Resize(0)<CR>
nnoremap <Leader>+ :call Resize(1)<CR>


function! DoAlignCode(...)
    :pyfile ~/.vim/python/aligncode.py
endfu

function! Resize(dir)
    :pyfile ~/.vim/python/resize.py
endfu

function! HelpGrep()
    :pyfile ~/.vim/python/helpgrep.py
endfu

function! Pdocfold()
    :pyfile ~/.vim/python/pydocfold.py
endfu

function! PyStripDoc()
    :pyfile ~/.vim/python/pystripdoc.py
endfu

function! SearchCode(...)
    :pyfile /home/ak/.vim/python/searchcode.py
endfu


function! NextWin()     " Next window, skipping tabbar
    exe "normal \<c-w>w"
    let n = 12      " break loop if project and tabbar are the only windows

    while n > 0 && (bufname("%") == "-TabBar-" || bufname("%") =~ '.*\.proj')
        exe "normal \<c-w>w"
        let n -= 1
    endwhile
endfu

function! DoSort()
    :pyfile ~/.vim/python/sortable.py
endfu

function! SortableHelp()
    echo " Move to the header you want to sort by and hit Enter\n"
    echo " Hit enter anywhere to sort by 1st column and to refresh layout\n"
    echo " Fields are separated by two or more spaces. Fields can not be empty\n"
    echo " Help: ?\n\n"
endfu

function! DoSum()
python <<
txt = vim.eval('@"')
try: print "Sum:", sum([float(x.strip(",;")) for x in txt.split()])
except: print "DoSum: error parsing numbers:", txt
.
endfu
vnoremap <Leader>s y:call DoSum()<CR>
command! Sum call DoSum()

