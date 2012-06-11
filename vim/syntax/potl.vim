
syn match potlText /^[ ]*[^·].*/
syn match potlTab9 /^                                    ·[^\t].*/
syn match potlTab8 /^                                ·[^\t].*/
syn match potlTab7 /^                            ·[^\t].*/
syn match potlTab6 /^                        ·[^\t].*/
syn match potlTab5 /^                    ·[^\t].*/
syn match potlTab4 /^                ·[^\t].*/
syn match potlTab3 /^            ·[^\t].*/
syn match potlTab2 /^        ·[^\t].*/
syn match potlTab1 /^    ·[^\t].*/
syn match potlTab0 /^·[^\t].*/


if &background == "dark"
  hi def potlTodo ctermbg=3 guibg=lightyellow guifg=black
  hi def potlTagRef ctermbg=3 ctermfg=4 cterm=bold guibg=lightred guifg=black
  hi def potlTagDef ctermbg=3 ctermfg=4 cterm=bold guibg=lightgreen guifg=black
else
  hi def potlTodo ctermbg=3 guibg=lightyellow
  hi def potlTagRef ctermbg=3 ctermfg=4 cterm=bold guibg=lightred
  hi def potlTagDef ctermbg=3 ctermfg=4 cterm=bold guibg=lightgreen
  hi def potlTextLeader guifg=darkgrey ctermfg=7
endif

hi Folded guibg=#676 guifg=#ccc
hi def potlTab0 ctermfg=1 cterm=NONE guifg=brown
hi def potlTab1 ctermfg=4 cterm=NONE guifg=darkcyan
hi def potlTab2 ctermfg=2 cterm=NONE guifg=#469
hi def potlTab3 ctermfg=3 cterm=NONE guifg=brown
hi def potlTab4 ctermfg=5 cterm=NONE guifg=darkmagenta
hi def potlTab5 ctermfg=6 cterm=NONE guifg=darkcyan
hi def potlTab6 ctermfg=1 cterm=NONE guifg=red
hi def potlTab7 ctermfg=4 cterm=NONE guifg=blue
hi def potlTab8 ctermfg=2 cterm=NONE guifg=darkgreen
hi def potlTab9 ctermfg=3 cterm=NONE guifg=brown

" vim: ts=2 sw=2 et
