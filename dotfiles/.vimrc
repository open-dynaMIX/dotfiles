" {{@@ env['dotdrop_warning'] @@}}

set nocompatible              " be iMproved, required
filetype off                  " required
let mapleader = " "

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

Plugin 'tomtom/tcomment_vim'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'plytophogy/vim-virtualenv'
Plugin 'tpope/vim-fugitive'

Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline_theme='term'
set ttimeoutlen=50

" auto-completion
" Plugin 'Valloric/YouCompleteMe'
" Track the engine.
Plugin 'SirVer/ultisnips'
" Snippets are separated from the engine. Add this if you want them:
Plugin 'honza/vim-snippets'

" define custom snippet directory
let g:UltiSnipsSnippetDirectories=["UltiSnips", "custom_snippets"]
" make YCM compatible with UltiSnips (using supertab)
" let g:ycm_key_list_select_completion = ['<C-n>', '<Down>']
" let g:ycm_key_list_previous_completion = ['<C-p>', '<Up>']
" let g:SuperTabDefaultCompletionType = '<C-n>'

" better key bindings for UltiSnipsExpandTrigger
let g:UltiSnipsExpandTrigger = "<tab>"
let g:UltiSnipsJumpForwardTrigger = "<tab>"
let g:UltiSnipsJumpBackwardTrigger = "<s-tab>"

" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

syntax on
colorscheme vividchalk
" colorscheme darkblue

set number          " show line numbers
set ls=2            " allways show status line
set tabstop=4       " numbers of spaces of tab character
set expandtab       " tabs are spaces
set shiftwidth=4    " numbers of spaces to (auto)indent
set showcmd         " display incomplete commands
set clipboard=unnamedplus
set hlsearch        " highlight searches
set ruler           " show the cursor position all the time
set title           " show title in console title bar
set autoindent      " always set autoindenting on
set smartindent     " smart indent
set showtabline=2   " always show tabbar
set mouse=a         " enable mousescroll
set nowrap
set ssop-=options    " do not store global and local values in a session
set ssop-=folds      " do not store folds
hi Normal guibg=NONE ctermbg=NONE
set t_Co=256
highlight ColorColumn ctermbg=8 guibg=lightgrey
let &colorcolumn=join(range(81,999),",")

au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

" Use ctrl-[hjkl] to select the active split!
nmap <silent> <c-k> :wincmd k<CR>
nmap <silent> <c-j> :wincmd j<CR>
nmap <silent> <c-h> :wincmd h<CR>
nmap <silent> <c-l> :wincmd l<CR>
nmap <silent> <c-up> :wincmd k<CR>
nmap <silent> <c-down> :wincmd j<CR>
nmap <silent> <c-left> :wincmd h<CR>
nmap <silent> <c-right> :wincmd l<CR>
map t <Esc>:tabnew
command CustomHelp tabnew ~/.vim/vim_cheatsheet.txt
