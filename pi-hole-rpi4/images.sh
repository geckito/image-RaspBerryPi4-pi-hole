#!/bin/sh

test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

# disabled for now since dracut fails using busybox
# and we can not run it atm after dracut.

#/usr/bin/busybox.install / --hardlinks

echo -e 'STARTMODE=auto\nBOOTPROTO=dhcp\n' > /etc/sysconfig/network/ifcfg-eth0
echo pihole > /etc/hostname

baseService sshd on

bash /.pi-hole-install.sh

