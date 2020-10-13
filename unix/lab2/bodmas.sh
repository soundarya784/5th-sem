#! /bin/sh

echo "enter two numbers"
read a
read b
ad1=`expr $a + $b`
sub1=`expr $a - $b`
p1=`expr $a \* $b`
div1=`expr $a / $b`
echo "addition : $ad1"
echo "subtraction : $sub1"
echo "mul: $p1"
echo "division : $div1"
