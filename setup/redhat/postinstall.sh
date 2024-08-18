#!/bin/sh

set -e

FLECTRA_CONFIGURATION_DIR=/etc/sleektiv
FLECTRA_CONFIGURATION_FILE=$FLECTRA_CONFIGURATION_DIR/sleektiv.conf
FLECTRA_DATA_DIR=/var/lib/sleektiv
FLECTRA_GROUP="sleektiv"
FLECTRA_LOG_DIR=/var/log/sleektiv
FLECTRA_LOG_FILE=$FLECTRA_LOG_DIR/sleektiv-server.log
FLECTRA_USER="sleektiv"
ABI=$(rpm -q --provides python3 | awk '/abi/ {print $NF}')

if ! getent passwd | grep -q "^sleektiv:"; then
    groupadd $FLECTRA_GROUP
    adduser --system --no-create-home $FLECTRA_USER -g $FLECTRA_GROUP
fi
# Register "$FLECTRA_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $FLECTRA_USER" 2> /dev/null || true
# Configuration file
mkdir -p $FLECTRA_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $FLECTRA_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $FLECTRA_USER
db_password = False
addons_path = /usr/lib/python${ABI}/site-packages/sleektiv/addons
" > $FLECTRA_CONFIGURATION_FILE
    chown $FLECTRA_USER:$FLECTRA_GROUP $FLECTRA_CONFIGURATION_FILE
    chmod 0640 $FLECTRA_CONFIGURATION_FILE
fi
# Log
mkdir -p $FLECTRA_LOG_DIR
chown $FLECTRA_USER:$FLECTRA_GROUP $FLECTRA_LOG_DIR
chmod 0750 $FLECTRA_LOG_DIR
# Data dir
mkdir -p $FLECTRA_DATA_DIR
chown $FLECTRA_USER:$FLECTRA_GROUP $FLECTRA_DATA_DIR

INIT_FILE=/lib/systemd/system/sleektiv.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=Flectra Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=sleektiv
Group=sleektiv
ExecStart=/usr/bin/sleektiv --config $FLECTRA_CONFIGURATION_FILE --logfile $FLECTRA_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
