#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git

git clone https://github.com/respeaker/seeed-voicecard
cd seeed-voicecard
sudo ./install.sh

cd
wget https://raw.githubusercontent.com/chad-hyer/public/main/.asoundrc

sudo raspi-config