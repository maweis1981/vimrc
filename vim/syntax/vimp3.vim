" Vim syntax file

if version < 600
    syntax clear
elseif exists("b:current_syntax")
    " finish
endif

syn match All ".*"
syn match Current "^> .*"
syn match Playlist "^--- .*"
syn match Vimp3Dir ".*/"
" syn match Done ".*  100  .*"

" hi def link All Keyword
" hi Header guifg=#222
" hi All guifg=#cc5
"
" hi def link Current Integer
hi Current guifg=#581 guibg=#333
hi Playlist guifg=#a45 guibg=#222
hi Vimp3Dir guifg=#a45
hi def link Current String
" hi def link Done String

" hi def link OnHold Special
" hi def link All Float

let b:current_syntax = "vimp3"
