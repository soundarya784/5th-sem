echo "enter salary"
read sal
da=`echo $sal\*0.03|bc`
hra=`echo $sal\*0.02|bc`
gross=`echo $sal+$da+$hra|bc` 
echo "GROSS SALARY IS: $gross"
