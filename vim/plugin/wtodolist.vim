" WTodo - todo plugin for vim written in Python
"

" Maps
"

if exists("g:wtodo_loaded")
    finish
endif

let g:wtodo_loaded = 1

nnoremap _T :call WTodo("open")<CR>

:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> N :call WTodo("new")<CR>0 R
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> <Tab> :call WTodo("new")<CR>0 R
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> <space> :call WtodoDone()<CR>
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> H :call WTodo("toggle_onhold")<CR>
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> <cr> :call WTodo("sort")<CR>
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> ? :call TodoHelp()<CR>
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> C :call WTodo("change_name")<CR>0 R
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> A :call WTodo("show_active")<CR>
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> <M-j> :m+<CR>
:au BufNewFile,BufRead,BufEnter *.todo nnoremap <buffer> <M-k> :m-2<CR>
:au BufRead *.todo :call WTodo("sort")


let s:headers='Name Project Priority Diff Done OnHold Started'


function! WTodo(...)
    :pyfile ~/.vim/python/wtodo.py
endfu

function! WtodoDone()    " Mark task as done, i.e. set 'Complete' to 100
    normal $F 4BR100
    normal 0
endfu

function! TodoHelp()
    " Help listing
    echo " WTodo commands:      \n\n"
    echo " New                  Tab or N\n"
    echo " Done                 Space\n"
    echo " Toggle OnHold        H\n"
    echo " Sort                 Enter\n"
    echo " Change name          C\n"
    echo " Show active tasks    A\n"
    echo " Move tasks           Alt-j/k\n\n"

    echo " Help                 ?\n\n"
    echo "When todo win is hidden, use '_T' to open and resize it to show active tasks"
endfu
