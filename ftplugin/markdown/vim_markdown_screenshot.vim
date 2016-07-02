" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))


" --------------------------------
"  Ensure python support exists
" --------------------------------
if !has('python')
    finish
endif


" --------------------------------
"  Function(s)
" --------------------------------
function! Screenshot()
python << endOfPython

from vim_markdown_screenshot import take_screenshot
take_screenshot()

endOfPython
endfunction


" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! Screenshot call Screenshot()
