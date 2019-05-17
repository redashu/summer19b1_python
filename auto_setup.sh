#!/bin/bash

cat    <<EOF     >/etc/yum.repos.d/a.repo
[a]
baseurl=http://13.234.66.67/summer19/kubernetes/
gpgcheck=0

[ia]
baseurl=http://13.234.66.67/summer19/python3
gpgcheck=0



[iiiiia]
baseurl=http://13.234.66.67/summer19/rhel75
gpgcheck=0

EOF

yum   install  python3*   -y
pip3   install  jupyter  

