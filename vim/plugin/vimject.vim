" Vimject - project plugin for vim, written in Python
"

if exists("g:vimject_loaded")
    finish
endif

let g:vimject_loaded = 1

" Maps
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <cr> :call Vimject("open")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <Leader>l :call Vimject("openall")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> U :call Vimject("unload_all")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <Leader>d :call Vimject("getcwd")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <Leader>L :call Vimject("addall")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <Leader>g :call Vimject("grepall")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <Leader>p :call Vimject("genpydoc")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <Leader>x :call Vimject("open_run")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <Leader>y :call Vimject("genpydoc_html")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> <Leader>o :call Vimject("genpydoc_potl")<CR>
:au BufNewFile,BufRead,BufEnter *.proj nnoremap <buffer> ? :call ProjHelp()<CR>

:au BufNewFile,BufRead *.proj setlocal nowrap
" Disabled because of a problem with TabBar plugin
" :au BufRead *.proj :call StartupResize()
:au BufNewFile,BufRead *.proj setlocal ai

nnoremap <Leader>P :call OpenProj()<CR>

function! Vimject(...)
    :pyfile ~/.vim/python/vimject.py
endfu


function! StartupResize()     " After $ vim myproj.proj
    if len(tabpagebuflist()) == 1
        vsplit
        exe "normal 23\<c-w>|"
    endif
endfu

function! OpenProj()     " Open or create project
    let n = input("Project name: ")
    if n != ''
        exe "vsplit ".n.".proj"
        exe "normal 30\<c-w>|"
    endif
endfu


function! ProjHelp()
    " Help listing
    echo " Vimject commands:\n\n"


    echo " Open or start a project                              ".g:mapleader."P\n"
    echo " Open file or dir                                      Enter\n"
    echo " Open all files in dir or project                     ".g:mapleader."l\n"
    echo " Add all files in dir to listing                      ".g:mapleader."L\n"
    echo " Add current directory name                           ".g:mapleader."d\n"
    echo " Grep all files in dir or project                     ".g:mapleader."g\n"
    echo " Unload a file or all files in dir or project          U\n"
    echo " Run a .py, .sh or .html file                         ".g:mapleader."x\n\n"

    echo " potl outline for .py files in dir or project         ".g:mapleader."o\n"
    echo "      - same but txt format                           ".g:mapleader."p\n"
    echo "      - same but html format                          ".g:mapleader."y\n\n"

    echo " (For open all, grep all and unload all commands, cursor must be on a dir or project)\n"
    echo " This help message                                     ?\n"
endfu
