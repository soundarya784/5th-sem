echo "enter the word"
read word
echo "enter the filename"
read f
val=`grep -n $word $f`
echo $val
