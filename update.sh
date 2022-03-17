#!/bin/bash
if [ ${EUID:-{$-UID}} != 0 ]; then
    echo 'Permission denied. Please execute as root'
fi

git pull
systemctl restart disConoha