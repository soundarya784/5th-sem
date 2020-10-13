#!/bin/sh
echo "enter filename (wordcount will be redirected to newfile.txt)"
read fname
output=`wc $fname`
echo $output >newfile.txt
