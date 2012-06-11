" Fin - very basic plugin to track finances
"

if exists("g:py_fin_loaded")
    finish
endif
let g:py_fin_loaded = 1

" Maps

:au BufNewFile,BufRead,BufEnter *.fin   nnoremap <buffer> <CR>      :call PyFin("new")<CR>k$R
:au BufNewFile,BufRead,BufEnter *.fin   nnoremap <buffer> U         :call PyFin("update")<CR>
:au BufNewFile,BufRead,BufEnter *.fin   nnoremap <buffer> <Leader>i :call PyFin("init")<CR>
:au BufNewFile,BufRead,BufEnter *.fin   nnoremap <buffer> <Leader>h :call FinHelp()<CR>
:au BufRead *.fin :call PyFin("update")


function! PyFin(...)
    :pyfile ~/.vim/python/fin.py
endfu

function! FinHelp()
    echo " New                   Enter\n"
    echo " Update totals         U\n"
    echo " Initialize new file  ".g:mapleader."i\n"
    echo " Help                 ".g:mapleader."h\n"
endfu
