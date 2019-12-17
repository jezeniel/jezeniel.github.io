---
title: Why I Use Vim
date: 2019-09-03 00:00
category: Blog
tags: vim, tools
---

[Vim][vim] is an open source text editor created by [Bram Moolenar][bram]
in 1991, which is an enhanced clone of [vi][vi]. It is keyboard-driven, and
due to how the default keybindings were designed, your hands don't often need
to move far away from the home row keys.  Vim is very configurable, you can add
custom shortcuts, commands, and has tons of [plugins][plugins] to improve your
workflow. You can run it in your favorite terminal or as a stand-alone
application.

Vim has gained a reputation of being hard to quit, causing it to have
a [meme][vim meme], [speedrun][speedrun] video, and be one of the
top [StackOverflow][stackoverflow] questions. You can also do fun things like
[vim golfing][vim golf] to test your skills, or even play [Tetris][tetris] inside
vim.

<figure class="image">
  <img src="{static}/images/why_vim/vim.png">
  <figcaption><i>Now I am stuck forever</i></figcaption>
</figure>

## The Beginning

My adventures in vim began when I started using Linux. Tutorials and guides
around the internet sometimes use it to modify configurations and files.
My first time in using vim is when I tried modifying a config for a software
that I was using. I fired it up and ... I can't even insert any text, then I
started maniacally typing random characters until I pressed some unknown key 
that allowed me to insert something. After editing, I still need to Google how
to save my work and quit vim!

<figure class="image">
  <img src="{static}/images/why_vim/not_sudo.png">
  <figcaption><i>I forgot to use sudo again for the nth time...</i></figcaption>
</figure>

Then I read the ["Learn Vim Progressively"][learn vim prog] blog post. It
mentioned vim as a "Six Billion Dollar editor" and "the best text editor
known to humankind". The promise of improved productivity is too hard to pass.
The young me thought that if I can do everything in the terminal without
relying on a GUI, it will make me a cool and [l33t][l33t] programmer.
Maybe I tried learning it for the wrong reasons, either way I pushed myself 
to use it even though my productivity suffered a bit because of the learning
curve. Eventually, I got used to it and I am using vim ever since.

<figure class="image">
  <img src="{static}/images/why_vim/hackerman.jpg">
  <figcaption><i>I can be like this, minus the mullet.</i></figcaption>
</figure>


## Why use it?

Vim is a *modal* text editor, this means it has different modes that you can use.
Keybindings, commands, and actions will change depending on the mode.
This is quite different from the usual *modeless* text editors today like Notepad,
Notepad++ and GEdit, in which you can enter text right away at the start. 
Though some of these editors are *modeless* by default, editors like Emacs, Sublime
and VSCode have plugin systems that can emulate vim.

To compare shortcuts between *modal* and *modeless* editors, here is some
comparison between vim (in `NORMAL` mode) and vscode:

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

Because of the *modeless* nature of vscode, it relies on using modifier keys 
like `Ctrl` and `Alt` to execute commands.  But it doesn't mean that vim is
better than vscode. Vscode has nice features out of the box that you still need
to configure/add to vim. What I am trying to show here is that due to the
*modal* nature of vim, it doesn't rely much on modifier keys. This lessens
[chording][chording] and keyboard travel time, which increases productivity
once you get used to it.

In vim, the usual modes being used are `NORMAL`, `INSERT`, `VISUAL`, `COMMAND` and `REPLACE`.

### Normal Mode
`NORMAL` mode is the default whenever you start vim.  You cannot type any text,
but instead, this is where you can do navigation, text manipulation, undo/redo
and many more. You will need to switch back to this mode by pressing `ESC` before
changing to other modes.

### Insert Mode
`INSERT` mode is the most familiar mode, due to being the only mode of *modeless* editors. 
This is where you, as the name suggests, insert/type texts.  Pressing `i` will
make you switch from `NORMAL` to `INSERT` mode.

### Visual Mode
`VISUAL` mode is for highlighting/selecting lines or blocks of texts, it is similar
to using `SHIFT` and arrow keys in *modeless* text editors. You can press `v` to select by
characters or `V` to highlight lines of texts, this allows you to apply commands
only to the selected texts.

### Command Mode
`COMMAND` mode is like a command line input. You can go to this mode by pressing
`:`. This is where you can save `:w`, quit `:q`, save and quit `:wq` or call
vim functions.

### Replace Mode
`REPLACE` mode is like using the `Insert` key of your keyboard. It will
replace text from the starting point until you go back to `NORMAL` mode. 
You can activate this by pressing `R`.

There are still lots of things you can do in vim, and this is just the tip 
of the iceberg. ["Learn Vim Progressively"][learn vim prog], [Vimcasts][vimcasts] or
`vimtutor` which is already installed when you install vim in Linux are good place to
start.

## Takeaway

Vim is not a perfect text editor, but it introduced me to a more efficient
way of doing my work. It taught me that people can still find ways to
innovate/improve something that was considered good enough. There are times 
that vim is not the best fit for some projects, and it might be better to just
use other editors or IDEs like PyCharm and Android Studio. However, I am glad that
the community of awesome programmers creates vim emulation plugins so we
can enjoy the best of both worlds.

In the end, it is not about what is the best one (because there isn't any), and 
neither about being cool nor l33t. It is about what makes you do your work
enjoyable and fun.

## Bonus
For modeless text editor lovers, you can try vim mode! Here are some
good vim emulation plugins for your favorite text editors:

- [Evil](https://github.com/emacs-evil/evil) for Emacs
- [IdeaVim](https://github.com/JetBrains/ideavim) for IntelliJ platform like Jetbrains products or Android Studio
- [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous) for SublimeText
- [VSCodeVimA](https://github.com/VSCodeVim/Vim) for vscode


[l33t]: https://en.wikipedia.org/wiki/Leet
[vim]: https://www.vim.org
[vi]: https://en.wikipedia.org/wiki/Vi
[vim meme]: https://www.google.com/search?q=vim+meme&tbm=isch
[vim golf]: https://www.vimgolf.com/
[vimcasts]: http://vimcasts.org
[plugins]: https://vimawesome.com/
[bram]: https://en.wikipedia.org/wiki/Bram_Moolenaar
[stackoverflow]: https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/
[speedrun]: https://www.youtube.com/watch?v=TLbfqZBL8t8
[learn vim prog]: http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/
[tetris]: https://www.youtube.com/watch?v=_27mpiU-Zmg
[chording]: https://en.wikipedia.org/wiki/Chording
