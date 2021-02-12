set exrc
set noerrorbells
set mouse=a
set guicursor=
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set relativenumber nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set nohlsearch
set hidden
set termguicolors
set scrolloff=7
set completeopt=menuone,noinsert,noselect
set colorcolumn=100
set signcolumn=yes
set cmdheight=1
set updatetime=200
set shortmess+=c
set splitright
set splitbelow

highlight ColorColumn ctermbg=0 guibg=lightgrey

call plug#begin('~/.vim/plugged')

Plug 'mhinz/vim-startify'
Plug 'gruvbox-community/gruvbox'
Plug 'itchyny/vim-gitbranch'
Plug 'itchyny/lightline.vim'
Plug 'flazz/vim-colorschemes'
Plug 'scrooloose/nerdtree'
Plug 'szw/vim-maximizer'
Plug 'christoomey/vim-tmux-navigator'
Plug 'kassio/neoterm'
Plug 'tpope/vim-commentary'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'neoclide/coc.nvim'
Plug 'janko/vim-test'
Plug 'vimwiki/vimwiki'
Plug 'chun-yang/auto-pairs'
Plug 'sirver/ultisnips'
Plug 'frazrepo/vim-rainbow'
Plug 'mileszs/ack.vim'
Plug 'ryanoasis/vim-devicons'
Plug 'ap/vim-css-color'
"Plug 'tmhedberg/simpylfold'

call plug#end()

colorscheme gruvbox
highlight Normal guibg=NONE

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" MY MAPPINGS...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let mapleader=" "
nnoremap <leader>z <Esc>:w<CR>
nnoremap <leader>vs <Esc>:vs<CR>
nnoremap <leader>e :e $MYVIMRC<CR>
nnoremap <leader>s :source $MYVIMRC<CR>
nnoremap <leader>bN :bprevious<CR>
nnoremap <leader>bn :bnext<CR>
nnoremap <leader>bd :bd<CR>
nnoremap <F5> :terminal <CR>
nnoremap <c-k> :Commentary<CR>
nmap <silent> <c-s> <Esc>:w<CR>
nmap <silent> 1j 5j
nmap <silent> 2j 10j
nmap <silent> 3j 15j
nmap <silent> 1k 5k
nmap <silent> 2k 10k
nmap <silent> 3k 15k

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" helpful..
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
function! Demo()
   	let curline = getline('.')
    call inputsave()
    let text = input("Enter File Name:: ")
    call inputrestore()
    return text
    " call setline('.', curline . ' ' . name)
endfunction

" " Copy to clipboard
vnoremap  <leader>y  "+y
nnoremap  <leader>Y  "+yg_
nnoremap  <leader>y  "+y
nnoremap  <leader>yy  "+yy

" " Paste from clipboard
nnoremap <leader>p "+p
nnoremap <leader>P "+P
vnoremap <leader>p "+p
vnoremap <leader>P "+P

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"CHANGE FONT SIZE commands...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let s:fontsize = 12
function! AdjustFontSize(amount)
  let s:fontsize = s:fontsize+a:amount
  :execute "set guifont=Hack\ Nerd\ Font\ Regular\ " . s:fontsize
endfunction

noremap <C-ScrollWheelUp> :call AdjustFontSize(1)<CR>
noremap <C-ScrollWheelDown> :call AdjustFontSize(-1)<CR>
inoremap <C-ScrollWheelUp> <Esc>:call AdjustFontSize(1)<CR>a
inoremap <C-ScrollWheelDown> <Esc>:call AdjustFontSize(-1)<CR>a

" In normal mode, pressing numpad's+ increases the font
noremap <kPlus> :call AdjustFontSize(1)<CR>
noremap <kMinus> :call AdjustFontSize(-1)<CR>
" In insert mode, pressing ctrl + numpad's+ increases the font
inoremap <C-kPlus> <Esc>:call AdjustFontSize(1)<CR>a
inoremap <C-kMinus> <Esc>:call AdjustFontSize(-1)<CR>a

fun! TrimWhitespace()
    let l:save = winsaveview()
    keeppatterns %s/\s\+$//e
    call winrestview(l:save)
endfun

augroup SOBHAN_BERA
    autocmd!
    autocmd BufWritePre * :call TrimWhitespace()
augroup END

let g:netrw_banner=0 " disable banner in netrw
let g:netrw_liststyle=3 " tree view in netrw
let g:markdown_fenced_languages = ['javascript', 'js=javascript', 'json=javascript'] " syntax highlighting in markdown

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" List all presets
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nmap <space>el :CocList explPresets

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Lighline configs...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:lightline = {
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'gitbranch#name'
      \ },
      \ 'colorscheme': 'gruvbox',
      \ }

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" maximizer config...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <leader>m :MaximizerToggle!<CR>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" neoterm configs...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:neoterm_default_mod = 'vertical'
let g:neoterm_size = 50
let g:neoterm_autoinsert = 1
let g:neoterm_autoscroll = 1
let g:neoterm_term_per_tab = 1
nnoremap <c-q> <Esc>:Ttoggle<CR>
inoremap <c-q> <Esc>:Ttoggle<CR>
tnoremap <c-q> <c-\><c-n>:Ttoggle<CR>
nnoremap <leader>x :TREPLSendLine<CR>
vnoremap <leader>x :TREPLSendSelection<CR>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" fzf.vim configs...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <leader><space> :GFiles<CR>
nnoremap <leader>FF :Files<CR>
nnoremap <leader>cc :History:<CR>
nnoremap <leader>ff :Rg<CR>
nnoremap <leader>fb :Buffers<CR>
inoremap <expr> <c-x><c-f> fzf#vim#complete#path(
    \ "find . -path '*/\.*' -prune -o -print \| sed '1d;s:^..::'",
    \ fzf#wrap({'dir': expand('%:p:h')}))
