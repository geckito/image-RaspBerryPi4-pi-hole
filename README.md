Raspberry Pi4 Pi-Hole Image
===========================

See https://pi-hole.net/ for more information about Pi-Hole.

Pi-Hole needs a static ip address, please enter it into
pi-hole-rpi4/pi-hole.cfg file.

Build with pbuild and put the resulting image on the SD Card.
Enjoy.
Build it by executing:

```shell
 # pbuild
```

Deploy the image using 

```shell
 # dd_rescue _build.aarch64/k3s-image/*.raw /dev/YOUR_SD_CARD
```

You can setup network and sshd via usual Geckito procedure:

```shell
 # mount /dev/mmcblk0p2 /mnt
 # less /mnt/boot/README.txt & following
 # umount /mnt
```

