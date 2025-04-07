#!/bin/sh
if [ "$1" = "build" ];then
    mkdir /home/changsheng/project/project21647/project
    cp -a /home/changsheng/project/project21647/server/. /home/changsheng/project/project21647/project/
    cd /home/changsheng/project/project21647/project
    rm -rf /home/changsheng/project/project21647/server
    echo "执行成功"
fi
