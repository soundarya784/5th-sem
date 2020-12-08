len=$#
i=1
val=$@
echo "arguments in reverse order"
while [ $i -le $len ]
do
	a=`expr $len - $i`
	shift $a
	echo "$1"
	set $val
	i=`expr $i + 1`
done
	
