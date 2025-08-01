#!/bin/bash

source /home/zhangjian22/sbt_setup.sh

echo "Entering TrueAsync simulator ..."
cd /home/zhangjian22/trueasync/

sbt "runMain $1 $2 $3"

echo ""
echo "Finished TrueAsync simulation."