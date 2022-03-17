#!/bin/bash
if [ `whoami` != 'root' ]; then
    echo 'Permission denied. Please execute as root'
else
    git pull
    systemctl restart disConoha
fi
