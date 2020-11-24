echo "enter file1 name"
read f1
echo "enter file2 name"
read f2
head -n 5 $f1>cse.txt
head -n 15 $f2|tail -n 8 $f2 >> cse.txt
echo `cat cse.txt`
echo " "
echo "number of lines:`wc -l cse.txt`"
