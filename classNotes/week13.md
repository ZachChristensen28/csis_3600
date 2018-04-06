# Week 13

## Unix Commands Continued

All unix commands return a status variable: `0` for OK `1` for not OK
> In a unix shell: 0 means true 1 means false

Use test to evaluate boolean conditionals

```bash
test -f data.txt # does it exist and is it a file?
```
Status of last command is stored in the `$?` variable

```bash
echo $? # to see results of previous command
OUTPUT: 0
```

### `test` Examples

```bash
test 1 -lt 2
OUTPUT: 0
```

Alternate Syntax for test: `[]`
```bash
[ -f data.txt ] # does it exist and is it a file?
OUTPUT: 0
```
```bash
[ 1 -lt 2 ]
OUTPUT: 0
```

## Scripts

```bash
#! /bin/bash
# script1

echo "The home directory is $HOME"
echo "The present working directory is $PWD"
echo -e "Here is a listing of the present working directory\n"

ls -al

RUN:
dos2unix script1
./script1
```
> Useful parameters: `$1` `$2` ... refer to the input parameters

> `$#` Holds the total number of parameters

```bash
#! /bin/bash
# script2

first=$1
second=$2
third=$3
total=$#

echo $first
echo $second
echo $third
echo $total
```

## Shell Math

`echo $[10*10]`

```bash
for ((i=0; i <= 10; i++)); do
  echo $[i*i]
done
```

### Conditionals

```bash
if [ -f /etc/hosts ]; then
  echo "The host file exists"
fi
```

## Text 2 HTML Script

```bash
#! /bin/bash
# Usage: text2html input.txt output.html

echo -e "<!DOCTYPE html>\n<html><body><pre>" > $2
cat $1 >> $2
echo "</pre></body></html>" >> $2
```

### Version 2.0

```bash
#! /bin/bash
# Usage: ls -al | ./text2html2
# Usage for files: cat awmt.txt | ./text2html2

echo -e "<!DOCTYPE html>\n<html><body><pre>" > out.html
while read LINE; do
  echo $LINE >> out.html
done
echo "</pre></body></html>" >> out.html
```

## Accepting Keyboard Input

```bash
#! /bin/bash
# Accepting input from the keyboard
# Usage: ./script04.bash

echo -e "Enter something from the keyboard\n"
read
echo "You entered: $REPLY"

echo -e "\nEnter something from the keyboard\n"
read input
echo -e "You entered: $input\n"

read -p "Again" input # Prompts user
echo "You entered $input"
```

## Friday LAB

View running tasks

      tasklist

Kill a process

      taskkill /PID [PID]

Kill a process using gawk

      tasklist | gawk '/notepad/ {system("taskkill /PID $2")}'

Kill process script
```bash
#! /bin/bash

# Usage: killprocess processName

pattern=$1

tasklist | gawk -v pat="$pattern" '$0 ~ pat {system(sprintf("taskkill /PID %s", $2))}' # `-v` assign value to variable
```
