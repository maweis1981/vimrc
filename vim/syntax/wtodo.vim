" Vim syntax file

if version < 600
    syntax clear
elseif exists("b:current_syntax")
    " finish
endif

syn match All ".*"
syn match OnHold ".*  Yes  .*"
syn match Done ".*  100  .*"
syn match Header " Name  .*\|----.*"

" hi def link All Keyword
" hi Header guifg=#222
" hi All guifg=#cc5
"
hi def link Header Integer
hi def link Done String

hi def link OnHold Special
hi def link All Float

let b:current_syntax = "todo"
