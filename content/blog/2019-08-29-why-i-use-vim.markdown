---
title: Why I use Vim
date: 2019-08-29 12:24
category: Blog
status: draft
tags: vim, personal, tools
---

[Vim][vim] (*VI IMproved*) is an open source text editor created by [Bram Moolenar][bram]
in 1991, it is an enhanced clone of vi, which is an older text editor. You
can use it inside a terminal and has a standalone app with a graphical
user interface.

It has a [speedrun][speedrun], and made a million of developers go to
[StackOverflow][stackoverflow] just to learn how to quit it. Vim is my
favorite text editor.

<figure class="image">
  <img src="{static}/images/why_vim/vim.png">
  <figcaption><i>Now I am stuck forever</i></figcaption>
</figure>

## The Beginning

My adventures in Vim started when I started using and learning Linux.
Tutorials and troubleshooting guides in the forums sometimes uses vi/vim when
modifying files. As expected, the first time I used it I can't
even write anything unless I accidentally pressed `a` or `i` to change
to `INSERT` mode. After editing I don't even know how to save or quit!

I was excited by the idea of doing everything in the terminal, the young me
wanted to be a cool and l33t programmer. I know it has a learning curve, but the
promise of increased productivity is very tempting to pass. So I tried to learn 
and use it on and off.

Then I stumbled upon the ["Learn Vim Progressively"][learn vim prog]
blog post. The article mentioned Vim to be a "Six Billion Dollar editor"
and "the best text editor known to human kind". After reading the article,
and seeing what Vim is capable of I was determined to learn and use it
once and for all. Many years has passed and I still use Vim.

## Why use it?

Vim introduced me to the world of *modal* text editors. It means
that it has different modes of editing. The effect of keys will change depending
on the current mode the editor is on.

This is quite different from the usual *modeless* text editors like  Notepad,
Notepad++ and GEdit. Though some of these editors are *modeless* like Emacs, Sublime
and VSCode by default, they have plugin system which can implement vim like mode.

In Vi/Vim there are two primary modes which are `NORMAL` and `INSERT` mode.
There are also three other modes which are `VISUAL`, `COMMAND` and `REPLACE`.

### Normal Mode
`NORMAL` mode is the default whenever you start Vim.  You cannot type text,
but instead, this is where you can do navigation, text manipulation, undo/redo
and many more.  You can also configure custom commands to run in this mode.
You will need to switch back to this mode by pressing `ESC` before 
changing to other modes.

### Insert Mode
`INSERT` mode is the more familiar mode for majority of people. This is where
you, as the name suggests, insert text. Press `i` so you can go from `NORMAL`
to `INSERT` mode.

### Visual Mode
`VISUAL` mode is for highlighting/selecting lines or blocks of text. It is similar
to using `SHIFT` and arrow keys in modeless text editors. It allows you to
do apply commands to the selected texts. You can use `v` to select single
character or `V` to highlight lines of texts.

### Command Mode
`COMMAND` mode is like a command line input. You can go to this mode by pressing
`:`. This is where you can save `:w`, quit `:q`, save and quit `:wq`.

### Replace Mode
`REPLACE` mode is like using the `Insert` key of your keyboard. It will 
replace text from the starting point. You can acti


[vim]: https://www.vim.org
[bram]: https://en.wikipedia.org/wiki/Bram_Moolenaar
[stackoverflow]: https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/
[speedrun]: https://www.youtube.com/watch?v=TLbfqZBL8t8
[learn vim prog]: http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/
