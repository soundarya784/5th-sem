echo "enter a number"
read num
if [ $num -lt 0 ]
then
	echo "number is negative"
elif [ $num -eq 0 ]
then
	echo "number equals zero"
else
	echo "number is positive"
fi
