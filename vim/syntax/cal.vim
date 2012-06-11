:syntax match hltoday +\[ \d\{1,2}\*\? \?\]+
:syntax match month +^====== .*+
:syntax match day +^=== .*+

:hi hltoday guifg=#999 guibg=#222
:hi month guibg=#888
:hi day guibg=#882
