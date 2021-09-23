#!/bin/bash

echo "doing pi-hole installation"

PI_HOLE_LOCAL_REPO="/etc/.pihole"

mkdir -p /etc/pihole/
mkdir -p /var/run/pihole
chmod 755 /usr/bin/pihole-FTL

export PIHOLE_SKIP_OS_CHECK=true
PH_TEST=true . "${PI_HOLE_LOCAL_REPO}/automated install/basic-install.sh"

if ! test -s $setupVars ; then
    echo "Need a configuration."
    exit 1
fi
source $setupVars

# Create pihole user/group
groupadd pihole
useradd -r --no-user-group -g pihole -s /usr/sbin/nologin pihole

export USER=pihole
LIGHTTPD_USER="lighttpd"
LIGHTTPD_GROUP="lighttpd"
LIGHTTPD_CFG="lighttpd.conf.fedora"

show_ascii_berry
useUpdateVars=true

installDefaultBlocklists
PRIVACY_LEVEL=0

enable_service lighttpd
LIGHTTPD_ENABLED=true

# Install FTL
chmod 644 "${PI_HOLE_CONFIG_DIR}/macvendor.db"
chown pihole:pihole "${PI_HOLE_CONFIG_DIR}/macvendor.db"
install -T -m 0755 "${PI_HOLE_LOCAL_REPO}/advanced/Templates/pihole-FTL.service" "/etc/init.d/pihole-FTL"
chkconfig pihole-FTL on

# Install Pi-Hole
installPihole

# auto-create gravity db if not present
sed -i -e '/^start()/a \  test -e /etc/pihole/gravity.db || /opt/pihole/gravity.sh --force' /etc/init.d/pihole-FTL

echo "WEBPASSWORD=$(HashPassword "pihole")" >> "${setupVars}"

exit 0
