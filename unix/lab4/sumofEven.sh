echo "enter a number"
read num
i=0
even=0
while [ $i -le $num ]
do
	even=`expr $even + $i`
	i=`expr $i + 2`
done
echo "sum of even numbers upto $num is: $even"
	 
