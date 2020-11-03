echo "enter temperature in farenheit"
read f
c=`echo "(($f-32)*5)/9"|bc`
echo "temperature in celsius : $c degree celcius"

