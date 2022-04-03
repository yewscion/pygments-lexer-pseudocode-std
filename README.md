# (Standard) Pseudocode Syntax Lexer for Pygments

This package contains a Pygments Lexer for Pseudocode based on the standard
outlined [here][a].

## Installation

There are a couple ways to install this package.

### GNU Guix

If You use [GNU Guix][b], this package is on [my channel][c]. Once You have it
set up, You can just run:

```
guix pull
guix install python-pygments-lexer-pseudocode-std
```

### Source

If You don't want to use [GNU Guix][b], You can clone this repo and install it
Yourself.

```
python setup.py install
```

## Usage

After installation the Pseudocode lexer automatically registers itself for files
with the `.algo` and `.pseudocode` extensions. Therefore, usage is easy:

    pygmentize document.algo

You can also manally indicate you want to use the Pseudocode lexer by using a
command line flag:

    pygmentize -l pseudocode somefile 

## Contribute

If you found a bug, don't hesitate to make a pull request.

## License

This repository is a fork. [Here][d] is the original repository, which focused
on French terms.

The Original Pseudocode Lexer code is licensed under the terms of the [MIT
license][e]. Every change made in this repository is licensed under the [AGPL
3.0][f] license.


[a]: https://users.csc.calpoly.edu/~jdalbey/SWE/pdl_std.html
[b]: https://guix.gnu.org/
[c]: https://sr.ht/~yewscion/yewscion-guix-channel/
[d]: https://github.com/svvac/pygments-lexer-pseudocode
[e]: https://opensource.org/licenses/MIT
[f]: https://www.gnu.org/licenses/agpl-3.0.en.html
