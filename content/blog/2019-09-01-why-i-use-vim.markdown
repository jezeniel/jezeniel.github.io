---
title: Why I Use Vim
date: 2019-09-01 12:00
category: Blog
status: draft
tags: vim, personal, tools
---

[Vim][vim] (*Vi IMproved*) is an open source text editor created by [Bram Moolenar][bram]
in 1991, which is an enhanced clone of vi, an older text editor. It is
usable inside your favorite terminal or can be a standalone application.

It is keyboard driven, this means that you don't need to use a mouse to navigate.
Your hands doesn't even need to travel far away from the home row keys due to the
bindings like `hjkl` way of navigating (though you can still use arrow keys). Vim is also very 
configurable and has tons of [plugins][plugins] you can use to improve experience.

There are also lots of fun things happening around the Vim universe.
Quitting Vim became a [meme][vim meme], it is also one of the top [StackOverflow][stackoverflow]
questions, and there is even a [speedrun][speedrun] video! You can also play [vimgolf][vim golf]
to test your vim skills, or even play [tetris][tetris].

<figure class="image">
  <img src="{static}/images/why_vim/vim.png">
  <figcaption><i>Now I am stuck forever</i></figcaption>
</figure>

## The Beginning

My adventures in vim started when I began using Linux, tutorials and guides
around the internet sometimes uses it to modify configurations and files.

The first time I used it while following a guide -- I can't even insert any text,
then I started typing random characters until I pressed some unknown keys that
allowed me to insert something. After editing, I still need to Google 
how to save my work and quit vim.

<figure class="image">
  <img src="{static}/images/why_vim/not_sudo.png">
  <figcaption><i>I forgot to sudo again...</i></figcaption>
</figure>

Then I saw the ["Learn Vim Progressively"][learn vim prog]
blog post. The article mentioned vim to be a "Six Billion Dollar editor"
and "the best text editor known to human kind". After reading the post,
the promise of improved productivity is too hard to pass, and the young me
also wanted to be a cool and l33t programmer. I am using vim ever since.

## Why use it?

Vim introduced me to the world of *modal* text editors. This means
you can switch to different modes, between invoking commands and entering texts,
the function of keys will also change depending on the mode.

This is quite different from the usual *modeless* text editors today like  Notepad,
Notepad++ and GEdit, in which you can enter text right away after opening. 
Though some of these editors are *modeless* by default, some editors like Emacs, Sublime
and VSCode have plugin systems which can emulate vim.

To compare shortcuts between *modal* and *modeless* editors, here are some 
comparison between vim and vscode:

| action | vim | vscode |
|--------|-----|--------|
| cut line | `dd` | `Ctrl + x` |
| copy line | `yy` | `Ctrl + c` |
| move line up/down | n/a | `Alt + ↑/↓` |
| jump to matching bracket | `%` | `Ctrl + Shift + \` |
| insert line below | `o` | `Ctrl + Enter` |
| insert line above | `O` | `Ctrl + Shift + Enter` |
| go to beginning/end of line | `0`/`$` | `Home`/`End` |
| go to the beginning of file | `gg` | `Ctrl + Home` |
| go to the end of file | `G` | `Ctrl + End` |

Comparing between the two, because of the *modeless* nature of vscode, it is
reliant on using modifier keys like `Ctrl` and `Alt` to execute commands.
But it doesn't mean that vim is better than vscode. Vscode also have nice features
out of the box that you still need to configure/add to vim.

What I am trying to show here is that due to the *modal* nature of vim, it
doesn't rely so much on modifier keys, which lessens [chording][chording] and
keyboard travel time. This results in increased productivity once you get
used to it.

In vim the usual modes being used are `NORMAL`, `INSERT`, `VISUAL`, `COMMAND` and `REPLACE`.

### Normal Mode
`NORMAL` mode is the default whenever you start vim.  You cannot type any text,
but instead, this is where you can do navigation, text manipulation, undo/redo
and many more. You can also configure custom commands to run in this mode.
You will need to switch back to this mode by pressing `ESC` before
changing to other modes.

### Insert Mode
`INSERT` mode is the most familiar mode, due to being the default or only
mode of *modeless* editors. This is where you, as the name suggests,
insert/type texts. Press `i` so you can go from `NORMAL` to `INSERT` mode.

### Visual Mode
`VISUAL` mode is for highlighting/selecting lines or blocks of texts. It is similar
to using `SHIFT` and arrow keys in *modeless* text editors, this allows you to
apply commands only to the selected texts. You can use `v` to select by
characters or `V` to highlight lines of texts.

### Command Mode
`COMMAND` mode is like a command line input. You can go to this mode by pressing
`:`. This is where you can save `:w`, quit `:q`, save, quit `:wq` or call
vim functions.

### Replace Mode
`REPLACE` mode is like using the `Insert` key of your keyboard. It will
replace text from the starting point. You can activate this by pressing `R`.

As of writing, vim is the only modal editor I used.

## Takeaway

Vim is not a perfect text editor, but it introduced me to a more efficient
way of doing my work and not about being cool or l33t. It taught me that people
can find ways to innovate/improve something that were considered good enough.

I also use vscode, pycharm and Android Studio, sometimes vim is not the best fit 
for some projects, and it might be better to just use other editors or IDEs.
But I am glad that the community creates vim emulation plugins to these programs
so I can have the best of both worlds.

In the end it is what is the best one, its what makes you more happy in doing
what you love.

## Bonus
For modeless text editor lovers, you can try vim mode! Here are some
good vim emulation plugins for your favorite text editors:

- [Evil](https://github.com/emacs-evil/evil) for Emacs
- [IdeaVim](https://github.com/JetBrains/ideavim) for IntelliJ platform like Jetbrains products or Android Studio
- [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous) for SublimeText
- [VSCodeVimA](https://github.com/VSCodeVim/Vim) for vscode


[vim]: https://www.vim.org
[vim meme]: https://www.google.com/search?q=vim+meme&tbm=isch
[vim golf]: https://www.vimgolf.com/
[plugins]: https://vimawesome.com/
[bram]: https://en.wikipedia.org/wiki/Bram_Moolenaar
[stackoverflow]: https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/
[speedrun]: https://www.youtube.com/watch?v=TLbfqZBL8t8
[learn vim prog]: http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/
[tetris]: https://www.youtube.com/watch?v=_27mpiU-Zmg
[chording]: https://en.wikipedia.org/wiki/Chording
