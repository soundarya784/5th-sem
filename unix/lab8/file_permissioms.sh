if [ $# -ne 2 ] 
then
	echo "enter filename"
elif [ ! -e $1 -o ! -e $2 ]
then
	echo "file does not exist"
else
	p1=`ls -l $1 | cut -c 2-10`
	p2=`ls -l $2 | cut -c 2-10`
	if [ $p1==$p2 ]
	then 
		echo "files are identical with permissions $p2"
	else
		echo "files are not equal \n $1 permission: $p1 \n $2 permission: $p2"
	fi
fi
	

