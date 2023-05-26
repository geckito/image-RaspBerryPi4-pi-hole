#
# spec file for package pihole-FTL
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           pihole-FTL
Version:        1
Release:        0
Summary:        DNS services within the Pi-hole project
License:        EUPL-1.2
Group:          Productivity/Networking/DNS/Servers
Url:            https://github.com/pi-hole/FTL
#!RemoteAssetUrl: git+https://github.com/pi-hole/FTL#v5.19.2
Patch1:         fix-build.patch
BuildRequires:  cmake
BuildRequires:  libnettle-devel
BuildRequires:  gmp-devel
BuildRequires:  libidn-devel
BuildRequires:  libcap-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite3-devel
BuildRequires:  termcap


%description
FTLDNS (pihole-FTL) offers DNS services within the Pi-hole project. It provides blazing fast
DNS and DHCP services. It can also provide TFTP and more as the resolver part based on the
popular dnsmasq. Furthermore, FTL offers an interactive API where extensive network analysis
data and statistics may be queried.

%prep
%setup -n FTL -c -T
cp -a %_sourcedir/FTL/* .
%patch1 -p1

%build
mkdir -p cmake
cd cmake
cmake .. \
%if 0%{?is_cross}
    -DCMAKE_HOST_SYSTEM_PROCESSOR="%_build_cpu" \
    -DCMAKE_SYSTEM_PROCESSOR=%_target_cpu \
    -DCMAKE_C_COMPILER=%cross_gcc \
    -DCMAKE_MAKE_PROGRAM=/usr/bin/make \
    -DCMAKE_SYSROOT=%cross_sysroot
%endif

make

%install
cd cmake
make DESTDIR=%{buildroot} install VERBOSE=1

%files
%_bindir/pihole-FTL
