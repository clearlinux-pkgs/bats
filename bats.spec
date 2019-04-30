#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bats
Version  : 1.1.0
Release  : 16
URL      : https://github.com/bats-core/bats-core/archive/v1.1.0.tar.gz
Source0  : https://github.com/bats-core/bats-core/archive/v1.1.0.tar.gz
Summary  : Battery status in the console
Group    : Development/Tools
License  : MIT
Requires: bats-bin = %{version}-%{release}
Requires: bats-libexec = %{version}-%{release}
Requires: bats-license = %{version}-%{release}
Requires: bats-man = %{version}-%{release}
Patch1: makefile.patch

%description
Bats is a TAP-compliant testing framework for Bash.
It provides a simple way to verify that the UNIX programs you write behave as expected.
Bats is most useful when testing software written in Bash, but you can use it to test any UNIX program.

%package bin
Summary: bin components for the bats package.
Group: Binaries
Requires: bats-libexec = %{version}-%{release}
Requires: bats-license = %{version}-%{release}

%description bin
bin components for the bats package.


%package libexec
Summary: libexec components for the bats package.
Group: Default
Requires: bats-license = %{version}-%{release}

%description libexec
libexec components for the bats package.


%package license
Summary: license components for the bats package.
Group: Default

%description license
license components for the bats package.


%package man
Summary: man components for the bats package.
Group: Default

%description man
man components for the bats package.


%prep
%setup -q -n bats-core-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556594931
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1556594931
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bats
cp LICENSE.md %{buildroot}/usr/share/package-licenses/bats/LICENSE.md
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bats

%files libexec
%defattr(-,root,root,-)
/usr/libexec/bats-core/bats
/usr/libexec/bats-core/bats-exec-suite
/usr/libexec/bats-core/bats-exec-test
/usr/libexec/bats-core/bats-format-tap-stream
/usr/libexec/bats-core/bats-preprocess

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bats/LICENSE.md

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bats.1
/usr/share/man/man7/bats.7
