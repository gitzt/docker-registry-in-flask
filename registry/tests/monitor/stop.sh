#!/bin/bash

workdir=$(cd $(dirname $0); pwd)

if [ ! -f "${workdir}/monitor.pid" ];then
   echo '进程PID文件不存在！'
   exit 0
fi

PID=$(cat ${workdir}/monitor.pid)
if [ ! -n "$PID" ];then
  echo "未启动进程,请先启动进程"
  exit 0
fi

echo "当前启动的进程PID为$PID"
kill $PID

echo "" > ${workdir}/monitor.pid
echo 'monitor.py停止运行'
