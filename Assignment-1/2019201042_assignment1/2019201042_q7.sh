#!/bin/bash
trap 'stty sane; tput cnorm;' EXIT
stty -echo
tput civis
declare -A grid
snake="*"
x=20
y=100
xA=0
yA=0
color=$((color%7+1))
for((i=0; i<=55; i++))do
	for((j=0; j<=204; j++))do
		grid[$i,$j]=0
	done
done
clear
while sleep 0.1
do 
	if [[ $y -lt 1 ]];then
		break
	elif [[ $y -gt 204 ]];then
		break
	elif [[ $x -lt 1 ]];then
		break
	elif [[ $x -gt 55 ]];then
		break
	fi
	x=`expr $x + $xA`
	y=`expr $y + $yA`
	if [[ ${grid[$x,$y]} -eq 1 && $xA -ne $yA ]]; then
		break
	fi
	grid[$x,$y]=1
	while IFS= read -rs -t 0.0001 -n 1 key
	do
		case $key in
			q) clear
				exit 0;;
			A)((xA=-1))
			((yA=0))
			((cur=1));;
			B)((xA=1))
			((yA=0))
			((cur=2));;
			C)((yA=1)) 
			((xA=0))				
			((cur=3));;
			D)((yA=-1)) 
			((xA=0))
			((cur=4));;
			
		esac	
		snake="*"
		color=$((color%7+1))
	done
	tput cup $x $y
	tput setaf "$color"
	printf "%s" "$snake"
done
clear
echo "Bye"
