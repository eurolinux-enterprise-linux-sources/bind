#
# Red Hat BIND package .spec file
#

#%%global PATCHVER P2
#%%global PREVER rc2
#%%global VERSION %{version}%{PREVER}
%global VERSION %{version}
#%%global VERSION %{version}-%{PATCHVER}

%{?!SDB:       %global SDB       1}
%{?!test:      %global test      0}
%{?!bind_uid:  %global bind_uid  25}
%{?!bind_gid:  %global bind_gid  25}
%{?!GSSTSIG:   %global GSSTSIG   1}
%{?!PKCS11:    %global PKCS11    1}
%{?!DEVEL:     %global DEVEL     1}
%global        bind_dir          /var/named
%global        chroot_prefix     %{bind_dir}/chroot
%global        selinuxbooleans   named_write_master_zones=1
%if %{SDB}
%global        chroot_sdb_prefix %{bind_dir}/chroot_sdb
%endif
#
Summary:  The Berkeley Internet Name Domain (BIND) DNS (Domain Name System) server
Name:     bind
License:  ISC
Version:  9.9.4
Release:  72%{?PATCHVER}%{?PREVER}%{?dist}
Epoch:    32
Url:      http://www.isc.org/products/BIND/
Buildroot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Group:    System Environment/Daemons
#
Source:   https://ftp.isc.org/isc/bind9/%{VERSION}/bind-%{VERSION}.tar.gz
Source1:  named.sysconfig
Source3:  named.logrotate
Source7:  bind-9.3.1rc1-sdb_tools-Makefile.in
Source8:  dnszone.schema
Source12: README.sdb_pgsql
Source25: named.conf.sample
Source26: named.conf
Source28: config-16.tar.bz2
# Up-to-date bind.keys from upstream
# Fetch a new one from page https://www.isc.org/bind-keys
Source29: bind.keys
Source30: ldap2zone.c
Source31: ldap2zone.1
Source32: named-sdb.8
Source33: zonetodb.1
Source34: zone2sqlite.1
Source35: bind.tmpfiles.d
Source36: trusted-key.key
Source37: named.service
Source38: named-chroot.service
Source39: named-sdb.service
Source40: named-sdb-chroot.service
Source41: setup-named-chroot.sh
Source42: generate-rndc-key.sh
Source43: named.rwtab
Source44: named-chroot-setup.service
Source45: named-sdb-chroot-setup.service
Source46: named-setup-rndc.service
Source47: named-pkcs11.service
# added due to GeoIP functionality tests
# patch tool does not support binary patches
Source48: geoip-testing-data.tar.xz

# Common patches
Patch5:  bind-nonexec.patch
Patch10: bind-9.5-PIE.patch
Patch16: bind-9.3.2-redhat_doc.patch
Patch72: bind-9.5-dlz-64bit.patch
Patch87: bind-9.5-parallel-build.patch
Patch101:bind-96-old-api.patch
Patch102:bind-95-rh452060.patch
Patch106:bind93-rh490837.patch
Patch109:bind97-rh478718.patch
Patch110:bind97-rh570851.patch
Patch111:bind97-exportlib.patch
Patch112:bind97-rh645544.patch
Patch119:bind97-rh693982.patch
Patch123:bind98-rh735103.patch
Patch124:bind93-rh726120.patch
# FIXME: This disables dlzexternal, which I will enable later again
# Make tests on all architectures and disable it
Patch127:bind99-forward.patch
Patch130:bind-9.9.1-P2-dlz-libdb.patch
Patch131:bind-9.9.1-P2-multlib-conflict.patch
Patch133:bind99-rh640538.patch
Patch134:bind97-rh669163.patch
Patch137:bind99-rrl.patch
# Install dns/update.h header for bind-dyndb-ldap plugin
Patch138:bind-9.9.3-include-update-h.patch
Patch139:bind99-ISC-Bugs-34738.patch
Patch140:bind99-ISC-Bugs-34870-v3.patch
Patch141:bind99-ISC-Bugs-35073.patch
Patch142:bind99-ISC-Bugs-35080.patch
Patch143:bind99-CVE-2014-0591.patch
Patch144:bind99-rh1067424.patch
Patch145:bind99-rh1072379.patch
Patch146:bind99-rh1098959.patch
Patch147:bind99-CVE-2014-8500.patch
Patch148:bind99-CVE-2015-1349.patch
Patch149:bind99-rh1215687-limits.patch
Patch154:bind99-rh1215164.patch
Patch155:bind99-rh1214827.patch
Patch156:bind99-CVE-2015-4620.patch
Patch157:bind99-CVE-2015-5477.patch
Patch158:bind-99-socket-maxevents.patch
Patch159:bind99-CVE-2015-5722.patch
Patch160:bind99-CVE-2015-8000.patch
Patch161:bind99-CVE-2015-8704.patch
Patch162:bind99-CVE-2016-1285-CVE-2016-1286.patch
Patch163:bind99-rh1291185.patch
Patch164:bind99-rh1259514.patch
Patch165:bind99-rh1306610.patch
Patch166:bind99-rh1220594-geoip.patch
Patch167:bind99-automatic-interface-scanning-rh1294506.patch
# commit 51bcc28543ce205f7af238ef2f3889ef020a0961 ISC 4467
patch168:bind99-CVE-2016-2776.patch
# commit bbb7c613b3e41495db627909660334695b48e60b ISC 4489
patch169:bind99-CVE-2016-8864.patch
# commit d372472f604d45f85b3bbae5d6f523fb561a8823 ISC 4508
patch170:bind99-CVE-2016-9131.patch
# commit a14b7f0187315767a1fa855f116fe937a7b402e3 ISC 4510
patch171:bind99-CVE-2016-9147.patch
# commit 69cb8ebf157183d9c36a9813f945348dd81b521f ISC 4517
Patch172:bind99-CVE-2016-9444.patch
# commit 2c74ad28efe5710ad04562c6f9902bc48d3be0ed ISC 4530
Patch173:bind99-rt43779.patch
# commit 062b04898be720ed0855efc192847fcbc667b3e1 ISC 4406
Patch174:bind99-CVE-2016-2775.patch
# ISC 4557
Patch175:bind99-CVE-2017-3135.patch
# ISC 4558
Patch176:bind99-rt44318.patch
# commit c550e75ade4ceb4ece96f660292799519a5c3183 ISC 4567
Patch177:bind99-rh1392362.patch
# commit 1f3ac11cb4ecfab52f517ebf78493b0f05318be2
Patch178:bind99-coverity-fixes2.patch
# ISC 4575
Patch179:bind99-CVE-2017-3136.patch
# ISC 4578
Patch180:bind99-CVE-2017-3137.patch
# commit 5e746ab61ed8158f784b86111fef95581a08b7dd ISC 3905
Patch181:bind99-rh1416304.patch
# ISC 4643
Patch182: bind99-CVE-2017-3142+3143.patch
# commit e3894cd3a92be79a64072835008ec589b17c601a
Patch183: bind99-rh1472862.patch
# commit 2fc1b8102d4bf02162012c27ab95e98a7438bd8f ISC 4647
Patch184: bind99-rh1476013.patch
# commit 51aed1827453f40ee56b165d45c5d58d96838d94
Patch185: bind99-rh1470637-tests.patch
# commit 51b00c6c783ccf5dca86119ff8f4f8b994298ca4 ISC 4712
Patch186: bind99-rh1470637.patch
# commit 6a3fa181d1253db5191139e20231512eebaddeeb ISC 3745
Patch187: bind99-rh1464850.patch
# commit 871f3c8beeb2134b17414ec167b90a57adb8e122 ISC 3980
Patch188: bind99-rh1464850-2.patch
# commit 4eb998928b9aef0ceda42d7529980d658138698a ISC 3525
Patch189: bind99-rh1501531.patch
# ISC 4858
Patch190: bind99-CVE-2017-3145.patch
Patch191: bind99-rh1510008.patch
Patch192: bind99-nta.patch
Patch193: bind99-rh1510008-2.patch
Patch194: bind99-fips.patch
Patch195: bind99-fips-tests.patch
# commit c3fbf330bc014f0470371e8da590d14a1d62977e ISC 4377
Patch196: bind99-rh1549130.patch
# commit cb735b3f902d4bb5f6e30328d5828d38efa63573
Patch197: bind99-rh1549130-2.patch
Patch198: bind99-CVE-2018-5740.patch

# Native PKCS#11 functionality from 9.10
Patch150:bind-9.9-allow_external_dnskey.patch
Patch151:bind-9.9-native-pkcs11.patch
Patch152:bind-9.9-dist-native-pkcs11.patch
Patch153:bind99-coverity-fixes.patch

# SDB patches
Patch11: bind-9.3.2b2-sdbsrc.patch
Patch12: bind-9.5-sdb.patch
Patch62: bind-9.5-sdb-sqlite-bld.patch

# needs inpection
Patch17: bind-9.3.2b1-fix_sdb_ldap.patch
Patch104: bind99-dyndb.patch

# IDN paches
Patch73: bind-9.5-libidn.patch
Patch83: bind-9.5-libidn2.patch
Patch85: bind-9.5-libidn3.patch
Patch94: bind95-rh461409.patch
Patch135:bind99-libidn4.patch

#
Requires(preun):  systemd
Requires(postun): systemd
Requires:       coreutils
Requires:       systemd-units
Requires(post): grep, systemd
Requires(post): shadow-utils
Requires(post): glibc-common
Requires(pre):  shadow-utils
Requires:       bind-libs = %{epoch}:%{version}-%{release}
Obsoletes:      bind-config < 30:9.3.2-34.fc6
Provides:       bind-config = 30:9.3.2-34.fc6
Obsoletes:      caching-nameserver < 31:9.4.1-7.fc8
Provides:       caching-nameserver = 31:9.4.1-7.fc8
Obsoletes:      dnssec-conf < 1.27-2
Provides:       dnssec-conf = 1.27-1
Requires:       python-ply
Provides:       python-isc = %{epoch}:%{version}-%{release}
Provides:       python-bind = %{epoch}:%{version}-%{release}
# selinux_set_booleans requires
Requires(post):      policycoreutils-python, libselinux-utils, selinux-policy
Requires(postun):    policycoreutils-python, libselinux-utils, selinux-policy
Requires(posttrans): policycoreutils-python, libselinux-utils, selinux-policy
BuildRequires:  openssl-devel, libtool, autoconf, pkgconfig, libcap-devel
BuildRequires:  libidn-devel, libxml2-devel, GeoIP-devel
BuildRequires:  systemd-units
BuildRequires:  python-ply
BuildRequires:  selinux-policy
%if %{SDB}
BuildRequires:  openldap-devel, postgresql-devel, sqlite-devel, mysql-devel
BuildRequires:  libdb-devel
%endif
%if %{test}
BuildRequires:  net-tools
%endif
%if %{GSSTSIG}
BuildRequires:  krb5-devel
%endif
# Needed to regenerate dig.1 manpage
BuildRequires: docbook-style-xsl, libxslt

%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.

%if %{PKCS11}
%package pkcs11
Summary: Bind with native PKCS#11 functionality for crypto
Group:   System Environment/Daemons
Requires: bind = %{epoch}:%{version}-%{release}
Requires: bind-libs = %{epoch}:%{version}-%{release}
Requires: bind-pkcs11-libs = %{epoch}:%{version}-%{release}

%description pkcs11
This is a version of BIND server built with native PKCS#11 functionality.
It is important to have SoftHSM v2+ installed and some token initialized.
For other supported HSM modules please check the BIND documentation.
This version of BIND binary is supported only in setup with the IPA server.

%package pkcs11-utils
Summary: Bind tools with native PKCS#11 for using DNSSEC
Group:   System Environment/Daemons
Requires: bind-pkcs11-libs = %{epoch}:%{version}-%{release}

%description pkcs11-utils
This is a set of PKCS#11 utilities that when used together create rsa
keys in a PKCS11 keystore. Also utilities for working with DNSSEC
compiled with native PKCS#11 functionality are included.

%package pkcs11-libs
Summary: Bind libraries compiled with native PKCS#11
Group:   System Environment/Daemons
Requires: bind-license = %{epoch}:%{version}-%{release}
Requires: bind-libs = %{epoch}:%{version}-%{release}

%description pkcs11-libs
This is a set of BIND libraries (dns, isc) compiled with native PKCS#11
functionality.

%package pkcs11-devel
Summary: Development files for Bind libraries compiled with native PKCS#11
Group:   System Environment/Daemons
Requires: bind-pkcs11-libs = %{epoch}:%{version}-%{release}

%description pkcs11-devel
This a set of development files for BIND libraries (dns, isc) compiled
with native PKCS#11 functionality.
%endif

%if %{SDB}
%package sdb
Summary: BIND server with database backends and DLZ support
Group:   System Environment/Daemons
Requires: bind
Requires: bind-libs = %{epoch}:%{version}-%{release}
Requires: systemd-units

%description sdb
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named-sdb)
which has compiled-in SDB (Simplified Database Backend) which includes
support for using alternative Zone Databases stored in an LDAP server
(ldapdb), a postgreSQL database (pgsqldb), an sqlite database (sqlitedb),
or in the filesystem (dirdb), in addition to the standard in-memory RBT
(Red Black Tree) zone database. It also includes support for DLZ
(Dynamic Loadable Zones)
%endif

%package libs-lite
Summary:  Libraries for working with the DNS protocol
Group:    Applications/System
Obsoletes:bind-libbind-devel < 31:9.3.3-4.fc7
Provides: bind-libbind-devel = 31:9.3.3-4.fc7
Requires: bind-license = %{epoch}:%{version}-%{release}

%description libs-lite
Contains lite version of BIND suite libraries which are used by various
programs to work with DNS protocol.

%package libs
Summary: Libraries used by the BIND DNS packages
Group:    Applications/System
Requires: bind-license = %{epoch}:%{version}-%{release}

%description libs
Contains heavyweight version of BIND suite libraries used by both named DNS
server and utilities in bind-utils package.

%package license
Summary:  License of the BIND DNS suite
Group:    Applications/System
BuildArch:noarch

%description license
Contains license of the BIND DNS suite.

%package utils
Summary: Utilities for querying DNS name servers
Group:   Applications/System
Requires: bind-libs = %{epoch}:%{version}-%{release}

%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain
Name System) name servers to find out information about Internet
hosts. These tools will provide you with the IP addresses for given
host names, as well as other information about registered domains and
network addresses.

You should install bind-utils if you need to get information from DNS name
servers.

%if %{DEVEL}
%package devel
Summary:  Header files and libraries needed for BIND DNS development
Group:    Development/Libraries
Obsoletes:bind-libbind-devel < 31:9.3.3-4.fc7
Provides: bind-libbind-devel = 31:9.3.3-4.fc7
Requires: bind-libs = %{epoch}:%{version}-%{release}

%description devel
The bind-devel package contains full version of the header files and libraries
required for development with ISC BIND 9
%endif

%package lite-devel
Summary:  Lite version of header files and libraries needed for BIND DNS development
Group:    Development/Libraries
Requires: bind-libs-lite = %{epoch}:%{version}-%{release}

%description lite-devel
The bind-lite-devel package contains lite version of the header
files and libraries required for development with ISC BIND 9

%package chroot
Summary:        A chroot runtime environment for the ISC BIND DNS server, named(8)
Group:          System Environment/Daemons
Prefix:         %{chroot_prefix}
Requires(post): grep
Requires(preun):grep
Requires:       bind = %{epoch}:%{version}-%{release}
Requires:       systemd-units

%description chroot
This package contains a tree of files which can be used as a
chroot(2) jail for the named(8) program from the BIND package.
Based on the code from Jan "Yenya" Kasprzak <kas@fi.muni.cz>

%if %{SDB}
%package sdb-chroot
Summary:        A chroot runtime environment for the ISC BIND DNS server, named-sdb(8)
Group:          System Environment/Daemons
Prefix:         %{chroot_prefix}
Requires:       bind-sdb
Requires:       systemd-units

%description sdb-chroot
This package contains a tree of files which can be used as a
chroot(2) jail for the named-sdb(8) program from the BIND package.
Based on the code from Jan "Yenya" Kasprzak <kas@fi.muni.cz>
%endif


%prep
%setup -q -n %{name}-%{VERSION}

# Common patches
%patch5 -p1 -b .nonexec
%patch10 -p1 -b .PIE
%patch16 -p1 -b .redhat_doc
%ifnarch alpha ia64
%patch72 -p1 -b .64bit
%endif
%patch73 -p1 -b .libidn
%patch83 -p1 -b .libidn2
%patch85 -p1 -b .libidn3
%patch87 -p1 -b .parallel
%patch94 -p1 -b .rh461409

%patch102 -p1 -b .rh452060
%patch106 -p0 -b .rh490837
%patch109 -p1 -b .rh478718
%patch110 -p1 -b .rh570851
%patch111 -p1 -b .exportlib
%patch112 -p1 -b .rh645544
%patch119 -p1 -b .rh693982
%patch123 -p1 -b .rh735103
%patch124 -p1 -b .rh726120
%patch127 -p1 -b .forward
%patch130 -p1 -b .libdb
%patch131 -p1 -b .multlib-conflict
%patch137 -p1 -b .rrl
%patch138 -p1 -b .update
%patch139 -p1 -b .journal
%patch140 -p1 -b .send_buffers
%patch141 -p1 -b .leak_35073
%patch142 -p1 -b .rbt_crash
%patch143 -p1 -b .CVE-2014-059
%patch144 -p1 -b .rh1067424
%patch145 -p1 -b .rh1072379
%patch146 -p1 -b .rh1098959
%patch147 -p1 -b .CVE-2014-8500
%patch148 -p1 -b .CVE-2015-1349
%patch149 -p1 -b .rh1215687-limits

