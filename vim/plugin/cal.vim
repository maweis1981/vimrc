" Cal - a calendar plugin for vim
"

if exists("g:py_cal_loaded")
    finish
endif

let g:py_cal_loaded = 1


""" Maps

:au BufNewFile,BufRead,BufEnter *.cal   nnoremap <buffer> <CR>      :call PyCal("entry")<CR>
:au BufNewFile,BufRead,BufEnter *.cal   nnoremap <buffer> <Leader>b :call PyCal("back")<CR>
:au BufNewFile,BufRead,BufEnter *.cal   nnoremap <buffer> <Leader>n :call PyCal("add_month")<CR>
:au BufNewFile,BufRead,BufEnter *.cal   nnoremap <buffer> <Leader>t :call PyCal("today")<CR>
:au BufNewFile,BufRead,BufEnter *.cal   nnoremap <buffer> <Leader>h :call CalHelp()<CR>
:au BufRead *.cal :call PyCal("today")

let g:py_cal_width = 98


function! PyCal(...)
    :pyfile ~/.vim/python/cal.py
endfu

function! CalHelp()
    echo " Add New Month           ".g:mapleader."n\n"
    echo " Add New Entry            Enter (on day in month view)\n"
    echo " Jump Back to month view ".g:mapleader."b\n\n"
    echo " Jump to today           ".g:mapleader."t\n"
    echo " Help                    ".g:mapleader."h\n"
endfu
