#!/bin/sh
# . ~/.bashrc
echo "##############################################"
echo "                 start uwsgi                  "
echo "##############################################"

SCRIPT_HOME=$(cd "$(dirname "$0")"; pwd)
echo  $SCRIPT_HOME 

UWSGI=/Users/yezi/develop/uwsgi-1.0.4/uwsgi

$UWSGI --enable-threads -x $SCRIPT_HOME/../conf/deploy.xml:wsgi_app >> $SCRIPT_HOME/../logs/wsgi_app.log 2>&1 & 