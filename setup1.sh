#!/bin/bash

sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install git

git clone https://github.com/respeaker/seeed-voicecard
cd seeed-voicecard
sudo ./install.sh
