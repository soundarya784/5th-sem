echo "enter a number"
read num
i=0
num1=0
num2=1 
n=`expr $num - 1`
if [ $num -eq "0" ]
	then 
		echo "fibonacci of $num is:0"
		
	elif [ $num -eq "1" ]
	then
		echo "fibonacci of $num is: 1"
		
	else
		while [ $i -lt $n ]
		do
	
			sum=`expr $num1 + $num2`
			num1=$num2
			num2=$sum
			i=`expr $i + 1`
		done
		echo "fibonacci of $num is:$sum"
fi


	
	
