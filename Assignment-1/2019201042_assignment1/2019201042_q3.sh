#!/bin/sh

read var
echo $var

if [ $var ]; then
	case $var in
		*.zip)unzip $var       ;;
		*.gz)gunzip $1         ;;
		*.tar)tar $var         ;;
		*.tar.gz)tar xvzf $var ;;
		*.tar.xz)tar zvxf $var ;;
		*.tar.bz2)tar xjf $1   ;;
    		*.tbz2)tar xjf $1      ;;
    		*.bz2)bunzip2 $1       ;;
    		*.rar)rar x $1         ;;
		*)echo "Cannot be extracted";;
	esac
fi
