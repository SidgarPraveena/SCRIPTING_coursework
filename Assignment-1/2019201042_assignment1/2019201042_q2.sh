echo $1
case $1 in
	*.jpg) display $1;;
	*.jpeg) display $1;;
	*.BMP) display $1;;
	*.mp3) ffplay $1;;
	*.aif) sox $1 five.wav
		ffplay five.wav;;
	*.wav) ffplay $1;;
	*.sh) gedit $1;;
	*.cpp) gedit $1;;
	*.txt) gedit $1;;
	*.py) gedit $1;;
	*.java) gedit $1;;
	*.xml) gedit $1;;
	*.html) google-chrome $1;;
	*.pdf) evince $1;;
esac
