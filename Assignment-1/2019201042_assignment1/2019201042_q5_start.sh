#!/bin/bash
sudo apt install openvpn
sudo sed -i '1s/^/nameserver 10.4.20.204\n/' /etc/resolv.conf
read -p "Enter Username:" un
read -p  "Enter password:" pwd

wget --user $un --password $pwd http://vpn.iiit.ac.in/secure/ubuntu.ovpn

sudo openvpn --config ubuntu.ovpn
