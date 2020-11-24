echo "enter you username"
read name

cat /etc/passwd | grep $name | cut -d ":" -f1 > cse.txt
val=`cat cse.txt`
if [ -z $val ]
then
	echo "user not found"
else
	cat /etc/passwd | grep $name | cut -d ":" -f6 > cse.txt
	echo `cat cse.txt`
fi