%patch150 -p1 -b .external_key
%patch151 -p1 -b .native_pkcs11
# http://cov01.lab.eng.brq.redhat.com/covscanhub/waiving/9377/
%patch153 -p1 -b .coverity_9377
%patch154 -p1 -b .rh1215164
%patch155 -p1 -b .nsupdate_realm
%patch156 -p1 -b .CVE-2015-4620
%patch157 -p1 -b .CVE-2015-5477
%patch158 -p1 -b .sock-maxevents
%patch159 -p1 -b .CVE-2015-5722
%patch160 -p1 -b .CVE-2015-8000
%patch161 -p1 -b .CVE-2015-8704
%patch162 -p1 -b .CVE-2016-1285-CVE-2016-1286
%patch163 -p1 -b .rh1291185
%patch164 -p1 -b .rh1259514
%patch165 -p1 -b .rh1306610-caa
%patch104 -p1 -b .dyndb

# GeoIP support
%patch166 -p1 -b .rh1220594-geoip
# extract the binary testing data
tar -xf %{SOURCE48} -C bin/tests/system/geoip/data

%patch167 -p1 -b .rh1294506
%patch168 -p1 -b .CVE-2016-2776
%patch169 -p1 -b .CVE-2016-8864
%patch170 -p1 -b .CVE-2016-9131
%patch171 -p1 -b .CVE-2016-9147
%patch172 -p1 -b .CVE-2016-9444
%patch173 -p1 -b .rt43779
%patch174 -p1 -b .CVE-2016-2775
%patch175 -p1 -b .CVE-2017-3135
%patch176 -p1 -b .rt44318
%patch177 -p1 -b .rh1392362
%patch178 -p1 -b .coverity2
%patch179 -p1 -b .CVE-2017-3136
%patch180 -p1 -b .CVE-2017-3137
%patch181 -p1 -b .rh1416304
%patch182 -p1 -b .CVE-2017-3142+3143
%patch183 -p1 -b .rh1472862
%patch184 -p1 -b .rh1476013
%patch185 -p1 -b .rh1470637-tests
%patch186 -p1 -b .rh1470637
%patch187 -p1 -b .rh1464850
%patch188 -p1 -b .rh1464850
%patch189 -p1 -b .rh1501531
%patch190 -p1 -b .CVE-2017-3145
%patch191 -p1 -b .dnssec-keymgr
%patch192 -p1 -b .rh1452091
%patch193 -p1 -b .dnssec-keymgr-2
%patch194 -p1 -b .fips
%patch195 -p1 -b .fips-tests
%patch196 -p1 -b .rh1549130
%patch197 -p1 -b .rh1549130-2
%patch198 -p1 -b .CVE-2018-5740

# Override upstream builtin keys
cp -fp %{SOURCE29} bind.keys

%if %{PKCS11}
cp -r bin/named{,-pkcs11}
cp -r bin/dnssec{,-pkcs11}
cp -r lib/isc{,-pkcs11}
cp -r lib/dns{,-pkcs11}
cp -r lib/export/isc{,-pkcs11}
cp -r lib/export/dns{,-pkcs11}
%patch152 -p1 -b .dist_pkcs11
%endif

