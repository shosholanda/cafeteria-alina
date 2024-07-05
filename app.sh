#!/bin/bash
# Ejecutar una sola vez por sesión
# Entrar al ambiente
source ./cafe/bin/activate 
whoami
pwd
LOG="${HOME}/.logs"
echo $LOG


# Log file
if [ ! -d $LOG ]; then
    echo "Creando carpeta ./logs"
    mkdir $LOG
fi
LOGFILE="$HOME/.logs/cafeteria_alina.log"

# Levantar el servidor
nohup waitress-serve --host localhost --port=5000 --call main:cafeteria_alina > $LOGFILE 2>&1 &

# Wait for the server to start
date
sleep 5

# Check if the server is running
if ps aux | grep 'waitress-serve' | grep -v 'grep'; then
  echo "Server is running." >> $LOGFILE
else
  echo "Server failed to start." >> $LOGFILE
fi
