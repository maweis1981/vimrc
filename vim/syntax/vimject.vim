" Vim syntax file

if version < 600
    syntax clear
elseif exists("b:current_syntax")
    finish
endif

syn match All "*"
syn match Project "---.*---"
syn match Dir "^[~/].*"
syn match Dir "^\s*[^#].*/$"
syn match Comment "^\s*#.*"

hi def link All None
hi def link Project Special
hi def link Dir Keyword
hi def link Comment Comment

let b:current_syntax = "vimject"
