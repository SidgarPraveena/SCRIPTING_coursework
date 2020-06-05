cd $1
t=all
if [ $2 == $t ]; 
then
	mkdir jpg
	mkdir mp3
	mkdir mp4
	mkdir txt
	mkdir cpp
	mkdir sh
	mkdir odt
	mkdir pdf
	items=$(ls)
	for j in $items
	do
		case $j in
			*.jpg) mv $j ~/test/jpg;;
			*.mp3) mv $j ~/test/mp3;;
			*.mp4) mv $j ~/test/mp4;;
			*.cpp) mv $j ~/test/cpp;;
			*.odt) mv $j ~/test/odt;;
			*.sh) mv $j ~/test/sh;;
			*.txt) mv $j ~/test/txt;;
			*.pdf) mv $j ~/test/pdf;;
		esac
	done
else
	args=("$@")
	temp=1
	lim=`expr $# - $temp`
	for i in `seq 1 $lim`
	do
		dr=${args[i]}
		items=$(ls | grep $dr)
		mkdir $dr
		for j in $items
		do
			echo $j
			mv $j ~/test/$dr
		done
	done
fi
 
