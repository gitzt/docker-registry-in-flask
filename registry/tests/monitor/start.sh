#!/bin/bash

workdir=$(cd $(dirname $0); pwd)

if [ ! -f "${workdir}/monitor.pid" ];then
  echo 'PID文件不存在,请重新运行命令！'
  touch ${workdir}/monitor.pid
  exit 0
fi

PID=$(cat ${workdir}/monitor.pid)
if [ -n "$PID" ];then
  echo "服务已启动，请先停止"
  exit 0
fi

nohup python -u ${workdir}/monitor.py > ${workdir}/nohup.out 2>&1 &

echo "启动进程的PID为$!"
if [ $? -eq 0 ];then
  echo $! > ${workdir}/monitor.pid
  echo "启动成功!"
else
  echo "启动失败!"
fi