%if %{SDB}
%patch101 -p1 -b .old-api
mkdir bin/named-sdb
cp -r bin/named/* bin/named-sdb
%patch11 -p1 -b .sdbsrc
# SDB ldap
cp -fp contrib/sdb/ldap/ldapdb.[ch] bin/named-sdb
# SDB postgreSQL
cp -fp contrib/sdb/pgsql/pgsqldb.[ch] bin/named-sdb
# SDB sqlite
cp -fp contrib/sdb/sqlite/sqlitedb.[ch] bin/named-sdb
# SDB Berkeley DB - needs to be ported to DB4!
#cp -fp contrib/sdb/bdb/bdb.[ch] bin/named_sdb
# SDB dir
cp -fp contrib/sdb/dir/dirdb.[ch] bin/named-sdb
# SDB tools
mkdir -p bin/sdb_tools
cp -fp %{SOURCE30} bin/sdb_tools/ldap2zone.c
cp -fp %{SOURCE7} bin/sdb_tools/Makefile.in
#cp -fp contrib/sdb/bdb/zone2bdb.c bin/sdb_tools
cp -fp contrib/sdb/ldap/{zone2ldap.1,zone2ldap.c} bin/sdb_tools
cp -fp contrib/sdb/pgsql/zonetodb.c bin/sdb_tools
cp -fp contrib/sdb/sqlite/zone2sqlite.c bin/sdb_tools
%patch12 -p1 -b .sdb
%endif
%if %{SDB}
%patch17 -p1 -b .fix_sdb_ldap
%endif
%if %{SDB}
%patch62 -p1 -b .sdb-sqlite-bld
%endif
%patch133 -p1 -b .rh640538
%patch134 -p1 -b .rh669163
%patch135 -p1 -b .libidn4

# Sparc and s390 arches need to use -fPIE
%ifarch sparcv9 sparc64 s390 s390x
for i in bin/named{,-sdb}/{,unix}/Makefile.in; do
  sed -i 's|fpie|fPIE|g' $i
done
%endif

:;

%build
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
export CPPFLAGS="$CPPFLAGS -DDIG_SIGCHASE"
export STD_CDEFINES="$CPPFLAGS"

sed -i -e \
's/RELEASEVER=\(.*\)/RELEASEVER=\1-RedHat-%{version}-%{release}/' \
version

libtoolize -c -f; aclocal -I libtool.m4 --force; autoconf -f

%configure \
  --with-libtool \
  --localstatedir=/var \
  --enable-threads \
  --with-geoip \
  --enable-ipv6 \
  --enable-filter-aaaa \
  --enable-rrl \
  --with-pic \
  --disable-static \
  --disable-openssl-version-check \
  --enable-exportlib \
  --with-export-libdir=%{_libdir} \
  --with-export-includedir=%{_includedir} \
  --includedir=%{_includedir}/bind9 \
%if %{PKCS11}
  --enable-native-pkcs11 \
  --with-pkcs11=%{_libdir}/pkcs11/libsofthsm2.so \
%endif
%if %{SDB}
  --with-dlopen=yes \
  --with-dlz-ldap=yes \
  --with-dlz-postgres=yes \
  --with-dlz-mysql=yes \
  --with-dlz-filesystem=yes \
  --with-dlz-bdb=yes \
%endif
%if %{GSSTSIG}
  --with-gssapi=yes \
  --disable-isc-spnego \
%endif
  --enable-fixed-rrset \
  --with-tuning=large \
  --with-docbook-xsl=%{_datadir}/sgml/docbook/xsl-stylesheets \
;
make %{?_smp_mflags}

# Regenerate dig.1 manpage
pushd bin/dig
make man
popd
pushd bin/python
make man
popd

%if %{test}
%check
if [ "`whoami`" = 'root' ]; then
  set -e
  chmod -R a+rwX .
  pushd bin/tests
  pushd system
  ./ifconfig.sh up
  popd
  make test
  e=$?
  pushd system
  ./ifconfig.sh down
  popd
  popd
  if [ "$e" -ne 0 ]; then
    echo "ERROR: this build of BIND failed 'make test'. Aborting."
    exit $e;
  fi;
else
  echo 'only root can run the tests (they require an ifconfig).'
%endif

%install
rm -rf ${RPM_BUILD_ROOT}

# Build directory hierarchy
mkdir -p ${RPM_BUILD_ROOT}/etc/logrotate.d
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bind
mkdir -p ${RPM_BUILD_ROOT}/var/named/{slaves,data,dynamic}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/{man1,man5,man8}
mkdir -p ${RPM_BUILD_ROOT}/run/named
mkdir -p ${RPM_BUILD_ROOT}/var/log

#chroot
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/{dev,etc,var,run/named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/var/{log,named,tmp}

# create symlink as it is on real filesystem
pushd ${RPM_BUILD_ROOT}/%{chroot_prefix}/var
ln -s ../run run
popd

mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/etc/{pki/dnssec-keys,named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/%{_libdir}/bind
# these are required to prevent them being erased during upgrade of previous
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/null
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/random
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/zero
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/etc/named.conf
#end chroot

#sdb-chroot
%if %{SDB}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/{dev,etc,var,run/named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/var/{log,named,tmp}

# create symlink as it is on real filesystem
pushd ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/var
ln -s ../run run
popd

mkdir -p ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/etc/{pki/dnssec-keys,named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/%{_libdir}/bind
# these are required to prevent them being erased during upgrade of previous
touch ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/dev/null
touch ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/dev/random
touch ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/dev/zero
touch ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/etc/named.conf
%endif
#end sdb-chroot

make DESTDIR=${RPM_BUILD_ROOT} install

# Remove unwanted files
rm -f ${RPM_BUILD_ROOT}/etc/bind.keys

# Systemd unit files
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE37} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE38} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE44} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE46} ${RPM_BUILD_ROOT}%{_unitdir}

%if %{SDB}
install -m 644 %{SOURCE39} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE40} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE45} ${RPM_BUILD_ROOT}%{_unitdir}
%endif
%if %{PKCS11}
install -m 644 %{SOURCE47} ${RPM_BUILD_ROOT}%{_unitdir}
%endif

mkdir -p ${RPM_BUILD_ROOT}%{_libexecdir}
install -m 755 %{SOURCE41} ${RPM_BUILD_ROOT}%{_libexecdir}/setup-named-chroot.sh
install -m 755 %{SOURCE42} ${RPM_BUILD_ROOT}%{_libexecdir}/generate-rndc-key.sh

install -m 644 %SOURCE3 ${RPM_BUILD_ROOT}/etc/logrotate.d/named
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/named
%if %{SDB}
mkdir -p ${RPM_BUILD_ROOT}/etc/openldap/schema
install -m 644 %{SOURCE8} ${RPM_BUILD_ROOT}/etc/openldap/schema/dnszone.schema
install -m 644 %{SOURCE12} contrib/sdb/pgsql/
%endif

# Install isc/errno2result.h header
install -m 644 lib/isc/unix/errno2result.h ${RPM_BUILD_ROOT}%{_includedir}/isc

# Files required to run test-suite outside of build tree:
cp -fp config.h ${RPM_BUILD_ROOT}/%{_includedir}/bind9
cp -fp lib/dns/include/dns/forward.h ${RPM_BUILD_ROOT}/%{_includedir}/dns
cp -fp lib/isc/unix/include/isc/keyboard.h ${RPM_BUILD_ROOT}/%{_includedir}/isc

# Remove libtool .la files:
find ${RPM_BUILD_ROOT}/%{_libdir} -name '*.la' -exec '/bin/rm' '-f' '{}' ';';

# Remove -devel files out of buildroot if not needed
%if !%{DEVEL}
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/bind9/*so
rm -rf ${RPM_BUILD_ROOT}/%{_includedir}/bind9
rm -f ${RPM_BUILD_ROOT}/%{_mandir}/man1/isc-config.sh.1*
rm -f ${RPM_BUILD_ROOT}/%{_mandir}/man3/lwres*
rm -f ${RPM_BUILD_ROOT}/%{_bindir}/isc-config.sh
%endif

# SDB manpages
%if %{SDB}
install -m 644 %{SOURCE31} ${RPM_BUILD_ROOT}%{_mandir}/man1/ldap2zone.1
install -m 644 %{SOURCE32} ${RPM_BUILD_ROOT}%{_mandir}/man8/named-sdb.8
install -m 644 %{SOURCE33} ${RPM_BUILD_ROOT}%{_mandir}/man1/zonetodb.1
install -m 644 %{SOURCE34} ${RPM_BUILD_ROOT}%{_mandir}/man1/zone2sqlite.1
%endif

# PKCS11 versions manpages
%if %{PKCS11}
pushd ${RPM_BUILD_ROOT}%{_mandir}/man8
ln -s named.8.gz named-pkcs11.8.gz
ln -s dnssec-checkds.8.gz dnssec-checkds-pkcs11.8.gz
ln -s dnssec-coverage.8.gz dnssec-coverage-pkcs11.8.gz
ln -s dnssec-dsfromkey.8.gz dnssec-dsfromkey-pkcs11.8.gz
ln -s dnssec-keyfromlabel.8.gz dnssec-keyfromlabel-pkcs11.8.gz
ln -s dnssec-keygen.8.gz dnssec-keygen-pkcs11.8.gz
ln -s dnssec-revoke.8.gz dnssec-revoke-pkcs11.8.gz
ln -s dnssec-settime.8.gz dnssec-settime-pkcs11.8.gz
ln -s dnssec-signzone.8.gz dnssec-signzone-pkcs11.8.gz
ln -s dnssec-verify.8.gz dnssec-verify-pkcs11.8.gz
ln -s dnssec-importkey.8.gz dnssec-importkey-pkcs11.8.gz
popd
%endif

# Ghost config files:
touch ${RPM_BUILD_ROOT}%{_localstatedir}/log/named.log

# configuration files:
tar -C ${RPM_BUILD_ROOT} -xjf %{SOURCE28}
touch ${RPM_BUILD_ROOT}/etc/rndc.key
touch ${RPM_BUILD_ROOT}/etc/rndc.conf
mkdir ${RPM_BUILD_ROOT}/etc/named
install -m 640 %{SOURCE26} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.conf
install -m 644 bind.keys ${RPM_BUILD_ROOT}/etc/named.iscdlv.key
install -m 644 %{SOURCE36} ${RPM_BUILD_ROOT}/etc/trusted-key.key

# sample bind configuration files for %%doc:
mkdir -p sample/etc sample/var/named/{data,slaves}
install -m 644 %{SOURCE25} sample/etc/named.conf
# Copy default configuration to %%doc to make it usable from system-config-bind
install -m 644 %{SOURCE26} named.conf.default
install -m 644 ${RPM_BUILD_ROOT}/etc/named.rfc1912.zones sample/etc/named.rfc1912.zones
install -m 644 ${RPM_BUILD_ROOT}/var/named/{named.ca,named.localhost,named.loopback,named.empty}  sample/var/named
for f in my.internal.zone.db slaves/my.slave.internal.zone.db slaves/my.ddns.internal.zone.db my.external.zone.db; do 
  echo '@ in soa localhost. root 1 3H 15M 1W 1D
  ns localhost.' > sample/var/named/$f; 
done
:;

mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
install -m 644 %{SOURCE35} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/named.conf

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d
install -m 644 %{SOURCE43} ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d/named

%pre
if [ "$1" -eq 1 ]; then
  /usr/sbin/groupadd -g %{bind_gid} -f -r named >/dev/null 2>&1 || :;
  /usr/sbin/useradd  -u %{bind_uid} -r -N -M -g named -s /bin/false -d /var/named -c Named named >/dev/null 2>&1 || :;
fi;
:;

%post
/sbin/ldconfig
if [ "$1" -eq 1 ]; then
  # Initial installation
  [ -x /sbin/restorecon ] && /sbin/restorecon /etc/rndc.* /etc/named.* >/dev/null 2>&1 ;
  # rndc.key has to have correct perms and ownership, CVE-2007-6283
  [ -e /etc/rndc.key ] && chown root:named /etc/rndc.key
  [ -e /etc/rndc.key ] && chmod 0640 /etc/rndc.key
else
  # Upgrade, use invalid shell
  if getent passwd named | grep ':/sbin/nologin$' >/dev/null; then
    usermod -s /bin/false named
  fi
fi
%systemd_post named.service
:;

%preun
# Package removal, not upgrade
%systemd_preun named.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart named.service
# Unset on both upgrade and install. Boolean would be unset from now
# until %posttrans on upgrade. Write requests might fail during update.
(export LC_ALL=C; %{selinux_unset_booleans %{selinuxbooleans}})

%posttrans
# selinux-policy-targeted is required for following macro to work.
# This package should not depend on it explicitly, but anaconda ensures
# it is installed. Run after all packages are installed.
(export LC_ALL=C; %{selinux_set_booleans %{selinuxbooleans}})

%if %{SDB}
%post sdb
# Initial installation 
%systemd_post named-sdb.service

%preun sdb
# Package removal, not upgrade
%systemd_preun named-sdb.service

%postun sdb
# Package upgrade, not uninstall
%systemd_postun_with_restart named-sdb.service
%endif

%if %{PKCS11}
%post pkcs11
# Initial installation
%systemd_post named-pkcs11.service

%preun pkcs11
# Package removal, not upgrade
%systemd_preun named-pkcs11.service

%postun pkcs11
# Package upgrade, not uninstall
%systemd_postun_with_restart named-pkcs11.service
%endif

%triggerpostun -n bind -- bind <= 32:9.5.0-20.b1
if [ "$1" -gt 0 ]; then
  [ -e /etc/rndc.key ] && chown root:named /etc/rndc.key
  [ -e /etc/rndc.key ] && chmod 0640 /etc/rndc.key
fi
:;

%triggerun -- bind < 32:9.9.0-0.6.rc1
/sbin/chkconfig --del named >/dev/null 2>&1 || :
/bin/systemctl try-restart named.service >/dev/null 2>&1 || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post libs-lite -p /sbin/ldconfig

%postun libs-lite -p /sbin/ldconfig

%pre chroot
# updating
if [ "$1" -gt 1 ]; then
    # if %%{chroot_prefix}/var/run is a directory, remove it
    # fix for Bug #1091341
    if [ -d %{chroot_prefix}/var/run ]; then
        rm -rf %{chroot_prefix}/var/run
    fi
fi

%post chroot
%systemd_post named-chroot.service
if [ "$1" -gt 0 ]; then
  [ -e %{chroot_prefix}/dev/random ] || \
    /bin/mknod %{chroot_prefix}/dev/random c 1 8
  [ -e %{chroot_prefix}/dev/zero ] || \
    /bin/mknod %{chroot_prefix}/dev/zero c 1 5
  [ -e %{chroot_prefix}/dev/null ] || \
    /bin/mknod %{chroot_prefix}/dev/null c 1 3
fi;
:;

%posttrans chroot
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon %{chroot_prefix}/dev/* > /dev/null 2>&1;
fi;
:;

%preun chroot
%systemd_preun named-chroot.service 
if [ "$1" -eq 0 ]; then
  # Package removal, not upgrade
  rm -f %{chroot_prefix}/dev/{random,zero,null}
fi
:;

%postun chroot
# Package upgrade, not uninstall
%systemd_postun_with_restart named-chroot.service


%if %{SDB}

%post sdb-chroot
%systemd_post named-sdb-chroot.service
if [ "$1" -gt 0 ]; then
  [ -e %{chroot_sdb_prefix}/dev/random ] || \
    /bin/mknod %{chroot_sdb_prefix}/dev/random c 1 8
  [ -e %{chroot_sdb_prefix}/dev/zero ] || \
    /bin/mknod %{chroot_sdb_prefix}/dev/zero c 1 5
  [ -e %{chroot_sdb_prefix}/dev/null ] || \
    /bin/mknod %{chroot_sdb_prefix}/dev/null c 1 3
fi;
:;

%posttrans sdb-chroot
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon %{chroot_sdb_prefix}/dev/* > /dev/null 2>&1;
fi;
:;

%preun sdb-chroot
%systemd_preun named-sdb-chroot.service 
if [ "$1" -eq 0 ]; then
  # Package removal, not upgrade
  rm -f %{chroot_sdb_prefix}/dev/{random,zero,null}
fi
:;

%postun sdb-chroot
# Package upgrade, not uninstall
%systemd_postun_with_restart named-sdb-chroot.service

%endif

%clean
rm -rf ${RPM_BUILD_ROOT}
:;

%files
%defattr(-,root,root,-)
%{_libdir}/bind
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/named
%config(noreplace) %attr(0644,root,named) %{_sysconfdir}/named.iscdlv.key
%config(noreplace) %attr(0644,root,named) %{_sysconfdir}/named.root.key
%{_tmpfilesdir}/named.conf
%{_sysconfdir}/rwtab.d/named
%{_unitdir}/named.service
%{_unitdir}/named-setup-rndc.service
%{_sbindir}/arpaname
%{_sbindir}/ddns-confgen
%{_sbindir}/genrandom
%{_sbindir}/named-journalprint
%{_sbindir}/nsec3hash
%{_sbindir}/dnssec*
%exclude %{_sbindir}/dnssec*pkcs11
%{_sbindir}/named-check*
%{_sbindir}/lwresd
%{_sbindir}/named
%{_sbindir}/rndc*
%{_sbindir}/named-compilezone
%{_sbindir}/isc-hmac-fixup
%{_libexecdir}/generate-rndc-key.sh
%{python_sitelib}/isc/
%{python_sitelib}/*.egg-info
%{_mandir}/man1/arpaname.1*
%{_mandir}/man5/named.conf.5*
%{_mandir}/man5/rndc.conf.5*
%{_mandir}/man8/rndc.8*
%{_mandir}/man8/named.8*
%{_mandir}/man8/lwresd.8*
%{_mandir}/man8/dnssec*.8*
%exclude %{_mandir}/man8/dnssec*-pkcs11.8*
%{_mandir}/man8/named-checkconf.8*
%{_mandir}/man8/named-checkzone.8*
%{_mandir}/man8/named-compilezone.8*
%{_mandir}/man8/rndc-confgen.8*
%{_mandir}/man8/ddns-confgen.8*
%{_mandir}/man8/genrandom.8*
%{_mandir}/man8/named-journalprint.8*
%{_mandir}/man8/nsec3hash.8*
%{_mandir}/man8/isc-hmac-fixup.8*
%doc CHANGES README named.conf.default
%doc doc/arm/*html doc/arm/*pdf
%doc sample/

# Hide configuration
%defattr(0640,root,named,0750)
%dir %{_sysconfdir}/named
%config(noreplace) %verify(not link) %{_sysconfdir}/named.conf
%config(noreplace) %verify(not link) %{_sysconfdir}/named.rfc1912.zones
%defattr(0660,root,named,01770)
%dir %{_localstatedir}/named
%defattr(0660,named,named,0770)
%dir %{_localstatedir}/named/slaves
%dir %{_localstatedir}/named/data
%dir %{_localstatedir}/named/dynamic
%ghost %{_localstatedir}/log/named.log
%defattr(0640,root,named,0750)
%config %verify(not link) %{_localstatedir}/named/named.ca
%config %verify(not link) %{_localstatedir}/named/named.localhost
%config %verify(not link) %{_localstatedir}/named/named.loopback
%config %verify(not link) %{_localstatedir}/named/named.empty
%ghost %config(noreplace) %{_sysconfdir}/rndc.key
# ^- rndc.key now created on first install only if it does not exist
# %%verify(not size,not md5) %%config(noreplace) %%attr(0640,root,named) /etc/rndc.conf
# ^- Let the named internal default rndc.conf be used -
#    rndc.conf not required unless it differs from default.
%ghost %config(noreplace) %{_sysconfdir}/rndc.conf
# ^- The default rndc.conf which uses rndc.key is in named's default internal config -
#    so rndc.conf is not necessary.
%config(noreplace) %{_sysconfdir}/logrotate.d/named
%defattr(-,named,named,-)
%dir /run/named

%if %{SDB}
%files sdb
%defattr(-,root,root,-)
%{_unitdir}/named-sdb.service
%{_mandir}/man1/zone2ldap.1*
%{_mandir}/man1/ldap2zone.1*
%{_mandir}/man1/zonetodb.1*
%{_mandir}/man1/zone2sqlite.1*
%{_mandir}/man8/named-sdb.8*
%doc contrib/sdb/ldap/README.ldap contrib/sdb/ldap/INSTALL.ldap contrib/sdb/pgsql/README.sdb_pgsql
%dir %{_sysconfdir}/openldap/schema
%config(noreplace) %{_sysconfdir}/openldap/schema/dnszone.schema
%{_sbindir}/named-sdb
%{_sbindir}/zone2ldap
%{_sbindir}/ldap2zone
%{_sbindir}/zonetodb
%{_sbindir}/zone2sqlite
%endif

%files libs
%defattr(-,root,root,-)
%{_libdir}/*so.*
%exclude %{_libdir}/*export.so.*
%exclude %{_libdir}/*pkcs11.so.*
%exclude %{_libdir}/*pkcs11-export.so.*

%files libs-lite
%defattr(-,root,root,-)
%{_libdir}/*export.so.*
%exclude %{_libdir}/*pkcs11-export.so.*

%files license
%defattr(-,root,root,-)
%doc COPYRIGHT

%files utils
%defattr(-,root,root,-)
%{_bindir}/dig
%{_bindir}/host
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_mandir}/man1/host.1*
%{_mandir}/man1/nsupdate.1*
%{_mandir}/man1/dig.1*
%{_mandir}/man1/nslookup.1*
%{_sysconfdir}/trusted-key.key

%if %{DEVEL}
%files devel
%defattr(-,root,root,-)
%{_libdir}/*so
%exclude %{_libdir}/*export.so
%exclude %{_libdir}/*pkcs11.so
%exclude %{_libdir}/*pkcs11-export.so
%{_includedir}/bind9
%exclude %{_includedir}/bind9/pkcs11
%exclude %{_includedir}/bind9/pk11
%{_mandir}/man1/isc-config.sh.1*
%{_mandir}/man3/lwres*
%{_bindir}/isc-config.sh
%endif

%files lite-devel
%defattr(-,root,root,-)
%{_libdir}/*export.so
%exclude %{_libdir}/*pkcs11-export.so
%{_includedir}/dns
%{_includedir}/dst
%{_includedir}/irs
%{_includedir}/isc
%{_includedir}/isccfg

%files chroot
%defattr(-,root,root,-)
%{_unitdir}/named-chroot.service
%{_unitdir}/named-chroot-setup.service
%{_libexecdir}/setup-named-chroot.sh
%ghost %{chroot_prefix}/dev/null
%ghost %{chroot_prefix}/dev/random
%ghost %{chroot_prefix}/dev/zero
%defattr(0640,root,named,0750)
%dir %{chroot_prefix}
%dir %{chroot_prefix}/dev
%dir %{chroot_prefix}/etc
%dir %{chroot_prefix}/etc/named
%dir %{chroot_prefix}/etc/pki
%dir %{chroot_prefix}/etc/pki/dnssec-keys
%dir %{chroot_prefix}/var
%dir %{chroot_prefix}/run
%ghost %config(noreplace) %{chroot_prefix}/etc/named.conf
%defattr(-,root,root,-)
%dir %{chroot_prefix}/usr
%dir %{chroot_prefix}/%{_libdir}
%dir %{chroot_prefix}/%{_libdir}/bind
%defattr(0660,root,named,01770)
%dir %{chroot_prefix}/var/named
%defattr(0660,named,named,0770)
%dir %{chroot_prefix}/var/tmp
%dir %{chroot_prefix}/var/log
%defattr(-,named,named,-)
%dir %{chroot_prefix}/run/named
%{chroot_prefix}/var/run

%if %{SDB}
%files sdb-chroot
%defattr(-,root,root,-)
%{_unitdir}/named-sdb-chroot.service
%{_unitdir}/named-sdb-chroot-setup.service
%{_libexecdir}/setup-named-chroot.sh
%ghost %{chroot_sdb_prefix}/dev/null
%ghost %{chroot_sdb_prefix}/dev/random
%ghost %{chroot_sdb_prefix}/dev/zero
%defattr(0640,root,named,0750)
%dir %{chroot_sdb_prefix}
%dir %{chroot_sdb_prefix}/dev
%dir %{chroot_sdb_prefix}/etc
%dir %{chroot_sdb_prefix}/etc/named
%dir %{chroot_sdb_prefix}/etc/pki
%dir %{chroot_sdb_prefix}/etc/pki/dnssec-keys
%dir %{chroot_sdb_prefix}/var
%dir %{chroot_sdb_prefix}/run
%ghost %config(noreplace) %{chroot_sdb_prefix}/etc/named.conf
%defattr(0660,root,named,01770)
%dir %{chroot_sdb_prefix}/var/named
%defattr(-,root,root,-)
%dir %{chroot_sdb_prefix}/usr
%dir %{chroot_sdb_prefix}/%{_libdir}
%dir %{chroot_sdb_prefix}/%{_libdir}/bind
%defattr(0660,named,named,0770)
%dir %{chroot_sdb_prefix}/var/tmp
%dir %{chroot_sdb_prefix}/var/log
%defattr(-,named,named,-)
%dir %{chroot_sdb_prefix}/run/named
%{chroot_sdb_prefix}/var/run
%endif

%if %{PKCS11}
%files pkcs11
%defattr(-,root,root,-)
%{_sbindir}/named-pkcs11
%{_unitdir}/named-pkcs11.service
%{_mandir}/man8/named-pkcs11.8*

%files pkcs11-utils
%defattr(-,root,root,-)
%{_sbindir}/dnssec*pkcs11
%{_sbindir}/pkcs11-destroy
%{_sbindir}/pkcs11-keygen
%{_sbindir}/pkcs11-list
%{_sbindir}/pkcs11-tokens
%{_mandir}/man8/pkcs11*.8*
%{_mandir}/man8/dnssec*-pkcs11.8*

%files pkcs11-libs
%defattr(-,root,root,-)
%{_libdir}/*pkcs11.so.*
%{_libdir}/*pkcs11-export.so.*

%files pkcs11-devel
%defattr(-,root,root,-)
%{_includedir}/bind9/pk11
%{_includedir}/bind9/pkcs11
%{_libdir}/*pkcs11.so
%{_libdir}/*pkcs11-export.so

%endif

%changelog
* Thu Sep 20 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-72
- Fix automatic selinux boolean named_write_master_zones (#1569466)
- Allow starting named with readonly home again

* Wed Aug 08 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-71
- Fix CVE-2018-5740

* Sun Jun 24 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-70
- Fix compiler warnings

* Thu Jun 21 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-69
- Refetch always records with TTL 0 (#1549130)

* Thu Jun 21 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-68
- Detect and disable MD5 functions in FIPS 140-2 mode (#1519306)

* Thu Jun 14 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-67
- Move change of dns_view_t to the end (#1452091)

* Fri Jun 01 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-66
- Correct recursing file name (#1435883)
- Use python binary again, install all modules (#1510008)

* Thu May 31 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-65
- Add rndc secroots and recursing output files into data (#1435883)

* Mon May 28 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-64
- Backported negative trust anchors (#1452091)

* Mon May 28 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-63
- Make named home writeable (#1569466)
- Change named shell to /bin/false

* Tue May 22 2018 Martin Sehnoutka <msehnout@redhat.com> - 32:9.9.4-62
- Resolves: #1510008 - add support for dnssec-keymgr

* Tue Jan 16 2018 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-61
- Fix CVE-2017-3145

* Tue Dec 05 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-60
- Fix regression caused by bug #1470637

* Mon Nov 13 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-59
- Support for additional signing algorithms in rndc (#1501531)
- New autogenerated rndc keys will use hmac-sha256 algorithm

* Tue Oct 31 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-58
- Fix multilib regression in headers

* Mon Oct 30 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-57
- Add with-tunning=large support (#rh1464850)

* Thu Oct 19 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-56
- Fix named-chroot restart leak (#1503646)

* Thu Oct 12 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-55
- Handle dig timeouts the same way as upstream (#1470637)

* Wed Oct 11 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-54
- Do not use next search domain on timeout from dig (#1470637)

* Tue Aug 01 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-53
- Fixed TSIG validation of AXFR and IXFR (#1476013)

* Fri Jul 07 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-52
- Add missing manual for dnssec-importkey (#1472862)

* Thu Jun 29 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-51
- Fix CVE-2017-3142 and CVE-2017-3143

* Mon May 22 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-50
- Update root servers and trust anchor (#1452635)

* Thu Apr 20 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-49
- Address deadlock between view.c and adb.c (#1416304)

* Tue Apr 11 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-48
- Fix CVE-2017-3136 (ISC change 4575)
- Fix CVE-2017-3137 (ISC change 4578)

* Wed Mar 29 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-47
- Simplify change of used config file, point to KB article (#1271315)

* Tue Mar 28 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-46
- Make comment how to use different config file (#1271315)

* Thu Mar 16 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-45
- Install again dns/dlz.h skipped in rebase
- Fixed coverity warnings on reenabled test dlzexternal

* Tue Mar 14 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-44
- Backported new upstream dyndb interface, removed dynamic_db (#1393886)

* Mon Feb 27 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-43
- Do not warn on WKS patch (#1392362)

* Tue Feb 21 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-42
- Support WKS records in chroot

* Wed Feb 08 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-41
- Fix CVE-2017-3135 (ISC change 4557)
- Fix and test caching CNAME before DNAME (ISC change 4558)

* Fri Jan 20 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-40
- Fix possible infinite loop in start_lookup (CVE-2016-2775)
- Do not change lib permissions in chroot (#1392531)

* Mon Jan 09 2017 Petr Menšík <pemensik@redhat.com> - 32:9.9.4-39
- Fix CVE-2016-9131 (ISC change 4508)
- Fix CVE-2016-9147 (ISC change 4510)
- Fix regression introduced by CVE-2016-8864 (ISC change 4530)
- Fix CVE-2016-9444 (ISC change 4517)

* Mon Oct 31 2016 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-38
- Fix CVE-2016-8864

* Fri Sep 23 2016 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-37
- Fix CVE-2016-2776

* Wed May 11 2016 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-36
- Added automatic interface scan functionality (#1294506)
- Removed NetworkManager dispatcher script since it is not needed any more (#1294506)

* Wed Apr 13 2016 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-35
- Added GeoIP support (#1220594)

* Fri Apr 01 2016 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-34
- Added support for CAA records (#1306610)
- Use HTTPS URL instead of FTP for upstream sources (#1319280)

* Tue Mar 22 2016 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-33
- Fix excessive queries caused by DS chasing with stub zones when DNSSEC is not used (#1291185)
- Fix error in internal test suite (#1259514)
- Fix named-checkconf call in *-chroot.service files (#1278082)
- Fix incorrect path in BIND sample configuration and added comment to default configuration (#1247502)

* Tue Mar 08 2016 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-32
- Fix CVE-2016-1285 and CVE-2016-1286

* Mon Jan 18 2016 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-31
- Fix CVE-2015-8704

* Mon Dec 14 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-30
- Fix CVE-2015-8000

* Wed Sep 02 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-29
- Fix CVE-2015-5722

* Wed Aug 05 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-28
- Increase ISC_SOCKET_MAXEVENTS to 2048 (#1235609)

* Tue Jul 28 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-27
- Fix CVE-2015-5477

* Wed Jul 08 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-26
- Fix CVE-2015-4620

* Tue Jul 07 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-25
- Fixed nsupdate realm auto-detection (#1214827)

* Mon Jun 29 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-24
- Reintroduce the DISABLE_ZONE_CHECKING into /etc/sysconfig/named (#1236475)

* Mon Jun 01 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-23
- Don't copy /etc/localtime on -chroot package installation (#1186773)
- Fix SPF resource records check to comply with RFC7208 (#1215164)
- Don't use ISC's DLV by default (#1223336)

* Fri May 22 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-22
- Add version specific requires on bind for bind-pkcs11 (Related: #1097753)
- Resolve issues found by static analysis (Related: #1097753)

* Thu May 21 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-21
- Added native PKCS#11 functionality (#1097753)

* Wed May 20 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-20
- DNS resolution failure in high load environment with SERVFAIL and "out of memory/success" in the log (#1221180)

* Thu May 14 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-19
- Install config for tmpfiles under %%{_tmpfilesdir} (#1180976)
- Fixed systemctl path in logrotate configuration (#1164264)
- remove information about system-config-bind from named.8 man page (#1152066)

* Mon Mar 02 2015 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-18.1
- Fix CVE-2015-1349

* Wed Dec 10 2014 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-18
- Fix CVE-2014-8500 (#1171976)

* Thu Sep 18 2014 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-17
- Fix error in dyndb API that can cause named to freeze on shutdown (#1142150)
- Fix error in triggerun scriptlet (#1143033)
- Remove /var/named/chroot/var/run on bind-chroot update if it is a directory (#1091341)

* Thu Aug 21 2014 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-16
- Add versioned requires on bind-libs to bind-utils and bind-sdb

* Wed Aug 20 2014 Tomas Hozza <thozza@redhat.com> - 32:9.9.4-15
- Use /dev/urandom when generating rndc.key file (#1107568)
- Allow authentication using TSIG in allow-notify configuration statement (#1067424)
- Fix race condition when destroying a resolver fetch object (#1072379)
- Increase defaults for lwresd workers and make workers and client objects number configurable (#1098959)
- Configure BIND with --with-dlopen=yes to support dynamically loadable DLZ drivers (#1096688)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 32:9.9.4-14
- Mass rebuild 2014-01-24

* Wed Jan 15 2014 Honza Horak <hhorak@redhat.com> - 32:9.9.4-13
- Rebuild for mariadb-libs
  Related: #1045013

* Tue Jan 14 2014 Tomas Hozza <thozza@redhat.com> 32:9.9.4-12
- Fix CVE-2014-0591

* Mon Jan 06 2014 Tomas Hozza <thozza@redhat.com> 32:9.9.4-11
- Build against libdb instead of libdb4 (#1044990)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 32:9.9.4-10
- Mass rebuild 2013-12-27

* Wed Dec 18 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-9
- Fix crash in rbtdb after two sucessive getoriginnode() calls (#1044026)

* Tue Dec 17 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-8
- Split chroot package for named and named-sdb
- Extract setting-up/destroying of chroot to a separate systemd service (#1004300)

* Thu Dec 05 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-7
- Create symlink /var/named/chroot/var/run -> /var/named/chroot/run (#1024384)
- Added session-keyfile statement into default named.conf since we use /run/named (#1024384)

* Thu Nov 28 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-6
- Fixed memory leak in nsupdate if 'realm' was used multiple times (#1034824)

* Tue Nov 12 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-5
- Install configuration for rwtab and fix chroot setup script (#1028189)
- use --enable-filter-aaaa when building bind to enable filter-aaaa-on-v4 option (#1025245)

* Thu Oct 31 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-4
- Correct the patch for #1020683

* Tue Oct 29 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-3
- Fix race condition on send buffers in dighost.c (#1020683)

* Tue Oct 08 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-2
- install isc/errno2result.h header (#1015165)

* Mon Sep 23 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.4-1
- update to 9.9.4 (#1010200)
- drop merged patches
- modify patches to fit on new version

* Tue Sep 10 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-8.P2
- Fix [ISC-Bugs #34738] dns_journal_open() returns a pointer to stack

* Fri Aug 16 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-7.P2
- Don't generate rndc.key if there exists rndc.conf

* Fri Aug 16 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-6.P2
- don't install named-sdb.service if SDB macro is defined to zero

* Sun Jul 28 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-5.P2
- update to 9.9.3-P2 (fix for CVE-2013-4854)
- update RRL patch to 9.9.3-P2-rl.13207.22
- Fix script for setting up chroot so it unmounts everything successfully

* Wed Jul 10 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-4.P1
- Fix dates in Changelog

* Wed Jun 05 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-3.P1
- update to 9.9.3-P1 (fix for CVE-2013-3919)
- update RRL patch to 9.9.3-P1-rl.156.01

* Mon Jun 03 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-2
- bump release to prevent update path issues

* Mon Jun 03 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-1
- update to 9.9.3
- install dns/update.h header
- update RRL patch to the latest version 9.9.3-rl.150.20

* Fri May 17 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-0.7.rc2
- Fix segfault in host/nslookup (#878139)

* Mon May 13 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-0.6.rc2
- update to 9.9.3rc2
- part of bind97-exportlib.patch not needed any more
- bind-9.9.1-P2-multlib-conflict.patch modified to reflect latest source
- rl-9.9.3rc1.patch -> rl-9.9.3rc2.patch
- bind99-opts.patch merged

* Fri May 03 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-0.5.rc1
- Include recursion Warning in named.conf and named.conf.sample (#740894)
- Include managed-keys-directory statement in named.conf.sample (#948026)

* Thu May 02 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.3-0.4.rc1
- Fix zone2sqlite to quote table names when creating/dropping/inserting (#919417)

* Fri Apr 19 2013 Adam Tkac <atkac redhat com> 32:9.9.3-0.3.rc1
- fix crash in nsupdate when processing "-r" parameter (#949544)

* Tue Apr 16 2013 Adam Tkac <atkac redhat com> 32:9.9.3-0.2.rc1
- ship dns/rrl.h in -devel subpkg

* Tue Apr 16 2013 Adam Tkac <atkac redhat com> 32:9.9.3-0.1.rc1
- update to 9.9.3rc1
- bind-96-libtool2.patch has been merged
- fix bind tmpfiles.d for named.pid /run migration (#920713)

* Wed Mar 27 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.2-12.P2
- New upstream patch version fixing CVE-2013-2266 (#928032)

* Tue Mar 19 2013 Adam Tkac <atkac redhat com> 32:9.9.2-11.P1
- move pidfile to /run/named/named.pid

* Wed Mar 06 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.2-10.P1
- Fix Makefile.in to include header added by rate limiting patch (#918330)

* Tue Mar 05 2013 Adam Tkac <atkac redhat com> 32:9.9.2-9.P1
- drop some developer-only documentation and move ARM to %%docdir

* Mon Feb 18 2013 Adam Tkac <atkac redhat com> 32:9.9.2-8.P1
- include rate limiting patch

* Tue Jan 29 2013 Tomas Hozza <thozza@redhat.com> 32:9.9.2-7.P1
- Corrected IP addresses in named.ca (#901741)
- mount/umount /var/named in setup-named-chroot.sh as the last one (#904666)

* Thu Dec 20 2012 Adam Tkac <atkac redhat com> 32:9.9.2-6.P1
- generate /etc/rndc.key during named service startup if doesn't exist
- increase startup timeout in systemd units to 90sec (default)
- fix IDN related statement in dig.1 manpage

* Wed Dec 05 2012 Tomas Hozza <thozza@redhat.com> 32:9.9.2-5.P1
- update to bind-9.9.2-P1

* Mon Nov 12 2012 Adam Tkac <atkac redhat com> 32:9.9.2-4
- document dig exit codes in manpage
- ignore empty "search" options in resolv.conf

* Mon Nov 12 2012 Adam Tkac <atkac redhat com> 32:9.9.2-3
- drop PKCS11 support on rhel

* Thu Oct 11 2012 Adam Tkac <atkac redhat com> 32:9.9.2-2
- install isc/stat.h

* Thu Oct 11 2012 Adam Tkac <atkac redhat com> 32:9.9.2-1
- update to 9.9.2
- bind97-rh714049.patch has been dropped
- patches merged
  - bind98-rh816164.patch

* Thu Sep 13 2012 Adam Tkac <atkac redhat com> 32:9.9.1-10.P3
- update to bind-9.9.1-P3

* Wed Aug 22 2012 Tomas Hozza <thozza@redhat.com> 32:9.9.1-9.P2
- fixed SPEC file so it comply with new systemd-rpm macros guidelines (#850045)
- changed %%define macros to %%global and fixed several rpmlint warnings

* Wed Aug 08 2012 Tomas Hozza <thozza@redhat.com> 32:9.9.1-8.P2
- Changed PrivateTmp to "false" in *-chroot.service unit files (#825869)

* Wed Aug 01 2012 Tomas Hozza <thozza@redhat.com> 32:9.9.1-7.P2
- Fixed bind-devel multilib conflict (#478718)

* Mon Jul 30 2012 Tomas Hozza <thozza@redhat.com> 32:9.9.1-6.P2
- Fixed bad path to systemctl in /etc/NetworkManager/dispatcher.d/13-named (#844047)
- Fixed path to libdb.so in config.dlz.in

* Thu Jul 26 2012 Adam Tkac <atkac redhat com> 32:9.9.1-5.P2
- update to 9.9.1-P2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32:9.9.1-4.P1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 32:9.9.1-3.P1
- Avoid shell invocation and dep for -libs-lite %%postun.

* Mon Jun 04 2012 Adam Tkac <atkac redhat com> 32:9.9.1-2.P1
- update to 9.9.1-P1 (CVE-2012-1667)

* Thu May 24 2012 Adam Tkac <atkac redhat com> 32:9.9.1-1
- update to 9.9.1
- bind99-coverity.patch merged
- bind-9.5-overflow.patch merged

* Mon May 07 2012 Adam Tkac <atkac redhat com> 32:9.9.0-6
- nslookup: return non-zero exit code when fail to get answer (#816164)

* Thu Apr 26 2012 Adam Tkac <atkac redhat com> 32:9.9.0-5
- initscript: don't umount /var/named when didn't mount it

* Tue Apr 24 2012 Adam Tkac <atkac redhat com> 32:9.9.0-4
- apply all non-SDB patches before SDB ones (#804475)
- enable Berkeley DB DLZ backend (#804478)

* Thu Apr 12 2012 Adam Tkac <atkac redhat com> 32:9.9.0-3
- bind97-rh699951.patch is no longer needed (different fix is in 9.9.0)

* Mon Mar 26 2012 Adam Tkac <atkac redhat com> 32:9.9.0-2
- remove unneeded bind99-v6only.patch

* Mon Mar 05 2012 Adam Tkac <atkac redhat com> 32:9.9.0-1
- update to 9.9.0
- load dynamic DBs later (and update dyndb patch)
- fix memory leak in named during processing of rndc command
- don't call `rndc-confgen -a` in "post" section
- fix some packaging bugs in bind-chroot

* Wed Feb 15 2012 Adam Tkac <atkac redhat com> 32:9.9.0-0.8.rc2
- build with "--enable-fixed-rrset"

* Wed Feb 01 2012 Adam Tkac <atkac redhat com> 32:9.9.0-0.7.rc2
- update to 9.9.0rc2
- doc/rfc and doc/draft are no longer shipped in tarball

* Mon Jan 30 2012 Adam Tkac <atkac redhat com> 32:9.9.0-0.6.rc1
- retire initscript in favour of systemd unit files (#719419)

* Thu Jan 12 2012 Adam Tkac <atkac redhat com> 32:9.9.0-0.5.rc1
- update to 9.9.0rc1

* Wed Dec 07 2011 Adam Tkac <atkac redhat com> 32:9.9.0-0.4.b2
- ship dns/forward.h in -devel subpkg

* Tue Nov 22 2011 Adam Tkac <atkac redhat com> 32:9.9.0-0.3.b2
- update to 9.9.0b2 (CVE-2011-4313)
- patches merged
  - bind97-rh700097.patch
  - bind99-cinfo.patch

* Mon Nov 14 2011 Adam Tkac <atkac redhat com> 32:9.9.0-0.2.b1
- ship dns/clientinfo.h in bind-devel

* Fri Nov 11 2011 Adam Tkac <atkac redhat com> 32:9.9.0-0.1.b1
- update to 9.9.0b1
- bind98-dlz_buildfix.patch merged

* Fri Oct 28 2011 Adam Tkac <atkac redhat com> 32:9.8.1-4
- nslookup failed to resolve name in certain cases

* Mon Sep 26 2011 Adam Tkac <atkac redhat com> 32:9.8.1-3
- remove deps filter, it is no longer needed (#739663)

* Fri Sep 09 2011 Adam Tkac <atkac redhat com> 32:9.8.1-2
- fix logrotate config file (#725256)

* Wed Sep 07 2011 Adam Tkac <atkac redhat com> 32:9.8.1-1
- update to 9.8.1
- ship /etc/trusted-key.key (needed by dig)
- use select instead of epoll in export libs (#735103)

* Wed Aug 31 2011 Adam Tkac <atkac redhat com> 32:9.8.1-0.3.rc1
- fix DLZ related compilation issues
- make /etc/named.{root,iscdlv}.key world-readable
- add bind-libs versioned requires to bind pkg

* Wed Aug 31 2011 Adam Tkac <atkac redhat com> 32:9.8.1-0.2.rc1
- fix rare race condition in request.c
- print "the working directory is not writable" as debug message
- re-add configtest target to initscript
- initscript: sybsys name is always named, not named-sdb
- nsupdate returned zero when target zone didn't exist (#700097)
- nsupdate could have failed if server has multiple IPs and the first
  was unreachable (#714049)

* Wed Aug 31 2011 Adam Tkac <atkac redhat com> 32:9.8.1-0.1.rc1
- update to 9.8.1rc1
- patches merged
  - bind97-rh674334.patch
  - bind97-cleanup.patch
  - bind98-includes.patch

* Wed Aug 03 2011 Adam Tkac <atkac redhat com> 32:9.8.0-9.P4
- improve patch for #725741

* Tue Jul 26 2011 Adam Tkac <atkac redhat com> 32:9.8.0-8.P4
- named could have crashed during reload when dyndb module is used (#725741)

* Tue Jul 05 2011 Adam Tkac <atkac redhat com> 32:9.8.0-7.P4
- update to 9.8.0-P4
  - bind98-libdns-export.patch merged

* Thu Jun 02 2011 Adam Tkac <atkac redhat com> 32:9.8.0-6.P2
- update the dyndb patch

* Fri May 27 2011 Adam Tkac <atkac redhat com> 32:9.8.0-5.P2
- fix compilation of libdns-export.so

* Fri May 27 2011 Adam Tkac <atkac redhat com> 32:9.8.0-4.P2
- update to 9.8.0-P2 (CVE-2011-1910)

* Fri May 06 2011 Adam Tkac <atkac redhat com> 32:9.8.0-3.P1
- update to 9.8.0-P1 (CVE-2011-1907)

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 32:9.8.0-2
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Thu Mar 03 2011 Adam Tkac <atkac redhat com> 32:9.8.0-1
- update to 9.8.0
- bind97-rh665971.patch merged

* Thu Mar 03 2011 Adam Tkac <atkac redhat com> 32:9.8.0-0.4.rc1
- revert previous change (integration with libnmserver)

* Tue Feb 22 2011 Adam Tkac <atkac redhat com> 32:9.8.0-0.3.rc1
- integrate named with libnmserver library

* Tue Feb 22 2011 Adam Tkac <atkac redhat com> 32:9.8.0-0.2.rc1
- include dns/rpz.h in -devel subpkg

* Mon Feb 21 2011 Adam Tkac <atkac redhat com> 32:9.8.0-0.1.rc1
- update to 9.8.0rc1

* Fri Feb 18 2011 Adam Tkac <atkac redhat com> 32:9.7.3-1
- update to 9.7.3
- fix dig +trace on dualstack systems (#674334)
- fix linkage order when building on system with older BIND (#665971)
- reduce number of gcc warnings

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32:9.7.3-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Adam Tkac <atkac redhat com> 32:9.7.3-0.5.rc1
- update to 9.7.3rc1
  - bind97-krb5-self.patch merged

* Wed Jan 12 2011 Adam Tkac <atkac redhat com> 32:9.7.3-0.4.b1
- fix typo in initscript

* Thu Jan 06 2011 Adam Tkac <atkac redhat com> 32:9.7.3-0.3.b1
- fix "service named status" when used with named-sdb
- don't check MD5, size and mtime of sysconfig/named

* Wed Jan 05 2011 Adam Tkac <atkac redhat com> 32:9.7.3-0.2.b1
- add new option DISABLE_ZONE_CHECKING to sysconfig/named

* Wed Jan 05 2011 Adam Tkac <atkac redhat com> 32:9.7.3-0.1.b1
- update to 9.7.3b1

* Wed Jan 05 2011 Adam Tkac <atkac redhat com> 32:9.7.2-10.P3
- initscript should terminate only the correct "named" process (#622785)

* Mon Dec 20 2010 Adam Tkac <atkac redhat com> 32:9.7.2-9.P3
- fix "krb5-self" update-policy rule processing

* Thu Dec 02 2010 Adam Tkac <atkac redhat com> 32:9.7.2-8.P3
- update to 9.7.2-P3

* Mon Nov 29 2010 Jan Görig <jgorig redhat com> 32:9.7.2-7.P2
- added tmpfiles.d support (#656550)
- removed old PID checking in initscript

* Mon Nov 08 2010 Adam Tkac <atkac redhat com> 32:9.7.2-6.P2
- don't emit various informational messages by default (#645544)

* Wed Oct 20 2010 Adam Tkac <atkac redhat com> 32:9.7.2-5.P2
- move BIND9 internal libs back to %%{_libdir}
- add "-export" suffix to public libraries (-lite subpkg)

* Thu Oct 07 2010 Adam Tkac <atkac redhat com> 32:9.7.2-4.P2
- ship -devel subpkg for internal libs, dnsperf needs it

* Thu Oct 07 2010 Adam Tkac <atkac redhat com> 32:9.7.2-3.P2
- new bind-libs-lite and bind-lite-devel subpkgs which contain
  public version of BIND 9 libraries
- don't ship devel files for internal version of BIND 9 libraries

* Wed Sep 29 2010 Adam Tkac <atkac redhat com> 32:9.7.2-2.P2
- update to 9.7.2-P2

* Thu Sep 16 2010 Adam Tkac <atkac redhat com> 32:9.7.2-1
- update to 9.7.2

* Fri Aug 27 2010 Adam Tkac <atkac redhat com> 32:9.7.2-0.3.rc1
- update to 9.7.2rc1

* Tue Aug 10 2010 Adam Tkac <atkac redhat com> 32:9.7.2-0.2.b1
- host: handle "debug", "attempts" and "timeout" options in resolv.conf well

* Tue Aug 03 2010 Adam Tkac <atkac redhat com> 32:9.7.2-0.1.b1
- update to 9.7.2b1
- patches merged
  - bind97-rh507429.patch

* Mon Jul 19 2010 Adam Tkac <atkac redhat com> 32:9.7.1-5.P2
- supply root zone DNSKEY in default configuration

* Mon Jul 19 2010 Adam Tkac <atkac redhat com> 32:9.7.1-4.P2
- update to 9.7.1-P2 (CVE-2010-0213)

* Mon Jul 12 2010 Adam Tkac <atkac redhat com> 32:9.7.1-3.P1
- remove outdated Copyright.caching-nameserver file
- remove rfc1912.txt, it is already located in %%doc/rfc directory
- move COPYRIGHT to the bind-libs subpkg
- add COPYRIGHT to the -pkcs11 subpkg

* Fri Jul 09 2010 Adam Tkac <atkac redhat com> 32:9.7.1-2.P1
- update to 9.7.1-P1

* Mon Jun 28 2010 Adam Tkac <atkac redhat com> 32:9.7.1-1
- update to 9.7.1
- improve the "dnssec-conf" trigger

* Wed Jun 09 2010 Adam Tkac <atkac redhat com> 32:9.7.1-0.2.rc1
- update to 9.7.1rc1
- patches merged
  - bind97-keysdir.patch

* Mon May 31 2010 Adam Tkac <atkac redhat com> 32:9.7.1-0.1.b1
- update to 9.7.1b1
- make /var/named/dynamic as a default directory for managed DNSSEC keys
- add patch to get "managed-keys-directory" option working
- patches merged
  - bind97-managed-keyfile.patch
  - bind97-rh554316.patch

* Fri May 21 2010 Adam Tkac <atkac redhat com> 32:9.7.0-11.P2
- update dnssec-conf Obsoletes/Provides

* Thu May 20 2010 Adam Tkac <atkac redhat com> 32:9.7.0-10.P2
- update to 9.7.0-P2

* Fri Mar 26 2010 Adam Tkac <atkac redhat com> 32:9.7.0-9.P1
- added lost patch for #554316 (occasional crash in keytable.c)

* Fri Mar 26 2010 Adam Tkac <atkac redhat com> 32:9.7.0-8.P1
- active query might be destroyed in resume_dslookup() which triggered REQUIRE
  failure (#507429)

* Mon Mar 22 2010 Adam Tkac <atkac redhat com> 32:9.7.0-7.P1
- install SDB related manpages only when build with SDB

* Fri Mar 19 2010 Adam Tkac <atkac redhat com> 32:9.7.0-6.P1
- update to 9.7.0-P1

* Tue Mar 16 2010 Jan Görig <jgorig redhat com> 32:9.7.0-5
- bind-sdb now requires bind

* Mon Mar 15 2010 Jan Görig <jgorig redhat com> 32:9.7.0-4
- add man-pages ldap2zone.1 zonetodb.1 zone2sqlite.1 named-sdb.8 (#525655)

* Mon Mar 01 2010 Adam Tkac <atkac redhat com> 32:9.7.0-3
- fix multilib issue (#478718) [jgorig]

* Mon Mar 01 2010 Adam Tkac <atkac redhat com> 32:9.7.0-2
- improve automatic DNSSEC reconfiguration trigger
- initscript now returns 2 in case that action doesn't exist (#523435)
- enable/disable chroot when bind-chroot is installed/uninstalled

* Wed Feb 17 2010 Adam Tkac <atkac redhat com> 32:9.7.0-1
- update to 9.7.0 final

* Mon Feb 15 2010 Adam Tkac <atkac redhat com> 32:9.7.0-0.14.rc2
- obsolete dnssec-conf
- automatically update configuration from old dnssec-conf based
- improve default configuration; enable DLV by default
- remove obsolete triggerpostun from bind-libs subpackage

* Thu Jan 28 2010 Adam Tkac <atkac redhat com> 32:9.7.0-0.13.rc2
- update to 9.7.0rc2

* Wed Jan 27 2010 Adam Tkac <atkac redhat com> 32:9.7.0-0.12.rc1
- initscript LSB related fixes (#523435)

* Wed Jan 27 2010 Adam Tkac <atkac redhat com> 32:9.7.0-0.11.rc1
- revert the "DEBUG" feature (#510283), it causes too many problems (#545128)

* Tue Dec 15 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.10.rc1
- update to 9.7.0rc1
- bind97-headers.patch merged
- update default configuration

* Tue Dec 01 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.9.b3
- update to 9.7.0b3

* Thu Nov 26 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.8.b2
- install isc/namespace.h header

* Fri Nov 06 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.7.b2
- update to 9.7.0b2

* Tue Nov 03 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.6.b1
- update to 9.7.0b1
- add bind-pkcs11 subpackage to support PKCS11 compatible keystores for DNSSEC
  keys

* Thu Oct 08 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.5.a3
- don't package named-bootconf utility, it is very outdated and unneeded

* Mon Sep 21 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.4.a3
- determine file size via `stat` instead of `ls` (#523682)

* Wed Sep 16 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.3.a3
- update to 9.7.0a3

* Tue Sep 15 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.2.a2
- improve chroot related documentation (#507795)
- add NetworkManager dispatcher script to reload named when network interface is
  activated/deactivated (#490275)
- don't set/unset named_write_master_zones SELinux boolean every time in
  initscript, modify it only when it's actually needed

* Tue Sep 15 2009 Adam Tkac <atkac redhat com> 32:9.7.0-0.1.a2
- update to 9.7.0a2
- merged patches
  - bind-96-db_unregister.patch
  - bind96-rh507469.patch

* Tue Sep 01 2009 Adam Tkac <atkac redhat com> 32:9.6.1-9.P1
- next attempt to fix the postun trigger (#520385)
- remove obsolete bind-9.3.1rc1-fix_libbind_includedir.patch

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 32:9.6.1-8.P1
- rebuilt with new openssl

* Tue Aug 04 2009 Martin Nagy <mnagy redhat com> 32:9.6.1-7.P1
- update the patch for dynamic loading of database backends

* Wed Jul 29 2009 Adam Tkac <atkac redhat com> 32:9.6.1-6.P1
- 9.6.1-P1 release (CVE-2009-0696)
- fix postun trigger (#513016, hopefully)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32:9.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Adam Tkac <atkac redhat com> 32:9.6.1-4
- remove useless bind-9.3.3rc2-rndckey.patch

* Mon Jul 13 2009 Adam Tkac <atkac redhat com> 32:9.6.1-3
- fix broken symlinks in bind-libs (#509635)
- fix typos in /etc/sysconfig/named (#509650)
- add DEBUG option to /etc/sysconfig/named (#510283)

* Wed Jun 24 2009 Adam Tkac <atkac redhat com> 32:9.6.1-2
- improved "chroot automount" patches (#504596)
- host should fail if specified server doesn't respond (#507469)

* Wed Jun 17 2009 Adam Tkac <atkac redhat com> 32:9.6.1-1
- 9.6.1 release
- simplify chroot maintenance. Important files and directories are mounted into
  chroot (see /etc/sysconfig/named for more info, #504596)
- fix doc/named.conf.default perms

* Wed May 27 2009 Adam Tkac <atkac redhat com> 32:9.6.1-0.4.rc1
- 9.6.1rc1 release

* Wed Apr 29 2009 Martin Nagy <mnagy redhat com> 32:9.6.1-0.3.b1
- update the patch for dynamic loading of database backends
- create %%{_libdir}/bind directory
- copy default named.conf to doc directory, shared with s-c-bind (atkac)

* Fri Apr 24 2009 Martin Nagy <mnagy redhat com> 32:9.6.1-0.2.b1
- update the patch for dynamic loading of database backends
- fix dns_db_unregister()
- useradd now takes "-N" instead of "-n" (atkac, #495726)
- print nicer error msg when zone file is actually a directory (atkac, #490837)

* Mon Mar 30 2009 Adam Tkac <atkac redhat com> 32:9.6.1-0.1.b1
- 9.6.1b1 release
- patches merged
  - bind-96-isc_header.patch
  - bind-95-rh469440.patch
  - bind-96-realloc.patch
  - bind9-fedora-0001.diff
- use -version-number instead of -version-info libtool param

* Mon Mar 23 2009 Adam Tkac <atkac redhat com> 32:9.6.0-11.1.P1
- logrotate configuration file now points to /var/named/data/named.run by
  default (#489986)

* Tue Mar 17 2009 Adam Tkac <atkac redhat com> 32:9.6.0-11.P1
- fall back to insecure mode when no supported DNSSEC algorithm is found
  instead of SERVFAIL
- don't fall back to non-EDNS0 queries when DO bit is set

* Tue Mar 10 2009 Adam Tkac <atkac redhat com> 32:9.6.0-10.P1
- enable DNSSEC only if it is enabled in sysconfig/dnssec

* Mon Mar 09 2009 Adam Tkac <atkac redhat com> 32:9.6.0-9.P1
- add DNSSEC support to initscript, enabled it per default
- add requires dnssec-conf

* Mon Mar 09 2009 Adam Tkac <atkac redhat com> 32:9.6.0-8.P1
- fire away libbind, it is now separate package

* Wed Mar 04 2009 Adam Tkac <atkac redhat com> 32:9.6.0-7.P1
- fixed some read buffer overflows (upstream)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 32:9.6.0-6.P1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Martin Nagy <mnagy redhat com> 32:9.6.0-5.P1
- update the patch for dynamic loading of database backends
- include iterated_hash.h

* Sat Jan 24 2009 Caolán McNamara <caolanm@redhat.com> 32:9.6.0-4.P1
- rebuild for dependencies

* Wed Jan 21 2009 Adam Tkac <atkac redhat com> 32:9.6.0-3.P1
- rebuild against new openssl

* Thu Jan 08 2009 Adam Tkac <atkac redhat com> 32:9.6.0-2.P1
- 9.6.0-P1 release (CVE-2009-0025)

* Mon Jan 05 2009 Adam Tkac <atkac redhat com> 32:9.6.0-1
- Happy new year
- 9.6.0 release

* Thu Dec 18 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.7.rc2
- 9.6.0rc2 release
- bind-96-rh475120.patch merged

* Tue Dec 16 2008 Martin Nagy <mnagy redhat com> 32:9.6.0-0.6.rc1
- add patch for dynamic loading of database backends

* Tue Dec 09 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.5.1.rc1
- allow to reuse address for non-random query-source ports (#475120)

* Wed Dec 03 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.5.rc1
- 9.6.0rc1 release
- patches merged
  - bind-9.2.0rc3-varrun.patch
  - bind-95-sdlz-include.patch
  - bind-96-libxml2.patch
- fixed rare use-after-free problem in host utility (#452060)
- enabled chase of DNSSEC signature chains in dig

* Mon Dec 01 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.4.1.b1
- improved sample config file (#473586)

* Wed Nov 26 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.4.b1
- reverted previous change, koji doesn't like it

* Wed Nov 26 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.3.b1
- build bind-chroot as noarch

* Mon Nov 24 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.2.1.b1
- updates due libtool 2.2.6
- don't pass -DLDAP_DEPRECATED to cpp, handle it directly in sources

* Tue Nov 11 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.2.b1
- make statistics http server working, patch backported from 9.6 HEAD

* Mon Nov 10 2008 Adam Tkac <atkac redhat com> 32:9.6.0-0.1.b1
- 9.6.0b1 release
- don't build ODBC and Berkeley DB DLZ drivers
- end of bind-chroot-admin script, copy config files to chroot manually
- /proc doesn't have to be mounted to chroot
- temporary use libbind from 9.5 series, noone has been released for 9.6 yet

* Mon Nov 03 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.8.4.b2
- dig/host: use only IPv4 addresses when -4 option is specified (#469440)

* Thu Oct 30 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.8.2.b2
- removed unneeded bind-9.4.1-ldap-api.patch

* Thu Oct 30 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.8.1.b2
- ship dns/{s,}dlz.h and isc/radix.h in bind-devel

* Tue Oct 07 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.8.b2
- removed bind-9.4.0-dnssec-directory.patch, it is wrong

* Wed Sep 24 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.7.b2
- 9.5.1b2 release
- patches merged
  - bind95-rh454783.patch
  - bind-9.5-edns.patch
  - bind95-rh450995.patch
  - bind95-rh457175.patch

* Wed Sep 17 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.6.b1
- IDN output strings didn't honour locale settings (#461409)

* Tue Aug 05 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.5.b1
- disable transfer stats on DLZ zones (#454783)

* Mon Aug 04 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.4.b1
- add forgotten patch for #457175
- build with -O2

* Thu Jul 31 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.3.b1
- static libraries are no longer supported
- IP acls weren't merged correctly (#457175)
- use fPIE on sparcv9/sparc64 (Dennis Gilmore)
- add sparc64 to list of 64bit arches in spec (Dennis Gilmore)

* Mon Jul 21 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.2.b1
- updated patches due new rpm (--fuzz=0 patch parameter)

* Mon Jul 14 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.1.1.b1
- use %%patch0 for Patch0 (#455061)
- correct source address (#455118)

* Tue Jul 08 2008 Adam Tkac <atkac redhat com> 32:9.5.1-0.1.b1
- 9.5.1b1 release (CVE-2008-1447)
- dropped bind-9.5-recv-race.patch because upstream doesn't want it

* Mon Jun 30 2008 Adam Tkac <atkac redhat com> 32:9.5.0-37.1
- update default named.conf statements (#452708)

* Thu Jun 26 2008 Adam Tkac <atkac redhat com> 32:9.5.0-37
- some compat changes to fix building on RHEL4

* Mon Jun 23 2008 Adam Tkac <atkac redhat com> 32:9.5.0-36.3
- fixed typo in %%posttrans script

* Wed Jun 18 2008 Adam Tkac <atkac redhat com> 32:9.5.0-36.2
- parse inner acls correctly (#450995)

* Mon Jun 02 2008 Adam Tkac <atkac redhat com> 32:9.5.0-36.1
- removed dns-keygen utility in favour of rndc-confgen -a (#449287)
- some minor sample fixes (#449274)

* Thu May 29 2008 Adam Tkac <atkac redhat com> 32:9.5.0-36
- updated to 9.5.0 final
- use getifaddrs to find available interfaces

* Mon May 26 2008 Adam Tkac <atkac redhat com> 32:9.5.0-35.rc1
- make /var/run/named writable by named (#448277)
- fixed one non-utf8 file

* Thu May 22 2008 Adam Tkac <atkac redhat com> 32:9.5.0-34.rc1
- fixes needed to pass package review (#225614)

* Wed May 21 2008 Adam Tkac <atkac redhat com> 32:9.5.0-33.1.rc1
- bind-chroot now depends on bind (#446477)

* Wed May 14 2008 Adam Tkac <atkac redhat com> 32:9.5.0-33.rc1
- updated to 9.5.0rc1
- merged patches
  - bind-9.5-libcap.patch
- make binaries readable by others (#427826)

* Tue May 13 2008 Adam Tkac <atkac redhat com> 32:9.5.0-32.b3
- reverted "any" patch, upstream says not needed
- log EDNS failure only when we really switch to plain EDNS (#275091)
- detect configuration file better

* Tue May 06 2008 Adam Tkac <atkac redhat com> 32:9.5.0-31.1.b3
- addresses 0.0.0.0 and ::0 really match any (#275091, comment #28)

* Mon May 05 2008 Adam Tkac <atkac redhat com> 32:9.5.0-31.b3
- readded bind-9.5-libcap.patch
- added bind-9.5-recv-race.patch from F8 branch (#400461)

* Wed Apr 23 2008 Adam Tkac <atkac redhat com> 32:9.5.0-30.1.b3
- build Berkeley DB DLZ backend

* Mon Apr 21 2008 Adam Tkac <atkac redhat com> 32:9.5.0-30.b3
- 9.5.0b3 release
- dropped patches (upstream)
  - bind-9.5-transfer-segv.patch
  - bind-9.5-mudflap.patch
  - bind-9.5.0-generate-xml.patch
  - bind-9.5-libcap.patch

* Wed Apr 02 2008 Adam Tkac <atkac redhat com> 32:9.5.0-29.3.b2
- fixed named.conf.sample file (#437569)

* Fri Mar 14 2008 Adam Tkac <atkac redhat com> 32:9.5.0-29.2.b2
- fixed URLs

* Mon Feb 25 2008 Adam Tkac <atkac redhat com> 32:9.5.0-29.1.b2
- BuildRequires cleanup

* Sun Feb 24 2008 Adam Tkac <atkac redhat com> 32:9.5.0-29.b2
- rebuild without mudflap (#434159)

* Wed Feb 20 2008 Adam Tkac <atkac redhat com> 32:9.5.0-28.b2
- port named to use libcap library, enable threads (#433102)
- removed some unneeded Requires

* Tue Feb 19 2008 Adam Tkac <atkac redhat com> 32:9.5.0-27.b2
- removed conditional build with libefence (use -fmudflapth instead)
- fixed building of DLZ stuff (#432497)
- do not build Berkeley DB DLZ backend
- temporary build with --disable-linux-caps and without threads (#433102)
- update named.ca file to affect IPv6 changes in root zone

* Mon Feb 11 2008 Adam Tkac <atkac redhat com> 32:9.5.0-26.b2
- build with -D_GNU_SOURCE (#431734)
- improved fix for #253537, posttrans script is now used
- improved fix for #400461
- 9.5.0b2
  - bind-9.3.2b1-PIE.patch replaced by bind-9.5-PIE.patch
    - only named, named-sdb and lwresd are PIE
  - bind-9.5-sdb.patch has been updated
  - bind-9.5-libidn.patch has been updated
  - bind-9.4.0-sdb-sqlite-bld.patch replaced by bind-9.5-sdb-sqlite-bld.patch
  - removed bind-9.5-gssapi-header.patch (upstream)
  - removed bind-9.5-CVE-2008-0122.patch (upstream)
- removed bind-9.2.2-nsl.patch
- improved sdb_tools Makefile.in

* Mon Feb 04 2008 Adam Tkac <atkac redhat com> 32:9.5.0-25.b1
- fixed segfault during sending notifies (#400461)
- rebuild with gcc 4.3 series

* Tue Jan 22 2008 Adam Tkac <atkac redhat com> 32:9.5.0-24.b1
- removed bind-9.3.2-prctl_set_dumpable.patch (upstream)
- allow parallel building of libdns library
- CVE-2008-0122

* Thu Dec 27 2007 Adam Tkac <atkac redhat com> 32:9.5.0-23.b1
- fixed initscript wait loop (#426382)
- removed dependency on policycoreutils and libselinux (#426515)

* Thu Dec 20 2007 Adam Tkac <atkac redhat com> 32:9.5.0-22.b1
- fixed regression caused by libidn2 patch (#426348)

* Wed Dec 19 2007 Adam Tkac <atkac redhat com> 32:9.5.0-21.b1
- fixed typo in post section (CVE-2007-6283)

* Wed Dec 19 2007 Adam Tkac <atkac redhat com> 32:9.5.0-20.b1
- removed obsoleted triggers
- CVE-2007-6283

* Wed Dec 12 2007 Adam Tkac <atkac redhat com> 32:9.5.0-19.2.b1
- added dst/gssapi.h to -devel subpackage (#419091)
- improved fix for (#417431)

* Mon Dec 10 2007 Adam Tkac <atkac redhat com> 32:9.5.0-19.1.b1
- fixed shutdown with initscript when rndc doesn't work (#417431)
- fixed IDN patch (#412241)

* Thu Dec 06 2007 Adam Tkac <atkac redhat com> 32:9.5.0-19.b1
- 9.5.0b1 (#405281, #392491)

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> 32:9.5.0-18.6.a7
- Rebuild for deps

* Wed Dec 05 2007 Adam Tkac <atkac redhat com> 32:9.5.0-18.5.a7
- build with -O0

* Mon Dec 03 2007 Adam Tkac <atkac redhat com> 32:9.5.0-18.4.a7
- bind-9.5-random_ports.patch was removed because upstream doesn't
  like it. query-source{,v6} options are sufficient (#391931)
- bind-chroot-admin called restorecon on /proc filesystem (#405281)

* Mon Nov 26 2007 Adam Tkac <atkac redhat com> 32:9.5.0-18.3.a7
- removed edns patch to keep compatibility with vanilla bind
  (#275091, comment #20)

* Wed Nov 21 2007 Adam Tkac <atkac redhat com> 32:9.5.0-18.2.a7
- use system port selector instead ISC's (#391931)

* Mon Nov 19 2007 Adam Tkac <atkac redhat com> 32:9.5.0-18.a7
- removed statement from initscript which passes -D to named

* Thu Nov 15 2007 Adam Tkac <atkac redhat com> 32:9.5.0-17.a7
- 9.5.0a7
- dropped patches (upstream)
  - bind-9.5-update.patch
  - bind-9.5-pool_badfree.patch
  - bind-9.5-_res_errno.patch

* Thu Nov 15 2007 Adam Tkac <atkac redhat com> 32:9.5.0-16.5.a6
- added bind-sdb again, contains SDB modules and DLZ modules
- bind-9.3.1rc1-sdb.patch replaced by bind-9.5-sdb.patch

* Mon Nov 12 2007 Adam Tkac <atkac redhat com> 32:9.5.0-16.4.a6
- removed Requires: openldap, postgresql, mysql, db4, unixODBC
- new L.ROOT-SERVERS.NET address

* Mon Oct 29 2007 Adam Tkac <atkac redhat com> 32:9.5.0-16.3.a6
- completely disable DBUS

* Fri Oct 26 2007 Adam Tkac <atkac redhat com> 32:9.5.0-16.2.a6
- minor cleanup in bind-chroot-admin

* Thu Oct 25 2007 Adam Tkac <atkac redhat com> 32:9.5.0-16.1.a6
- fixed typo in initscript

* Tue Oct 23 2007 Adam Tkac <atkac redhat com> 32:9.5.0-16.a6
- disabled DBUS (dhcdbd doesn't exist & #339191)

* Thu Oct 18 2007 Adam Tkac <atkac redhat com> 32:9.5.0-15.1.a6
- fixed missing va_end () functions (#336601)
- fixed memory leak when dbus initialization fails

* Tue Oct 16 2007 Adam Tkac <atkac redhat com> 32:9.5.0-15.a6
- corrected named.5 SDB statement (#326051)

* Mon Sep 24 2007 Adam Tkac <atkac redhat com> 32:9.5.0-14.a6
- added edns patch again (#275091)

* Mon Sep 24 2007 Adam Tkac <atkac redhat com> 32:9.5.0-13.a6
- removed bind-9.3.3-edns.patch patch (see #275091 for reasons)

* Thu Sep 20 2007 Adam Tkac <atkac redhat com> 32:9.5.0-12.4.a6
- build with O2
- removed "autotools" patch
- bugfixing in bind-chroot-admin (#279901)

* Thu Sep 06 2007 Adam Tkac <atkac redhat com> 32:9.5.0-12.a6
- bind-9.5-2119_revert.patch and bind-9.5-fix_h_errno.patch are
  obsoleted by upstream bind-9.5-_res_errno.patch

* Wed Sep 05 2007 Adam Tkac <atkac redhat com> 32:9.5.0-11.9.a6
- fixed wrong resolver's dispatch pool cleanup (#275011, patch from 
  tmraz redhat com)

* Wed Sep 05 2007 Adam Tkac <atkac redhat com> 32:9.5.0-11.3.a6
- initscript failure message is now printed correctly (#277981,
  Quentin Armitage (quentin armitage org uk) )

* Mon Sep 03 2007 Adam Tkac <atkac redhat com> 32:9.5.0-11.2.a6
- temporary revert ISC 2119 change and add "libbind-errno" patch
  (#254501) again

* Thu Aug 23 2007 Adam Tkac <atkac redhat com> 32:9.5.0-11.1.a6
- removed end dots from Summary sections (skasal@redhat.com)
- fixed wrong file creation by autotools patch (skasal@redhat.com)

* Thu Aug 23 2007 Adam Tkac <atkac redhat com> 32:9.5.0-11.a6
- start using --disable-isc-spnego configure option
  - remove bind-9.5-spnego-memory_management.patch (source isn't
    compiled)

* Wed Aug 22 2007 Adam Tkac <atkac redhat com> 32:9.5.0-10.2.a6
- added new initscript option KEYTAB_FILE which specified where
  is located kerberos .keytab file for named service
- obsolete temporary bind-9.5-spnego-memory_management.patch by
  bind-9.5-gssapictx-free.patch which conforms BIND coding standards
  (#251853)

* Tue Aug 21 2007 Adam Tkac <atkac redhat com> 32:9.5.0-10.a6
- dropped direct dependency to /etc/openldap/schema directory
- changed hardcoded paths to macros
- fired away code which configure LDAP server

* Tue Aug 14 2007 Adam Tkac <atkac redhat com> 32:9.5.0-9.1.a6
- named could crash with SRV record UPDATE (#251336)

* Mon Aug 13 2007 Adam Tkac <atkac redhat com> 32:9.5.0-9.a6
- disable 64bit dlz driver patch on alpha and ia64 (#251298)
- remove wrong malloc functions from lib/dns/spnego.c (#251853)

* Mon Aug 06 2007 Adam Tkac <atkac redhat com> 32:9.5.0-8.2.a6
- changed licence from BSD-like to ISC

* Tue Jul 31 2007 Adam Tkac <atkac redhat com> 32:9.5.0-8.1.a6
- disabled named on all runlevels by default

* Mon Jul 30 2007 Adam Tkac <atkac redhat com> 32:9.5.0-8.a6
- minor next improvements on autotools patch
- dig and host utilities now using libidn instead idnkit for
  IDN support

* Wed Jul 25 2007 Warren Togami <wtogami@redhat.com> 32:9.5.0-7.a6
- binutils/gcc bug rebuild (#249435)

* Tue Jul 24 2007 Adam Tkac <atkac redhat com> 32:9.5.0-6.a6
- updated to 9.5.0a6 which contains fixes for CVE-2007-2925 and
  CVE-2007-2926
- fixed building on 64bits

* Mon Jul 23 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-5
- integrated "autotools" patch for testing purposes (upstream will
  accept it in future, for easier building)

* Mon Jul 23 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-4.1
- fixed DLZ drivers building on 64bit systems

* Fri Jul 20 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-4
- fixed relation between logrotated and chroot-ed named

* Wed Jul 18 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-3.9
- removed bind-sdb package (default named has compiled SDB backend now)
- integrated DLZ (Dynamically loadable zones) drivers
- integrated GSS-TSIG support (RFC 3645)
- build with -O0 (many new features, potential core dumps will be more useful)

* Tue Jul 17 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-3.2
- initscript should be ready for parallel booting (#246878)

* Tue Jul 17 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-3
- handle integer overflow in isc_time_secondsastimet function gracefully (#247856)

* Mon Jul 16 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-2.2
- moved chroot configfiles into chroot subpackage (#248306)

* Mon Jul 02 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-2
- minor changes in default configuration
- fix h_errno assigment during resolver initialization (unbounded recursion, #245857)
- removed wrong patch to #150288

* Tue Jun 19 2007 Adam Tkac <atkac redhat com> 31:9.5.0a5-1
- updated to latest upstream

* Wed Jun 13 2007 Adam Tkac <atkac redhat com> 31:9.4.1-7
- marked caching-nameserver as obsolete (#244604)
- fixed typo in initscript (causes that named doesn't detect NetworkManager
  correctly)
- next cleanup in configuration - moved configfiles into config.tar
- removed delay between start & stop in restart function in named.init

* Tue Jun 12 2007 Adam Tkac <atkac redhat com> 31:9.4.1-6
- major changes in initscript. Could be LSB compatible now
- removed caching-nameserver subpackage. Move configs from this
  package to main bind package as default configuration and major
  configuration cleanup

* Mon Jun 04 2007 Adam Tkac <atkac redhat com> 31:9.4.1-5
- very minor compatibility change in bind-chroot-admin (line 215)
- enabled IDN support by default and don't distribute IDN libraries
- specfile cleanup
- add dynamic directory to /var/named. This directory will be primarily used for
  dynamic DNS zones. ENABLE_ZONE_WRITE and SELinux's named_write_master_zones no longer exist

* Thu May 24 2007 Adam Tkac <atkac redhat com> 31:9.4.1-4
- removed ldap-api patch and start using deprecated API
- fixed minor problem in bind-chroot-admin script (#241103)

* Tue May 22 2007 Adam Tkac <atkac redhat com> 31:9.4.1-3
- fixed bind-chroot-admin dynamic DNS handling (#239149)
- updated zone-freeze patch to latest upstream
- ldap sdb has been rewriten to latest api (#239802)

* Mon May 07 2007 Adam Tkac <atkac redhat com> 31:9.4.1-2.fc7
- test build on new build system

* Wed May 02 2007 Adam Tkac <atkac redhat com> 31:9.4.1-1.fc7
- updated to 9.4.1 which contains fix to CVE-2007-2241

* Fri Apr 27 2007 Adam Tkac <atkac redhat com> 31:9.4.0-8.fc7
- improved "zone freeze patch" - if multiple zone with same name exists
  no zone is freezed
- minor cleanup in caching-nameserver's config file
- fixed race-condition in dbus code (#235809)
- added forgotten restorecon statement in bind-chroot-admin

* Tue Apr 17 2007 Adam Tkac <atkac redhat com> 31:9.4.0-7.fc7
- removed DEBUGINFO option because with this option (default) was bind
  builded with -O0 and without this flag no debuginfo package was produced.
  (I want faster bind => -O2 + debuginfo)
- fixed zone finding (#236426)

* Mon Apr 16 2007 Adam Tkac <atkac redhat com> 31:9.4.0-6.fc7
- added idn support (still under development with upstream, disabled by default)

* Wed Apr 11 2007 Adam Tkac <atkac redhat com> 31:9.4.0-5.fc7
- dnssec-signzone utility now doesn't ignore -d parameter

* Tue Apr 10 2007 Adam Tkac <atkac redhat com> 31:9.4.0-4.fc7
- removed query-source[-v6] options from caching-nameserver config
  (#209954, increase security)
- throw away idn. It won't be ready in fc7

* Tue Mar 13 2007 Adam Tkac <atkac redhat com> 31:9.4.0-3.fc7
- prepared bind to merge review
- added experimental idn support to bind-utils utils (not enabled by default yet)
- change chroot policy in caching-nameserver post section
- fixed bug in bind-chroot-admin - rootdir function is called properly now

* Mon Mar 12 2007 Adam Tkac <atkac redhat com> 31:9.4.0-2.fc7
- added experimental SQLite support (written by John Boyd <jaboydjr@netwalk.com>)
- moved bind-chroot-admin script to chroot package
- bind-9.3.2-redhat_doc.patch is always applied (#231738)

* Tue Mar 06 2007 Adam Tkac <atkac@redhat.com> 31:9.4.0-1.fc7
- updated to 9.4.0
- bind-chroot-admin now sets EAs correctly (#213926)
- throw away next_server_on_referral and no_servfail_stops patches (fixed in 9.4.0)

* Thu Feb 15 2007 Adam Tkac <atkac@redhat.com> 31:9.3.4-7.fc7
- minor cleanup in bind-chroot-admin script

* Fri Feb 09 2007 Adam Tkac <atkac@redhat.com> 31:9.3.4-6.fc7
- fixed broken bind-chroot-admin script (#227995)

* Wed Feb 07 2007 Adam Tkac <atkac@redhat.com> 31:9.3.4-5.fc7
- bind-chroot-admin now uses correct chroot path (#227600)

* Mon Feb 05 2007 Adam Tkac <atkac@redhat.com> 31:9.3.4-4.fc7
- fixed conflict between bind-sdb and ldap
- removed duplicated bind directory in bind-libs

* Thu Feb 01 2007 Adam Tkac <atkac@redhat.com> 31:9.3.4-3.fc7
- fixed building without libbind
- fixed post section (selinux commands is now in if-endif statement)
- prever macro has been removed from version

* Mon Jan 29 2007 Adam Tkac <atkac@redhat.com> 31:9.3.4-2.fc7
- redirected output from bind-chroot prep and %%preun stages to /dev/null

* Thu Jan 25 2007 Adam Tkac <atkac@redhat.com> 31:9.3.4-1.fc7
- updated to version 9.3.4 which contains security bugfixes

* Tue Jan 23 2007 Adam Tkac <atkac@redhat.com> 31:9.3.3-5.fc7
- package bind-libbind-devel has been marked as obsolete

* Mon Jan 22 2007 Adam Tkac <atkac@redhat.com> 31:9.3.3-4.fc7
- package bind-libbind-devel has beed removed (libs has been moved to bind-devel & bind-libs)
- Resolves: #214208

* Tue Jan 16 2007 Martin Stransky <stransky@redhat.com> - 31:9.3.3-3
- fixed a multi-lib issue
- Resolves: rhbz#222717

* Thu Jan 4 2007 Martin Stransky <stransky@redhat.com> - 31:9.3.3-2
- added namedGetForwarders written in shell (#176100),
  created by Baris Cicek <baris@nerd.com.tr>.

* Sun Dec 10 2006 Martin Stransky <stransky@redhat.com> - 31:9.3.3-1
- update to 9.3.3 final
- fix for #219069: file included twice in src.rpm

* Wed Dec 6 2006 Martin Stransky <stransky@redhat.com> - 31:9.3.3-0.1.rc3
- added back an interval to restart
- renamed package, it should meet the N-V-R criteria
- fix for #216185: bind-chroot-admin able to change root mode 750
- added fix from #215997: incorrect permissions on dnszone.schema
- added a notice to init script when /etc/named.conf doesn't exist (#216075)

* Mon Oct 30 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.3-6
- fix for #200465: named-checkzone and co. cannot be run as non-root user
- fix for #212348: chroot'd named causes df permission denied error
- fix for #211249, #211083 - problems with stopping named
- fix for #212549: init script does not unmount /proc filesystem
- fix for #211282: EDNS is globally enabled, crashing CheckPoint FW-1,
    added edns-enable options to named configuration file which can suppress
    EDNS in queries to DNS servers (see /usr/share/doc/bind-9.3.3/misc/options)
- fix for #212961: bind-chroot doesn't clean up its mess on %%preun
- update to 9.3.3rc3, removed already merged patches

* Fri Oct 13 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.3-5
- fix for #209359: bind-libs from compatlayer CD will not 
  install on ia64

* Tue Oct 10 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.3-4
- added fix for #210096: warning: group named does not exist - using root

* Thu Oct  5 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.3-3
- added fix from #209400 - Bind Init Script does not create 
  the PID file always, created by Jeff Means
- added timeout to stop section of init script. 
  The default is 100 sec. and can be adjusted by NAMED_SHUTDOWN_TIMEOUT
  shell variable.

* Mon Oct  2 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.3-2
- removed chcon from %%post script, replaced by restorecon 
  (Bug 202547, comment no. 37)

* Fri Sep 15 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.3-1
- updated to the latest upstream (9.3.3rc2)

* Wed Sep  6 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.2-41
- added upstream patch for correct SIG handling - CVE-2006-4095

* Tue Sep  5 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.2-40
- suppressed messages from bind-chroot-admin
- cleared notes about bind-config

* Tue Aug 22 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.2-39
- added fix for #203522 - "bind-chroot-admin -e" command fails

* Mon Aug 21 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.2-38
- fix for #203194 - tmpfile usage

* Thu Aug 17 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.2-37
- fix for #202542 - /usr/sbin/bind-chroot-admin: No such file or directory
- fix for #202547 - file_contexts: invalid context

* Fri Aug 11 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.2-36
- added Provides: bind-config

* Fri Aug 11 2006 Martin Stransky <stransky@redhat.com> - 30:9.3.2-35
- fix bug 197493: renaming subpackage bind-config to caching-nameserver

* Mon Jul 24 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-34
- fix bug 199876: make '%%exclude libbbind.*' conditional on %%{LIBBIND}

* Mon Jul 24 2006 Florian La Roche <laroche@redhat.com> - 30:9.3.2-33
- fix #195881, perms are not packaged correctly

* Fri Jul 21 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-32
- fix addenda to bug 189789: 
  determination of selinux enabled was still not 100% correct in bind-chroot-admin
- fix addenda to bug 196398:
  make named.init test for NetworkManager being enabled AFTER testing for -D absence;
  named.init now supports a 'DISABLE_NAMED_DBUS' /etc/sysconfig/named setting to disable
  auto-enable of named dbus support if NetworkManager enabled.

* Wed Jul 19 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-30
- fix bug 196398 - Enable -D option automatically in initscript
  if NetworkManager enabled in any runlevel.
- fix namedGetForwarders for new dbus
- fix bug 195881 - libbind.so should be owned by bind-libbind-devel

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 30:9.3.2-28.FC6
- Rebuild against new dbus

* Wed Jul 12 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-27.FC6
- rebuild with fixed glibc-kernheaders

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 30:9.3.2-26.FC6.1
- rebuild

* Wed Jun 14 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-26.FC6
- fix bugs 191093, 189789
- backport selected fixes from upstream bind9 'v9_3_3b1' CVS version:
  ( see http://www.isc.org/sw/bind9.3.php "Fixes" ): 
  o change 2024 / bug 16027:
    named emitted spurious "zone serial unchanged" messages on reload
  o change 2013 / bug 15941:
    handle unexpected TSIGs on unsigned AXFR/IXFR responses more gracefully
  o change 2009 / bug 15808: coverity fixes
  o change 1997 / bug 15818: 
    named was failing to replace negative cache entries when a positive one
    for the type was learnt
  o change 1994 / bug 15694: OpenSSL 0.9.8 support
  o change 1991 / bug 15813:
    The configuration data, once read, should be treated as readonly.
  o misc. validator fixes 
  o misc. resolver fixes
  o misc. dns fixes
  o misc. isc fixes
  o misc. libbind fixes
  o misc. isccfg fix
  o misc. lwres fix
  o misc. named fixes
  o misc. dig fixes
  o misc. nsupdate fix
  o misc. tests fixes

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 30:9.3.2-24.FC6
- and actually put the devel symlinks in the right subpackage

* Thu May 25 2006 Jeremy Katz <katzj@redhat.com> - 30:9.3.2-23.FC6
- rebuild for -devel deps

* Tue Apr 18 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-22
- apply upstream patch for ncache_adderesult segfault bug 173961 addenda
- fix bug 188382: rpm --verify permissions inconsistencies
- fix bug 189186: use /sbin/service instead of initscript
- rebuild for new gcc, glibc-kernheaders

* Tue Apr 04 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-20
- fix resolver.c ncache_adderesult segfault reported in addenda to bug 173961 
  (upstream bugs #15642, #15528 ?)
- allow named ability to generate core dumps after setuid (upstream bug #15753)

* Mon Apr 03 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-18
- fix bug 187529: make bind-chroot-admin deal with subdirectories properly

* Thu Mar 30 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-16
- fix bug 187286: 
     prevent host(1) printing duplicate 'is an alias for' messages
     for the default AAAA and MX lookups as well as for the A lookup
     (it now uses the CNAME returned for the A lookup for the AAAA and MX lookups).
     This is upstream bug #15702 fixed in the unreleased bind-9.3.3
- fix bug 187333: fix SOURCE24 and SOURCE25 transposition

* Wed Mar 29 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-14
- fix bug 186577: remove -L/usr/lib from libbind.pc and more .spec file cleanup
- add '%%doc' sample configuration files in /usr/share/doc/bind*/sample
- rebuild with new gcc and glibc

