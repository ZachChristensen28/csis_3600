#! /bin/bash
# Usage: ls -al | ./text2html2
# Usage for files: cat awmt.txt | ./text2html2 [filename]

# check for file name
if [ -z $1 ]; then
	echo "Please enter a file name"
	echo -e "Usage: ls -al | ./text2html2 [filename]\n"
	exit
fi

fileName=$1

# Text 2 html
echo -e "<!DOCTYPE html>\n<html><body><pre>" > out.html
while read LINE; do
  echo $LINE >> out.html
done
echo "</pre></body></html>" >> out.html

# Asks for file name and updates the file
if [[ $fileName != *".html" ]]; then
	fileName=$fileName.html
	mv -f out.html $fileName
fi

# Launch file in firefox
firefox $fileName