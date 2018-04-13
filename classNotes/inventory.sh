#! /bin/bash
# Usage: ./inventory.sh [path-to-inventory] [filename]

# Check for valid path
if [ -z $1 ]; then
  echo "Please enter a path inventory"
  echo -e "Usage: ./inventory.sh [path-to-inventory] [filename]\n"
  exit
fi

# Check for file name
if [ -z $2 ]; then
	echo "Please enter a file name"
	echo -e "Usage: ./inventory.sh [path-to-inventory] [filename]\n"
	exit
fi

path=$1
fileName=$2

# Text 2 html
echo -e "<!DOCTYPE html>\n<html><body><pre>" > out.html
ls -al $path >> out.html
echo "</pre></body></html>" >> out.html

# Asks for file name and updates the file
if [[ $fileName != *".html" ]]; then
	fileName=$fileName.html
fi

# Rename file
mv -f out.html $fileName

# Launch file in firefox
firefox $fileName
