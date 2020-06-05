#!/bin/sh
echo -n "Enter latitude: "
read lat
echo -n "Enter longitude: "
read long
var1="https://darksky.net/forecast/${lat},${long}/us12/en"
wget -q -O- ${var1} | grep -A 13 "latitude" > ammu.txt 

cat ammu.txt | grep -o "\"temperature\":[0-9][0-9]\.[0-9][0-9]" > ammu1.txt
cat ammu.txt | grep -o "\"summary\":\"[a-zA-Z ]*\"" > ammu2.txt
awk '{print $1;exit}' ammu1.txt
awk '{print $1;exit}' ammu2.txt
