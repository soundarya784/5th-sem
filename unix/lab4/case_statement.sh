echo "enter two numbers"
read a b
echo "enter an operator"
read op
case $op in
+) echo "additon: `expr $a + $b` "
	;;
-) echo "subtraction: `expr $a - $b` "
	;;
/) echo "division : `expr $a / $b` "
	;;
*) echo "multiplication : `expr $a \* $b` "
	;;

esac