* Wed Mar 22 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-12
- fix typo in initscript
- fix Requires(post): policycoreutils in sub-packages

* Mon Mar 20 2006 Jason Vas Dias <jvdias@redhat.com> - 30.9.3.2-10
- fix bug 185969: more .spec file cleanup

* Wed Mar 08 2006 Jason Vas Dias <jvdias@redhat.com> - 30.9.3.2-8
- Do not allow package to be installed if named:25 userid creation fails
- Give libbind a pkg-config file
- remove restorecon from bind-chroot-admin (not required).
- fix named.caching-nameserver.conf (listen-on-v6 port 53 { ::1 };)

* Tue Mar 07 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-7
- fix issues with bind-chroot-admin

* Mon Mar 06 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-6
- replace caching-nameserver with bind-config sub-package
- fix bug 177595: handle case where $ROOTDIR is a link in initscript
- fix bug 177001: bind-config creates symlinks OK now
- fix bug 176388: named.conf is now never replaced by any RPM
- fix bug 176248: remove unecessary creation of rpmsave links
- fix bug 174925: no replacement of named.conf
- fix bug 173963: existing named.conf never modified
- major .spec file cleanup

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 30:9.3.2-4.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-4
- regenerate redhat_doc patch for non-DBUS builds
- allow dbus builds to work with dbus version < 0.6 (bz #179816)

* Tue Feb 07 2006 Florian La Roche <laroche@redhat.com> 30:9.3.2-3
- try supporting without dbus support

* Mon Feb 06 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-2.1
- Rebuild for new gcc, glibc, glibc-kernheaders

* Mon Jan 16 2006 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-2
- fix bug 177854: temporary fix for broken kernel-2.6.15-1854+
  /proc/net/if_inet6 format

* Wed Dec 21 2005 Jason Vas Dias <jvdias@redhat.com> - 30:9.3.2-1
- Upgrade to 9.3.2, released today

* Tue Dec 20 2005 Jason Vas Dias <jvdias@redhat.com> - 28:9.3.2rc1-2
- fix bug 176100: do not Require: perl just for namedGetForwarders !

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec 02 2005 Jason Vas Dias <jvdias@redhat.com> - 28:9.3.2rc-1
- Upgrade to upstream version 9.3.2rc1
- fix namedSetForwarders -> namedGetForwarders SOURCE14 typo

* Thu Dec 01 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-26
- rebuild for new dbus 0.6 dependency; remove use of
  DBUS_NAME_FLAG_PROHIBIT_REPLACEMENT

* Wed Nov 23 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-24
- allow D-BUS support to work in bind-chroot environment:
  workaround latest selinux policy by mounting /var/run/dbus/
  under chroot instead of /var/run/dbus/system-bus-socket

* Sun Nov 13 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-22
- fix bug 172632 - remove .la files
- ship namedGetForwarders and namedSetForwarders scripts
- fix detection of -D option in chroot

* Tue Nov  8 2005 Tomas Mraz <tmraz@redhat.com> - 24:9.3.1-21
- rebuilt with new openssl

* Wed Oct 19 2005 Jason Vas Dias <jvdias@redhat.com> - 24.9.3.1-20
- Allow the -D enable D-BUS option to be used within bind-chroot .
- fix bug 171226: supply some documentation for pgsql SDB .

* Thu Oct 06 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-18
- fix bug 169969: do NOT call dbus_svc_dispatch() in dbus_mgr_init_dbus() -
      task->state != task_ready and will cause Abort in task.c if process
      is waiting for NameOwnerChanged to do a SetForwarders

* Wed Oct 05 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-16
- Fix reconnecting to dbus-daemon after it stops & restarts .

* Tue Sep 27 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-14
- When forwarder nameservers are changed with D-BUS, flush the cache.

* Mon Sep 26 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-12
- fix bug 168302: use %%{__cc} for compiling dns-keygen
- fix bug 167682: bind-chroot directory permissions
- fix issues with -D dbus option when dbus service not running or disabled

* Tue Aug 30 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-12
- fix bug 167062: named should be started after syslogd by default

* Mon Aug 22 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-11
- fix bug 166227: host: don't do default AAAA and MX lookups with '-t a' option

* Tue Aug 16 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-10
- Build with D-BUS patch by default; D-BUS support enabled with named -D option
- Enable D-BUS for named_sdb also
- fix sdb pgsql's zonetodb.c: must use isc_hash_create() before dns_db_create()
- update fix for bug 160914 : test for RD=1 and ARCOUNT=0 also before trying next server
- fix named.init script to handle named_sdb properly
- fix named.init script checkconfig() to handle named '-c' option
  and make configtest, test, check configcheck synonyms

* Tue Jul 19 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-8
- fix named.init script bugs 163598, 163409, 151852(addendum)

* Tue Jul 12 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-7
- fix bug 160914: resolver utilities should try next server on empty referral
                  (now that glibc bug 162625 is fixed)
                  host and nslookup now by default try next server on SERVFAIL
                  (host now has '-s' option to disable, and nslookup given
                   '[no]fail' option similar to dig's [no]fail option).
- rebuild and re-test with new glibc & gcc (all tests passed).

* Tue May 31 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-6
- fix bug 157950: dig / host / nslookup should reject invalid resolv.conf
                  files and not use uninitialized garbage nameserver values
                  (ISC bug 14841 raised).

* Mon May 23 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-4_FC4
- Fix SDB LDAP

* Mon May 16 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-4
- Fix bug 157601: give named.init a configtest function
- Fix bug 156797: named.init should check SELinux booleans.local before booleans
- Fix bug 154335: if no controls in named.conf, stop named with -TERM sig, not rndc
- Fix bug 155848: add NOTES section to named.8 man-page with info on all Red Hat
                  BIND quirks and SELinux DDNS / slave zone file configuration
- D-BUS patches NOT applied until dhcdbd is in FC

* Sun May 15 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-4_dbus
- Enhancement to allow dynamic forwarder table management and
- DHCP forwarder auto-configuration with D-BUS

* Thu Apr 14 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-2_FC4
- Rebuild for bind-sdb libpq.so.3 dependency
- fix bug 150981: don't install libbind man-pages if no libbind
- fix bug 151852: mount proc on $ROOTDIR/proc to allow sysconf(...)
  to work and correct number of CPUs to be determined

* Fri Mar 11 2005 Jason Vas Dias <jvdias@redhat.com> - 24:9.3.1-1_FC4
- Upgrade to ISC BIND 9.3.1 (final release) released today.

* Wed Mar  9 2005 Jason Vas Dias <jvdias@redhat.com> - 22.9.3.1rc1-5
- fix bug 150288: h_errno not being accessed / set correctly in libbind
- add libbind man-pages from bind-8.4.6

* Mon Mar  7 2005 Jason Vas Dias <jvdias@redhat.com> - 22:9.3.1rc1-4
- Rebuild with gcc4 / glibc-2.3.4-14.

* Tue Mar  1 2005 Nalin Dahyabhai <nalin@redhat.com> - 22:9.3.1rc1-3
- configure with --with-pic to get PIC libraries

* Sun Feb 20 2005 Jason Vas Dias <jvdias@redhat.com> - 22:9.3.1rc1-2
- fix bug 149183: don't use getifaddrs() .

* Wed Feb 16 2005 Jason Vas Dias <jvdias@redhat.com> - 22:9.3.1rc1-1
- Upgrade to 9.3.1rc1
- Add Simplified Database Backend (SDB) sub-package ( bind-sdb )
-     add named_sdb - ldap + pgsql + dir database backend support with
-     'ENABLE_SDB' named.sysconfig option
- Add BIND resolver library & includes sub-package ( libbind-devel)
- fix bug 147824 / 147073 / 145664: ENABLE_ZONE_WRITE in named.init
- fix bug 146084 : shutup restorecon

* Tue Jan 11 2005 Jason Vas Dias <jvdias@redhat.com> - 22:9.3.0-2
- Fix bug 143438: named.init will now make correct ownership of $ROOTDIR/var/named
-                 based on 'named_write_master_zones' SELinux boolean.
- Fix bug 143744: dig & nsupdate IPv6 timeout  (dup of 140528)

* Mon Nov 29 2004 Jason Vas Dias <jvdias@redhat.com> - 9.3.0-1
- Upgrade BIND to 9.3.0 in Rawhide / FC4 (bugs 134529, 133654...)

* Mon Nov 29 2004 Jason Vas Dias <jvdias@redhat.com> - 20:9.2.4-4
- Fix bugs 140528 and 141113:
- 2 second timeouts when IPv6 not configured and root nameserver's
- AAAA addresses are queried

* Mon Oct 18 2004 Jason Vas Dias <jvdias@redhat.com> - 20:9.2.4-2
- Fix bug 136243: bind-chroot %%post must run restorecon -R %%{prefix}
- Fix bug 135175: named.init must return non-zero if named is not run
- Fix bug 134060: bind-chroot %%post must use mktemp, not /tmp/named
- Fix bug 133423: bind-chroot %%files entries should have been %%dirs

* Thu Sep 23 2004 Jason Vas Dias <jvdias@redhat.com> - 20:9.2.4-1
- BIND 9.2.4 (final release) released - source code actually
- identical to 9.2.4rc8, with only version number change.

* Mon Sep 20 2004 Jason Vas Dias <jvdias@redhat.com> - 10:9.2.4rc8-14
- Upgrade to upstream bind-9.2.4rc8 .
- Progress: Finally! Hooray! ISC bind now distributes:
- o named.conf(5) and nslookup(8) manpages
-    'bind-manpages.bz2' source can now disappear
-    (could this have something to do with ISC bug I raised about this?)
- o 'deprecation_msg' global has vanished
-     bind-9.2.3rc3-deprecation_msg_shut_up.diff.bz2 can disappear

* Mon Sep 20 2004 Jason Vas Dias <jvdias@redhat.com> - 10:9.2.4rc8-14
- Fix bug 106572/132385: copy /etc/localtime to chroot on start

* Fri Sep 10 2004 Jason Vas Dias <jvdias@redhat.com> - 10:9.2.4rc7-12_EL3
- Fix bug 132303: if ROOTDIR line was replaced after upgrade from
- bind-chroot-9.2.2-21, restart named

* Wed Sep 8  2004 Jason Vas Dias <jvdias@redhat.com> - 10:9.2.4rc7-11_EL3
- Fix bug 131803: replace ROOTDIR line removed by broken
- bind-chroot 9.2.2-21's '%%postun'; added %%triggerpostun for bind-chroot

* Tue Sep 7  2004 Jason Vas Dias <jvdias@redhat.com> - 10:9.2.4rc7-10_EL3
- Fix bugs 130121 & 130981 for RHEL-3

* Mon Aug 30 2004 Jason Vas Dias <jvdias@redhat.com> - 10:9.2.4rc7-10
- Fix bug 130121: add '%%ghost' entries for files included in previous
- bind-chroot & not in current - ie. named.conf, rndc.key, dev/* -
- that RPM removed after upgrade .

* Thu Aug 26 2004 Jason Vas Dias <jvdias@redhat.com>
- Fix bug 130981: add '-t' option to named-checkconf invocation in
- named.init if chroot installed.

* Wed Aug 25 2004 Jason Vas Dias <jvdias@redhat.com>
- Remove resolver(5) manpage now in man-pages (bug 130792);
- Don't create /dev/ entries in bind-chroot if already there (bug 127556);
- fix bind-devel Requires (bug 130919)
- Set default location for dumpdb & stats files to /var/named/data

* Tue Aug 24 2004 Jason Vas Dias <jvdias@redhat.com>
- Fix devel Requires for bug 130738 & fix version

* Tue Aug 24 2004 Jason Vas Dias <jvdias@redhat.com>
- Fix errors on clean install if named group does not exist
- (bug 130777)

* Thu Aug 19 2004 Jason Vas Dias <jvdias@redhat.com>
- Upgrade to bind-9.2.4rc7; applied initscript fix
- for bug 102035.

* Mon Aug  9 2004 Jason Vas Dias <jvdias@redhat.com>
- Fixed bug 129289: bind-chroot install / deinstall
- on install, existing config files 'safe_replace'd
- with links to chroot copies; on uninstall, moved back.

* Fri Aug  6 2004 Jason Vas Dias <jvdias@redhat.com>
- Fixed bug 129258: "${prefix}/var/tmp" typo in spec

* Wed Jul 28 2004 Jason Vas Dias <jvdias@redhat.com>
- Fixed bug 127124 : 'Requires: kernel >= 2.4'
- causes problems with Linux VServers

* Tue Jul 27 2004 Jason Vas Dias <jvdias@redhat.com>
- Fixed bug 127555 : chroot tar missing var/named/slaves

* Fri Jul 16 2004 Jason Vas Dias <jvdias@redhat.com>
- Upgraded to ISC version 9.2.4rc6

* Fri Jul 16 2004 Jason Vas Dias <jvdias@redhat.com>
- Fixed named.init generation of error messages on
- 'service named stop' and 'service named reload'
- as per bug 127775

* Wed Jun 23 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-19
- Bump for rhel 3.0  U3

* Wed Jun 23 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-18
- remove disable-linux-caps

* Wed Jun 16 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-17
- Update RHEL3 to latest bind

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 8 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-15
- Remove device files from chroot,  Named uses the system one

* Fri Mar 26 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-14
- Move RFC to devel package

* Fri Mar 26 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-13
- Fix location of restorecon

* Thu Mar 25 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-12
- Tighten security on config files.  Should be owned by root

* Thu Mar 25 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-11
- Update key patch to include conf-keygen

* Tue Mar 23 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-10
- fix chroot to only happen once.
- fix init script to do kill insteall of killall

* Mon Mar 15 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-9
- Add fix for SELinux security context

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Feb 28 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- run ldconfig for libs subrpm

* Mon Feb 23 2004 Tim Waugh <twaugh@redhat.com>
- Use ':' instead of '.' as separator for chown.

* Tue Feb 17 2004 Daniel Walsh <dwalsh@redhat.com> 9.2.3-7
- Add COPYRIGHT

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Dec 30 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.3-5
- Add defattr to libs

* Mon Dec 29 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.3-4
- Break out library package

* Mon Dec 22 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.3-3
- Fix condrestart

* Wed Nov 12 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.3-2
- Move libisc and libdns to bind from bind-util

* Tue Nov 11 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.3-1
- Move to 9.2.3

* Mon Oct 27 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2.P3-10
- Add PIE support

* Fri Oct 17 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2.P3-9
- Add /var/named/slaves directory

* Sun Oct 12 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- do not link against libnsl, not needed for Linux

* Wed Oct 8 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2.P3-6
- Fix local time in log file

* Tue Oct 7 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2.P3-5
- Try again

* Mon Oct 6 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2.P3-4
- Fix handling of chroot -/dev/random

* Thu Oct 2 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2.P3-3
- Stop hammering stuff on update of chroot environment

* Mon Sep 29 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2.P3-2
- Fix chroot directory to grab all subdirectories

* Wed Sep 24 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2.P3-1
- New patch to support for "delegation-only"

* Wed Sep 17 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-23
- patch support for "delegation-only"

* Wed Jul 30 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-22
- Update to build on RHL

* Wed Jul 30 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-21
- Install libraries as exec so debug info will be pulled

* Sat Jul 19 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-20
- Remove BSDCOMPAT (BZ 99454)

* Tue Jul 15 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-19
- Update to build on RHL

* Tue Jul 15 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-18
- Change protections on /var/named and /var/chroot/named

* Tue Jun 17 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-17
- Update to build on RHL

* Tue Jun 17 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-16
- Update to build on RHEL

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 22 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-14
- Update to build on RHEL

* Tue Apr 22 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-13
- Fix config description of named.conf in chroot
- Change named.init script to check for existence of /etc/sysconfig/network

* Fri Apr 18 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-12
- Update to build on RHEL

* Fri Apr 18 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-11
- Update to build on RHEL

* Fri Apr 18 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-10
- Fix echo OK on starting/stopping service

* Fri Mar 28 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-9
- Update to build on RHEL

* Fri Mar 28 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-8
- Fix echo on startup

* Tue Mar 25 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-7
- Fix problems with chroot environment
- Eliminate posix threads

* Mon Mar 24 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-6
- Fix build problems

* Fri Mar 14 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-5
- Fix build on beehive

* Thu Mar 13 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-4
- build bind-chroot kit

* Tue Mar 11 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-3
- Change configure to use proper threads model

* Fri Mar 7 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-2
- update to 9.2.2

* Tue Mar 4 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.2-1
- update to 9.2.2

* Fri Jan 24 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.1-16
- Put a sleep in restart to make sure stop completes

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 7 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.1-14
- Separate /etc/rndc.key to separate file

* Tue Jan 7 2003 Nalin Dahyabhai <nalin@redhat.com> 9.2.1-13
- Use openssl's pkgconfig data, if available, at build-time.

* Mon Jan 6 2003 Daniel Walsh <dwalsh@redhat.com> 9.2.1-12
- Fix log rotate to use service named reload
- Change service named reload to give success/failure message [73770]
- Fix File checking [75710]
- Begin change to automatically run in CHROOT environment

* Tue Dec 24 2002 Daniel Walsh <dwalsh@redhat.com> 9.2.1-10
- Fix startup script to work like all others.

* Mon Dec 16 2002 Daniel Walsh <dwalsh@redhat.com> 9.2.1-9
- Fix configure to build on x86_64 platforms

* Wed Aug 07 2002 Karsten Hopp <karsten@redhat.de>
- fix #70583,  doesn't build on IA64

* Tue Jul 30 2002 Karsten Hopp <karsten@redhat.de> 9.2.1-8
- bind-utils shouldn't require bind

* Mon Jul 22 2002 Karsten Hopp <karsten@redhat.de> 9.2.1-7
- fix name of pidfine in logrotate script (#68842)
- fix owner of logfile in logrotate script (#41391)
- fix nslookup and named.conf man pages (output on stderr)
  (#63553, #63560, #63561, #54889, #57457)
- add rfc1912 (#50005)
- gzip all rfc's
- fix typo in keygen.c (#54870)
- added missing manpages (#64065)
- shutdown named properly with rndc stop (#62492)
- /sbin/nologin instead of /bin/false (#68607)
- move nsupdate to bind-utils (where the manpage already was) (#66209, #66381)
- don't kill initscript when rndc fails (reload)    (#58750)


* Mon Jun 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.1-5
- Fix #65975

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May  9 2002 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.1-2
- Move libisccc, lib isccfg and liblwres from bind-utils to bind,
  they're not required if you aren't running a nameserver.

* Fri May 03 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 9.2.1 release

* Thu Mar 14 2002 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-8
- Merge 30+ bug fixes from 9.2.1rc1 code

* Mon Mar 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-7
- Don't exit if /etc/named.conf doesn't exist if we're running
  chroot (#60868)
- Revert Elliot's changes, we do require specific glibc/glibc-kernheaders
  versions or bug #58335 will be back. "It compiles, therefore it works"
  isn't always true.

* Thu Feb 28 2002 Elliot Lee <sopwith@redhat.com> 9.2.0-6
- Fix BuildRequires (we don't need specific glibc/glibc-kernheaders
versions).
- Use _smp_mflags

* Wed Feb 20 2002 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-4
- rebuild, require recent autoconf, automake (#58335)

* Fri Jan 25 2002 Tim Powers <timp@redhat.com>
- rebuild against new libssl

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Nov 27 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-1
- 9.2.0

* Thu Nov 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-0.rc10.2
- 9.2.0rc10

* Mon Nov  5 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-0.rc8.2
- Fix up rndc.conf (#55574)

* Thu Oct 25 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-0.rc8.1
- rc8
- Enforce --enable-threads

* Mon Oct 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-0.rc7.1
- 9.2.0rc7
- Use rndc status for "service named status", it's supposed to actually
  work in 9.2.x.

* Wed Oct  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-0.rc5.1
- 9.2.0rc5
- Fix rpm --rebuild with ancient libtool versions (#53938, #54257)

* Tue Sep 25 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-0.rc4.1
- 9.2.0rc4

* Fri Sep 14 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.2.0-0.rc3.1
- 9.2.0rc3
- remove ttl patch, I don't think we need this for 8.0.
- remove dig.1.bz2 from the bind8-manpages tar file, 9.2 has a new dig man page
- add lwres* man pages to -devel

* Mon Sep  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-4
- Make sure /etc/rndc.conf isn't world-readable even after the
  %%post script inserted a random key (#53009)

* Thu Jul 19 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-3
- Add build dependencies (#49368)
- Make sure running service named start several times doesn't create
  useless processes (#47596)
- Work around the named parent process returning 0 even if the config
  file is broken (it's parsed later by the child processes) (#45484)

* Mon Jul 16 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-2
- Don't use rndc status, it's not yet implemented (#48839)

* Sun Jul 08 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 9.1.3 release

* Tue Jul  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc3.1
- Fix up rndc configuration and improve security (#46586)

* Tue Jun 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc2.2
- Sync with caching-nameserver-7.1-6

* Mon Jun 25 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc2.1
- Update to rc2

* Fri Jun  1 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc1.3
- Remove resolv.conf(5) man page, it's now in man-pages

* Thu May 31 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc1.2
- Add named.conf man page from bind 8.x (outdated, but better than nothing,
  #42732)
- Rename the rndc key (#42895)
- Add dnssec* man pages

* Mon May 28 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc1.1
- 9.1.3rc1
- s/Copyright/License/

* Mon May  7 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.2-1
- 9.1.2 final. No changes between 9.1.2-0.rc1.1 and this one, except for
  the version number, though.

* Thu May  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.2-0.rc1.1
- 9.1.2rc1

* Thu Mar 29 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.1-1
- 9.1.1

* Thu Mar 15 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.0-10
- Merge fixes from 9.1.1rc5

* Sun Mar 11 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.0-9
- Work around bind 8 -> bind 9 migration problem when using buggy zone files:
  accept zones without a TTL, but spew out a big fat warning. (#31393)

* Thu Mar  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add fixes from rc4

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Thu Mar  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- killall -HUP named if rndc reload fails (#30113)

* Tue Feb 27 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Merge some fixes from 9.1.1rc3

* Tue Feb 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Don't use the standard rndc key from the documentation, instead, create a random one
  at installation time (#26358)
- Make /etc/rndc.conf readable by user named only, it contains secret keys

* Tue Feb 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.1 probably won't be out in time, revert to 9.1.0 and apply fixes
  from 9.1.1rc2
- bind requires bind-utils (#28317)

* Tue Feb 13 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to rc2, fixes 2 more bugs
- Fix build with glibc >= 2.2.1-7

* Thu Feb  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to 9.1.1rc1; fixes 17 bugs (14 of them affecting us;
  1 was fixed in a Red Hat patch already, 2 others are portability
  improvements)

* Wed Feb  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Remove initscripts 5.54 requirement (#26489)

* Mon Jan 29 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add named-checkconf, named-checkzone (#25170)

* Mon Jan 29 2001 Trond Eivind Glomsrod <teg@redhat.com>
- use echo, not gprintf

* Wed Jan 24 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix problems with $GENERATE
  Patch from Daniel Roesen <droesen@entire-systems.com>
  Bug #24890

* Thu Jan 18 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0 final

* Sat Jan 13 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0rc1
- i18nify init script
- bzip2 source to save space

* Thu Jan 11 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix %%postun script

* Tue Jan  9 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0b3

* Mon Jan  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add named.conf man page from bind8 (#23503)

* Sun Jan  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Make /etc/rndc.conf and /etc/sysconfig/named noreplace
- Make devel require bind = %%{version} rather than just bind

* Sun Jan  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix init script for real

* Sat Jan  6 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix init script when ROOTDIR is not set

* Thu Jan  4 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add hooks for setting up named to run chroot (RFE #23246)
- Fix up requirements

* Fri Dec 29 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0b2

* Wed Dec 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Move run files to /var/run/named/ - /var/run isn't writable
  by the user we're running as. (Bug #20665)

* Tue Dec 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix reverse lookups (#22272)
- Run ldconfig in %%post utils

* Tue Dec 12 2000 Karsten Hopp <karsten@redhat.de>
- fixed logrotate script (wrong path to kill)
- include header files in -devel package
- bugzilla #22049, #19147, 21606

* Fri Dec  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0b1 (9.1.0 is in our timeframe and less buggy)

* Mon Nov 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.0.1

* Mon Oct 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix initscript (Bug #19956)
- Add sample rndc.conf (Bug #19956)
- Fix build with tar 1.13.18

* Tue Oct 10 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Add some missing man pages (taken from bind8) (Bug #18794)

* Sun Sep 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.0.0 final

* Wed Aug 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rc5
- fix up nslookup

* Thu Aug 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rc4

* Thu Jul 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.0.0rc1

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul  9 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add "exit 0" for uninstall case

* Fri Jul  7 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add prereq init.d and cleanup install section

* Fri Jun 30 2000 Trond Eivind Glomsrod <teg@redhat.com>
- fix the init script

* Wed Jun 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- make libbind.a and nslookup.help readable again by setting INSTALL_LIB to ""

* Mon Jun 26 2000 Bernhard Rosenkranzer <bero@redhat.com>
- Fix up the initscript (Bug #13033)
- Fix build with current glibc (Bug #12755)
- /etc/rc.d/init.d -> /etc/init.d
- use %%{_mandir} rather than /usr/share/man

* Mon Jun 19 2000 Bill Nottingham <notting@redhat.com>
- fix conflict with man-pages
- remove compatibilty chkconfig links
- initscript munging

* Wed Jun 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify logrotate setup to use PID file
- temporarily disable optimization by unsetting $RPM_OPT_FLAGS at build-time
- actually bump the release this time

* Sun Jun  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- FHS compliance

* Mon Apr 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- clean up restart patch

* Mon Apr 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- provide /var/named (fix for bugs #9847, #10205)
- preserve args when restarted via ndc(8) (bug #10227)
- make resolv.conf(5) a link to resolver(5) (bug #10245)
- fix SYSTYPE bug in all makefiles
- move creation of named user from %%post into %%pre

* Mon Feb 28 2000 Bernhard Rosenkranzer <bero@redhat.com>
- Fix TTL (patch from ISC, Bug #9820)

* Wed Feb 16 2000 Bernhard Rosenkranzer <bero@redhat.com>
- fix typo in spec (it's %%post, without a leading blank) introduced in -6
- change SYSTYPE to linux

* Fri Feb 11 2000 Bill Nottingham <notting@redhat.com>
- pick a standard < 100 uid/gid for named

* Fri Feb 04 2000 Elliot Lee <sopwith@redhat.com>
- Pass named a '-u named' parameter by default, and add/remove user.

* Thu Feb  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- fix host mx bug (Bug #9021)

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies
- man pages are compressed

* Wed Jan 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- It's /usr/bin/killall, not /usr/sbin/killall (Bug #8063)

* Mon Jan 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up location of named-bootconf.pl and make it executable
  (Bug #8028)
- bind-devel requires bind

* Mon Nov 15 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- update to 8.2.2-P5

* Wed Nov 10 1999 Bill Nottingham <notting@redhat.com>
- update to 8.2.2-P3

* Tue Oct 12 1999 Cristian Gafton <gafton@redhat.com>
- add patch to stop a cache only server from complaining about lame servers
  on every request.

* Fri Sep 24 1999 Preston Brown <pbrown@redhat.com>
- use real stop and start in named.init for restart, not ndc restart, it has
  problems when named has changed during a package update... (# 4890)

* Fri Sep 10 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %%preun, not %%postun

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Mon Jul 26 1999 Bill Nottingham <notting@redhat.com>
- fix installed chkconfig links to match init file

* Sat Jul  3 1999 Jeff Johnson <jbj@redhat.com>
- conflict with new (in man-1.24) man pages (#3876,#3877).

* Tue Jun 29 1999 Bill Nottingham <notting@redhat.com>
- fix named.logrotate (wrong %%SOURCE)

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 8.2.1.
- add named.logrotate (#3571).
- hack around egcs-1.1.2 -m486 bug (#3413, #3485).
- vet file list.

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- don't run by default

* Sun May 30 1999 Jeff Johnson <jbj@redhat.com>
- nslookup fixes (#2463).
- missing files (#3152).

* Sat May  1 1999 Stepan Kasal <kasal@math.cas.cz>
- nslookup patched:
  to count numRecords properly
  to fix subsequent calls to ls -d
  to parse "view" and "finger" commands properly
  the view hack updated for bind-8 (using sed)

* Wed Mar 31 1999 Bill Nottingham <notting@redhat.com>
- add ISC patch
- add quick hack to make host not crash
- add more docs

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add probing information in the init file to keep linuxconf happy
- dont strip libbind

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- removed 'done' output at named shutdown.

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.2

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to use the __FDS_BITS macro
- build for glibc 2.1

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- change named.restart to /usr/sbin/ndc restart

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- install man pages correctly.
- change K10named to K45named.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- don't start if /etc/named.conf doesn't exist.

* Sat Aug  8 1998 Jeff Johnson <jbj@redhat.com>
- autmagically create /etc/named.conf from /etc/named.boot in %%post
- remove echo in %%post

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in 5.1 mods

* Sun Apr 12 1998 Manuel J. Galan <manolow@step.es>
- Several essential modifications to build and install correctly.
- Modified 'ndc' to avoid deprecated use of '-'

* Mon Dec 22 1997 Scott Lampert <fortunato@heavymetal.org>
- Used buildroot
- patched bin/named/ns_udp.c to use <libelf/nlist.h> for include
  on Redhat 5.0 instead of <nlist.h>
