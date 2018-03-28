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

### Find every file with the name perl
```Bash
for i in *; do
  file $i | grep perl
done
```
### Find all Executable files

`ls | grep .exe`

### Find unique words

```Bash
for i in `cat awt.txt`; do
  echo $i
done | sort -u > $HOME/sortedWords.txt
...
# OR Sort by unique words
done | sort | uniq -c > $HOME/sortedWords2.txt
...
# OR Sort by Frequency
done | sort | uniq -c | sort > $HOME/sortedWords3.txt
```

## AWK

Pattern scanning and processing language

### Usage

`gawk 'program' filenames`

#### i.e.

Print out field one for /etc/passwd output
>`cat /etc/passwd | gawk -F: '{print $1}'`

`NR` - Number of Records
>`gawk '{print NR, $0}' datafile01`

#### Awk program
```AWK
{
  # awk01
  nc += length ($0)
  nw += NF # Number of fields
}
END {print NR, nw, nc}
```
Run
> `gawk -f awk01 awmt.txt`

## Heredocs

```Bash
#! /bin/bash
  DATE=`date`
  cat <<EOF
  date: $DATE

  Now is the time
  for all good programmers
  EOF
```
