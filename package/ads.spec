#
# spec file for package ads
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ads
Version:        2.0
Release:        0
Summary:        Swiss army knife for samba
License:        GPL-3.0
Group:          Productivity/Networking/Samba
Url:            https://github.com/suse-samba-tools/ads
Source:         %{name}-%{version}.tar.bz2
Requires:       krb5-client
Requires:       python3-dnspython
Requires:       python3-ldb
Requires:       python3-netifaces
Requires:       python3-python-pam
Requires:       samba-client
Requires:       samba-python3
Requires:       ntp
Requires:       samba-dsdb-modules
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  python3
BuildRequires:  python3-argparse-manpage
BuildRequires:  python3-dnspython
BuildRequires:  python3-ldb
BuildRequires:  python3-netifaces
BuildRequires:  python3-python-pam
BuildRequires:  samba-python3
Provides:       vasclnt vastool

%description
Active Directory services tool for samba.
For join, unjoin, provisioning, demotion, user/group and password administration,
ldap attribute modification, posix enablement, kdc timesync, pam and nss configuration,
daemon start/stop, cache flush, etc.
The ads command attempts to maintain compatibility with the proprietary vastool command,
while also adding additional features relevant to samba (such as kdc provisioning).

%prep
%setup -q

%build
autoreconf -if
%configure
make

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/ads
%{_bindir}/vastool
%{_mandir}/man1/ads.1*

%changelog