if has('nvim')
  au! TermOpen * tnoremap <buffer> <Esc> <c-\><c-n>
  au! FileType fzf tunmap <buffer> <Esc>
endif

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" fugitive configs...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <leader>gg :G<cr>
nnoremap <leader>dg :Gdiff master<cr>
nnoremap <leader>gl :G log -100<cr>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" autocomplete...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Use <c-space> to trigger completion.
if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Symbol renaming.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nmap <leader>rn <Plug>(coc-rename)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Formatting selected code.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" vim-test...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <silent> tt :TestNearest<CR>
nnoremap <silent> tf :TestFile<CR>
nnoremap <silent> ts :TestSuite<CR>
nnoremap <silent> t_ :TestLast<CR>
let test#strategy = "neovim"
let test#neovim#term_position = "vertical"

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" RAINBOW PARENTHESES CONFIGs.....
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:rbpt_colorpairs = [
    \ ['brown',       'RoyalBlue3'],
    \ ['Darkblue',    'SeaGreen3'],
    \ ['darkgray',    'DarkOrchid3'],
    \ ['darkgreen',   'firebrick3'],
    \ ['darkcyan',    'RoyalBlue3'],
    \ ['darkred',     'SeaGreen3'],
    \ ['darkmagenta', 'DarkOrchid3'],
    \ ['brown',       'firebrick3'],
    \ ['gray',        'RoyalBlue3'],
    \ ['black',       'SeaGreen3'],
    \ ['darkmagenta', 'DarkOrchid3'],
    \ ['Darkblue',    'firebrick3'],
    \ ['darkgreen',   'RoyalBlue3'],
    \ ['darkcyan',    'SeaGreen3'],
    \ ['darkred',     'DarkOrchid3'],
    \ ['red',         'firebrick3'],
    \ ]
let g:rbpt_max = 16
let g:rbpt_loadcmd_toggle = 0

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Ultisnips...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <leader>u :UltiSnipsEdit<CR>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Rainbow...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:rainbow_active = 1
let g:rainbow_guifgs = ['RoyalBlue3', 'DarkOrange3', 'DarkOrchid3', 'FireBrick']
let g:rainbow_ctermfgs = ['lightblue', 'lightgreen', 'yellow', 'red', 'magenta']

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" STARTIFY ...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <leader>ls :SLoad<CR>
nnoremap <leader>ds :SDelete<CR>
nnoremap <leader>cs :SClose<CR>

" returns all modified files of the current git repo
" `2>/dev/null` makes the command fail quietly, so that when we are not
" in a git repo, the list will be empty
function! s:gitModified()
    let files = systemlist('git ls-files -m 2>/dev/null')
    return map(files, "{'line': v:val, 'path': v:val}")
endfunction

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" same as above, but show untracked files, honouring .gitignore
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
function! s:gitUntracked()
    let files = systemlist('git ls-files -o --exclude-standard 2>/dev/null')
    return map(files, "{'line': v:val, 'path': v:val}")
endfunction

let g:startify_lists = [
        \ { 'type': 'files',     'header': ['   MRU']            },
        \ { 'type': 'dir',       'header': ['   MRU '. getcwd()] },
        \ { 'type': 'sessions',  'header': ['   Sessions']       },
        \ { 'type': 'bookmarks', 'header': ['   Bookmarks']      },
        \ { 'type': function('s:gitModified'),  'header': ['   git modified']},
        \ { 'type': function('s:gitUntracked'), 'header': ['   git untracked']},
        \ { 'type': 'commands',  'header': ['   Commands']       },
        \ ]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" NERDTREE CONFIGs...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTreeToggle<CR>:vertical resize 35<CR>
nnoremap <C-t> :NERDTree<CR>:vertical resize 35<CR>
nnoremap <C-f> :NERDTreeFind<CR>

"NERDTREE AND STARTIFY...
let g:startify_bookmarks = systemlist("cut -sd' ' -f 2- ~/.NERDTreeBookmarks")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" folding configs...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"let g:SimpylFold_docstring_preview = 1
"let g:SimpylFold_fold_import = 1
"let g:SimpylFold_fold_blank = 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"OTHER CUSTOMs... this configs are taken from window gvim version gvimrc...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if filereadable("/etc/vim/gvimrc.local")
  source /etc/vim/gvimrc.local
endif

set encoding=utf-8
" source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim
behave mswin

nnoremap <C-/> :s/^\(\s*\)/\1\/\/<CR> :s/^\(\s*\)\/\/\/\//\1<CR> $
nnoremap <C-r> :so /etc/vim/gvimrc<CR>

if &diffopt !~# 'internal'
  set diffexpr=MyDiff()
endif
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg1 = substitute(arg1, '!', '\!', 'g')
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg2 = substitute(arg2, '!', '\!', 'g')
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let arg3 = substitute(arg3, '!', '\!', 'g')
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      if empty(&shellxquote)
        let l:shxq_sav = ''
        set shellxquote&
      endif
      let cmd = '"' . $VIMRUNTIME . '\diff"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  let cmd = substitute(cmd, '!', '\!', 'g')
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3
  if exists('l:shxq_sav')
    let &shellxquote=l:shxq_sav
  endif
endfunction

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Useful functions...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
function LoadTime()
	let ti=strftime('%c')
	let ex="|*| @created on : "
	let fi=ex . ti
	put=fi
endfunction

function! RandInt(Low, High) abort
    let l:milisec = str2nr(matchstr(reltimestr(reltime()), '\v\.\zs\d+'))
    return l:milisec % (a:High - a:Low + 1) + a:Low
endfunction


" END OF CONFIGs...
"TESTING
