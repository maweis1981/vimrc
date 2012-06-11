" This sets up *.potl files to be outlines
au BufNewFile,BufRead *.potl			set ft=potl

" Mappings:
:au FileType potl nnoremap <buffer> <Leader>n :call NewHeader()<CR>A
:au FileType potl nnoremap <buffer> <Leader>z0 :set foldlevel=0<CR>
:au FileType potl nnoremap <buffer> <Leader>z1 :set foldlevel=1<CR>
:au FileType potl nnoremap <buffer> <Leader>z2 :set foldlevel=2<CR>
:au FileType potl nnoremap <buffer> <Leader>z3 :set foldlevel=3<CR>
:au FileType potl nnoremap <buffer> <Leader>z4 :set foldlevel=4<CR>
:au FileType potl nnoremap <buffer> <Leader>z5 :set foldlevel=5<CR>
:au FileType potl nnoremap <buffer> <Leader>z6 :set foldlevel=6<CR>
:au FileType potl nnoremap <buffer> <Leader>z7 :set foldlevel=7<CR>
:au FileType potl nnoremap <buffer> <Leader>z8 :set foldlevel=8<CR>
:au FileType potl nnoremap <buffer> <Leader>z9 :set foldlevel=9<CR>
:au FileType potl nnoremap <buffer> <Leader>h :call PotlHelp()<CR>
:au FileType potl nnoremap <buffer> <Leader>> :call PotlPromote(1)<CR>
:au FileType potl nnoremap <buffer> <Leader>< :call PotlPromote(-1)<CR>
:au FileType potl nnoremap - zc
:au FileType potl nnoremap = zo

:au FileType potl setlocal foldmethod=expr foldexpr=PotlFoldLevel(v:lnum) formatoptions=crqno autoindent
:au FileType potl setlocal foldtext=PotlFoldText()

