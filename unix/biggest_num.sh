echo "enter three numbers"
read num1 num2 num3
large=0
test $num1 -gt $num2 && large=$num1 || large=$num2
test $num3 -gt $large && large=$num3 
echo $large 

