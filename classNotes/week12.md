# Week 12

## tar

- c: create
- v: verbose
- f: use the following file
- z: compress
- x: extract
- t: list contents
- r: append

**common usage:**

> `tar cvfz new-name.tar.gz file-to-tar` # compress and archive the file
>
> `tar xvfz tar-file.tar.gz` # extract compressed archive file

## grep

**d.f.** globally search a regular expression and print

Examples:

1. `grep -in ".* interface" regular-expressions.txt` # `-i` ignore case and `n` print line numbers
1. `grep -wn express regular-expressoins.txt` # `-w` select only words
1. `grep -c express regular-expressions.txt` # `-c` counts the number of occurences
1. `grep -o express regular-expressions.txt` # `-o` print only the occurences

**Color for grep** `export GREP_OPTIONS='--color=auto'`
