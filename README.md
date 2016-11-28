# slides.vim [![Build Status](https://travis-ci.org/gabber12/slides.vim.svg?branch=master)](https://travis-ci.org/gabber12/slides.vim) [![Coverage Status](https://coveralls.io/repos/github/gabber12/slides.vim/badge.svg)](https://coveralls.io/github/gabber12/slides.vim) [![Build status](https://ci.appveyor.com/api/projects/status/468l3o3s522k0vpt?svg=true)](https://ci.appveyor.com/project/gabber12/slides-vim) [![PyPI version](https://badge.fury.io/py/slides.vim.svg)](https://badge.fury.io/py/slides.vim)

Code Presentations in vim

You can install slides.vim by 



## Installation

Install a markdown syntax highlighter for easier editing. (I recommend [tpope/vim-markdown](http://github.com/tpope/vim-markdown))


```
pip install slides.vim
```

## Usage

1. Write your slides in a markdown file (See below for details on _limited_ markdown syntax)

2. Run `vimslides <file_name.md>` and it will generate a file for each slide and open them in VIM



## A Note About Markdown

Slides are separated by 3 newlines in a row.

Example:

```
# Important Intro

* unordered list 1
* unordered list 2
* unordered list 3



# Important TOC

Your first paragraph
```
---------------------

Made by [gabber12](http://github.com/gabber12): [tybenz.com](http://gabber12.me) 



