#!/bin/sh

echo "enter a number"
read num
i=1
fact=1

while [ $i -le $num ] 
do
	
	fact=`expr $fact \* $i`
	i=`expr $i + 1`
done
if [ $num -eq 0 ]
	then 
		echo "factorial of 0 is : 1"
	else
		echo "factorial of $num is :$fact"
fi

	
