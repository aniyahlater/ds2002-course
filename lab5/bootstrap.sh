#!/bin/bash
/usr/bin/apt update -y
/usr/bin/apt upgrade -y
/usr/bin/apt install -y git
/usr/bin/python3 -m pip install pandas
# going to install python3
/usr/bin/apt install -y git python3 python3-dev python3-pip nfs-utils
# going to install boto3
/bin/pip3 install boto3 pandas requests
#i already installed git
# thus the three attempted installations are python3, boto3 and git

